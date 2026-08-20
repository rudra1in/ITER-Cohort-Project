"""
LangGraph ReAct Orchestrator
============================
  plan_query
      ↓
  retrieve
      ↓
  assess_sufficiency ──── sufficient ──→ generate_answer → save_memory
      │
      ├── needs_tools ──→ use_tools (ReAct loop, max 3 iterations)
      │                      │
      │                      └─── loop back to assess_sufficiency
      │
      └── needs_crew ───→ route_to_crew → generate_answer → save_memory

"""

import json
import logging
from typing import TypedDict, Optional, List, Annotated
import operator

from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver

logger = logging.getLogger(__name__)

 
# GRAPH STATE
 

class GraphState(TypedDict):

    # Inputs
    test_id: str
    session_id: str
    question: str

    # Derived 
    history: str
    query_plan: dict
    retrieval_results: List[dict]
    evidence: List[dict]
    answer: str
    mode: str           
    # "rag" | "tools" | "crew"
    # Non-event-shaped tool results (e.g. compare_candidates()'s
    # aggregate stats, get_event_detail()'s single record) that don't
    # fit the "event card" shape retrieval_results expects, but must
    # still reach generate_answer - manually accumulated across
    # iterations in _node_use_tools, so no reducer needed here.
    tool_context: List[str]

    #   Routing flags  
    needs_investigation: bool
    needs_tools: bool

    #   ReAct loop control  
    tool_calls: Annotated[List[dict], operator.add]
    iterations: int

    #   Error handling  
    error: Optional[str]


 
# ORCHESTRATOR
 

class LangGraphOrchestrator:
    """
    LangGraph-based orchestrator with ReAct tool loop and CrewAI
    escalation for complex investigation queries.
    """

    MAX_ITERATIONS = 3

    def __init__(
        self,
        rag,
        investigation_crew,
        database,
        retriever,
        embedding_service,
        memory
    ):

        self.rag = rag
        self.investigation_crew = investigation_crew
        self.database = database
        self.retriever = retriever
        self.embedding_service = embedding_service
        self.memory_store = memory

        # Build the LangGraph tools once.
        self._tools = self._build_tools()

        #compile the graph.
        self._graph = self._build_graph()

        self._checkpointer = MemorySaver()

        self._graph_with_memory = self._build_graph(
            checkpointer=self._checkpointer
        )

     
    # TOOL REGISTRY
     

    def _build_tools(self):
        """
        Build the five ReAct tools available to the graph's tool node.
        Each tool returns a plain dict / list (JSON-serialisable).
        """

        db = self.database
        retriever = self.retriever
        embedding_service = self.embedding_service

        def search_events(
            test_id: str,
            query: str,
            candidate_id: str = None,
            top_k: int = 8
        ) -> List[dict]:
            """Hybrid semantic + keyword search for behavioral events."""
            return retriever.search(
                test_id=test_id,
                query=query,
                top_k=top_k,
                candidate_id=candidate_id or None
            )

        def get_candidate_timeline(
            test_id: str,
            candidate_id: str
        ) -> List[dict]:
            """Return all behavioral events for one candidate in time order."""
            return db.get_candidate_timeline(test_id, candidate_id)

        def get_suspicious_events(
            test_id: str
        ) -> List[dict]:
            """Return all events that have been flagged as suspicious."""
            return db.get_suspicious_events(test_id)

        def get_event_detail(
            event_id: str
        ) -> Optional[dict]:
            """Return a full event record including evidence frame IDs."""
            return db.get_event(event_id)

        def compare_candidates(
            test_id: str
        ) -> List[dict]:
            """
            Return per-candidate, per-event-type aggregate statistics
            to support comparison questions.
            """
            return db.get_test_statistics(test_id)

        return {
            "search_events": search_events,
            "get_candidate_timeline": get_candidate_timeline,
            "get_suspicious_events": get_suspicious_events,
            "get_event_detail": get_event_detail,
            "compare_candidates": compare_candidates,
        }

     
    # GRAPH BUILDER
     

    def _build_graph(self, checkpointer=None):
        """Compile the LangGraph state machine."""

        builder = StateGraph(GraphState)

        #   Nodes  
        builder.add_node("plan_query", self._node_plan_query)
        builder.add_node("retrieve", self._node_retrieve)
        builder.add_node("assess_sufficiency", self._node_assess_sufficiency)
        builder.add_node("use_tools", self._node_use_tools)
        builder.add_node("route_to_crew", self._node_route_to_crew)
        builder.add_node("generate_answer", self._node_generate_answer)
        builder.add_node("save_memory", self._node_save_memory)

        #   Edges  
        builder.set_entry_point("plan_query")
        builder.add_edge("plan_query", "retrieve")
        builder.add_edge("retrieve", "assess_sufficiency")

        # Conditional after assess_sufficiency
        builder.add_conditional_edges(
            "assess_sufficiency",
            self._route_after_assess,
            {
                "generate_answer": "generate_answer",
                "use_tools": "use_tools",
                "route_to_crew": "route_to_crew",
            }
        )

        # Conditional after use_tools (loop or exit)
        builder.add_conditional_edges(
            "use_tools",
            self._route_after_tools,
            {
                "assess_sufficiency": "assess_sufficiency",
                "generate_answer": "generate_answer",
            }
        )

        builder.add_edge("route_to_crew", "generate_answer")
        builder.add_edge("generate_answer", "save_memory")
        builder.add_edge("save_memory", END)

        compile_kwargs = {}
        if checkpointer is not None:
            compile_kwargs["checkpointer"] = checkpointer

        return builder.compile(**compile_kwargs)

     
    # NODE: PLAN QUERY
     

    def _node_plan_query(self, state: GraphState) -> dict:

        try:
            history = self.memory_store.format_history(
                state["session_id"]
            )

            plan = self.rag.plan_query(
                state["question"],
                history
            )

        except Exception as exc:
            logger.warning("plan_query failed: %s", exc)
            plan = {
                "intent": "general",
                "candidate_id": None,
                "search_query": state["question"]
            }
            history = "No previous conversation."

        return {
            "history": history,
            "query_plan": plan,
            "tool_calls": [],
            "iterations": 0,
            "mode": "rag",
            "needs_investigation": False,
            "needs_tools": False,
            "error": None,
        }

     
    # NODE: RETRIEVE
     

    def _node_retrieve(self, state: GraphState) -> dict:

        plan = state.get("query_plan", {})

        search_query = plan.get(
            "search_query",
            state["question"]
        )

        candidate_id = plan.get("candidate_id")

        try:
            results = self.retriever.search(
                test_id=state["test_id"],
                query=search_query,
                top_k=8,
                candidate_id=candidate_id
            )

            evidence = self.rag.get_evidence(results)

        except Exception as exc:
            logger.warning("retrieve failed: %s", exc)
            results = []
            evidence = []

        return {
            "retrieval_results": results,
            "evidence": evidence,
        }

     
    # NODE: ASSESS SUFFICIENCY
     

    def _node_assess_sufficiency(self, state: GraphState) -> dict:
        """
        Use the LLM to decide whether the retrieved evidence is
        sufficient to answer the question, or whether more tool
        calls / a full crew investigation is warranted.

        Returns one of: "sufficient" | "needs_tools" | "needs_crew"
        encoded in state flags.
        """

        results = state.get("retrieval_results", [])
        question = state["question"]
        iterations = state.get("iterations", 0)

        # If we already exhausted tool iterations, just answer.
        if iterations >= self.MAX_ITERATIONS:
            return {
                "needs_tools": False,
                "needs_investigation": False,
            }

        # Quick path: no results at all → try tools first.
        if not results and iterations == 0:
            return {
                "needs_tools": True,
                "needs_investigation": False,
            }

        system_prompt = """
You are a routing assistant for a behavioral evidence RAG system.

Your only job is to classify whether the retrieved evidence is
sufficient to answer the user's question.

Return ONLY one of these exact strings (no explanation):
- sufficient
- needs_tools
- needs_crew

Use "needs_crew" ONLY for multi-candidate investigation questions
that require cross-candidate comparison, ranking, or a comprehensive
report. Example: "rank all candidates by risk" or "give me a full
investigation report".

Use "needs_tools" for targeted follow-up searches (single candidate
timeline, specific event type queries, etc.).

Use "sufficient" when the retrieved evidence directly addresses the
question.
"""

        evidence_text = self.rag.format_results(results)

        user_prompt = f"""
Question: {question}

Retrieved evidence ({len(results)} results):
{evidence_text[:2000]}
"""

        try:
            decision = self.rag.llm.invoke(
                system_prompt,
                user_prompt
            ).strip().lower()

        except Exception as exc:
            logger.warning("assess_sufficiency LLM failed: %s", exc)
            decision = "sufficient"

        if "needs_crew" in decision:
            return {
                "needs_tools": False,
                "needs_investigation": True,
            }

        if "needs_tools" in decision:
            return {
                "needs_tools": True,
                "needs_investigation": False,
            }

        return {
            "needs_tools": False,
            "needs_investigation": False,
        }

     
    # ROUTING: AFTER ASSESS
     

    def _route_after_assess(self, state: GraphState) -> str:

        if state.get("needs_investigation"):
            return "route_to_crew"

        if state.get("needs_tools"):
            return "use_tools"

        return "generate_answer"

     
    # NODE: USE TOOLS (ReAct loop body)
     

    def _node_use_tools(self, state: GraphState) -> dict:
        """
        One iteration of the ReAct tool loop.

        The LLM selects ONE tool to call based on the current
        state, the tool is executed, and the result is appended
        to tool_calls for the next assess_sufficiency pass.
        """

        test_id = state["test_id"]
        question = state["question"]
        results = state.get("retrieval_results", [])
        previous_calls = state.get("tool_calls", [])

        tool_descriptions = """
Available tools:
- search_events(query, candidate_id?)   — semantic+keyword search
- get_candidate_timeline(candidate_id) — all events for one candidate
- get_suspicious_events()              — events flagged suspicious
- get_event_detail(event_id)           — full detail of one event
- compare_candidates()                 — per-candidate aggregate stats
"""

        previous_text = ""
        if previous_calls:
            previous_text = "\n".join(
                f"- {c['tool']}({c['args']}) → {str(c['result'])[:300]}"
                for c in previous_calls[-3:]
            )
        else:
            previous_text = "None yet."

        system_prompt = """
You are a tool-selection assistant for a behavioral evidence system.

Select ONE tool to call next to gather more evidence.

Return ONLY valid JSON in this exact format:
{
  "tool": "<tool_name>",
  "args": { "<arg_name>": "<value>", ... }
}

Do not include any other text.
"""

        user_prompt = f"""
Question: {question}

Previous tool calls:
{previous_text}

{tool_descriptions}

Current evidence count: {len(results)} results retrieved so far.

Which single tool should be called next to best answer the question?
"""

        tool_result = {}
        tool_call_record = {}

        try:
            raw = self.rag.llm.invoke(system_prompt, user_prompt)

            parsed = self.rag.parse_json(
                raw,
                {
                    "tool": None,
                    "args": {}
                }
            )

            tool_name = parsed.get("tool", "")
            tool_args = parsed.get("args", {})

            if tool_name not in self._tools:
                raise ValueError(f"Unknown tool: {tool_name}")

            tool_fn = self._tools[tool_name]

            # Inject test_id where appropriate.
            if "test_id" in tool_fn.__code__.co_varnames:
                tool_args["test_id"] = test_id

            tool_result = tool_fn(**tool_args)

            tool_call_record = {
                "tool": tool_name,
                "args": tool_args,
                "result": tool_result,
            }

            # Merge tool results into retrieval_results if they look
            # like event lists (have event_id) - these get the full
            # "event card" rendering in format_results().
            #
            # Tool results that DON'T look like events (e.g.
            # compare_candidates()'s aggregate stats, or
            # get_event_detail()'s single dict) would otherwise be
            # silently dropped here and never reach generate_answer -
            # they're captured separately as tool_context instead, so
            # nothing a tool successfully returns is ever discarded.
            new_results = list(results)
            tool_context_entries = list(
                state.get("tool_context", [])
            )

            if isinstance(tool_result, list):

                had_event_shaped_item = False

                for item in tool_result:
                    if isinstance(item, dict) and "event_id" in item:
                        had_event_shaped_item = True
                        if not any(
                            r.get("event_id") == item["event_id"]
                            for r in new_results
                        ):
                            new_results.append(item)

                if not had_event_shaped_item and tool_result:
                    # e.g. compare_candidates()'s aggregate stat rows
                    tool_context_entries.append(
                        f"{tool_name}() result:\n{tool_result}"
                    )

            elif tool_result:
                # e.g. get_event_detail()'s single dict, or any scalar/non-list tool return value
                tool_context_entries.append(
                    f"{tool_name}() result:\n{tool_result}"
                )

            evidence = self.rag.get_evidence(new_results)

        except Exception as exc:
            logger.warning("use_tools failed: %s", exc)
            tool_call_record = {
                "tool": "error",
                "args": {},
                "result": str(exc),
            }
            new_results = results
            evidence = state.get("evidence", [])
            tool_context_entries = list(
                state.get("tool_context", [])
            )

        return {
            "retrieval_results": new_results,
            "evidence": evidence,
            "tool_calls": [tool_call_record],   # appended via operator.add
            "tool_context": tool_context_entries,
            "iterations": state.get("iterations", 0) + 1,
            "mode": "tools",
            "needs_tools": False,  # reset as assess will re-evaluate
        }

     
    # ROUTING: AFTER TOOLS
     

    def _route_after_tools(self, state: GraphState) -> str:

        if state.get("iterations", 0) >= self.MAX_ITERATIONS:
            return "generate_answer"

        return "assess_sufficiency"

     
    # NODE: ROUTE TO CREW
     

    def _node_route_to_crew(self, state: GraphState) -> dict:
        """
        Delegates to the CrewAI investigation crew.
        The crew answer is stored in state["answer"] and we skip
        the generate_answer LLM call (it just passes through).
        """

        try:
            crew_answer = self.investigation_crew.investigate(
                test_id=state["test_id"],
                question=state["question"]
            )

        except Exception as exc:
            logger.error("Crew investigation failed: %s", exc)
            crew_answer = (
                "The multi-agent investigation could not be "
                f"completed: {exc}. "
                "Please review the available events manually."
            )

        return {
            "answer": crew_answer,
            "mode": "crew",
        }

     
    # NODE: GENERATE ANSWER
     

    def _node_generate_answer(self, state: GraphState) -> dict:

        # If crew already set the answer, pass through.
        if state.get("mode") == "crew" and state.get("answer"):
            return {}

        results = state.get("retrieval_results", [])
        question = state["question"]
        history = state.get("history", "")
        tool_context = state.get("tool_context", [])

        try:
            answer = self.rag.generate_answer(
                question=question,
                history=history,
                results=results,
                tool_context=tool_context
            )

        except Exception as exc:
            logger.error("generate_answer failed: %s", exc)
            answer = (
                "An error occurred while generating the answer. "
                f"Detail: {exc}"
            )

        return {
            "answer": answer,
        }

     
    # NODE: SAVE MEMORY
     

    def _node_save_memory(self, state: GraphState) -> dict:

        session_id = state["session_id"]
        question = state["question"]
        answer = state.get("answer", "")

        try:
            self.memory_store.save_user_message(session_id, question)
            self.memory_store.save_assistant_message(session_id, answer)
        except Exception as exc:
            logger.warning("save_memory failed: %s", exc)

        return {}

     
    # PUBLIC: RUN
     

    def run(
        self,
        test_id: str,
        session_id: str,
        question: str
    ) -> dict:
        """
        Execute the LangGraph for one conversational turn.

        Returns a dict compatible with the existing /chat API
        response shape:
        {
            "answer": str,
            "mode": "rag" | "tools" | "crew",
            "query_plan": dict,
            "results": list,
            "evidence": list,
            "tool_calls": list,
        }
        """

        initial_state: GraphState = {
            "test_id": test_id,
            "session_id": session_id,
            "question": question,
            "history": "",
            "query_plan": {},
            "retrieval_results": [],
            "evidence": [],
            "answer": "",
            "mode": "rag",
            "needs_investigation": False,
            "needs_tools": False,
            "tool_calls": [],
            "tool_context": [],
            "iterations": 0,
            "error": None,
        }

        config = {"configurable": {"thread_id": session_id}}

        try:
            final_state = self._graph_with_memory.invoke(
                initial_state,
                config=config
            )

        except Exception as exc:
            logger.error("LangGraph execution failed: %s", exc)

            #fallback to direct RAG.
            try:
                self.memory_store.create_session(session_id, test_id)
                fallback = self.rag.chat(
                    test_id=test_id,
                    session_id=session_id,
                    question=question
                )
                fallback["mode"] = "rag"
                fallback["tool_calls"] = []
                return fallback
            except Exception as fallback_exc:
                return {
                    "answer": (
                        "An error occurred in the orchestrator. "
                        f"Detail: {exc}"
                    ),
                    "mode": "error",
                    "query_plan": {},
                    "results": [],
                    "evidence": [],
                    "tool_calls": [],
                }

        return {
            "answer":
                final_state.get("answer", "No answer generated."),
            "mode":
                final_state.get("mode", "rag"),
            "query_plan":
                final_state.get("query_plan", {}),
            "results":
                final_state.get("retrieval_results", []),
            "evidence":
                final_state.get("evidence", []),
            "tool_calls":
                final_state.get("tool_calls", []),
        }
