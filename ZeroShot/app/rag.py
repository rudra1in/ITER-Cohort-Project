import json
import re

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser


class RAGService:

    def __init__(
        self,
        database,
        retriever,
        memory,
        llm
    ):

        self.database = database
        self.retriever = retriever
        self.memory = memory
        self.llm = llm

        chat_model = getattr(llm, "llm", llm)

        
        # LANGCHAIN FOR QUERY PLANNING
        
        planner_prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a query planner for a behavioral analysis RAG system.
            You do NOT decide whether someone cheated.
            Your job is only to convert the user's question into a retrieval plan.
            Return ONLY valid JSON.
            Schema:
            {{
            "intent": "who|when|what|evidence|compare|general", "candidate_id": null, "search_query": "..." 
            }}

            Rules:
            - Preserve candidate names if explicitly mentioned.
            - Resolve pronouns using conversation history when possible.
            - Do not invent candidate names.
            - search_query should contain the important behavioral concepts and candidate names.
            """),
                        ("human", """Conversation history:
                        {history}

Current question:
{question}
""")
        ])

        self.planner_chain = planner_prompt | chat_model | JsonOutputParser()

        
        # LANGCHAIN  FOR ANSWER GENERATION
        
        answer_prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a careful assistant for a post-test behavioral analysis system.

CRITICAL RULES:
1. You MUST NEVER state that a person definitely cheated.
2. You may use the word "cheating" as a conclusion.
3. Only describe OBSERVABLE EVIDENCE contained in the retrieved records.

BAD (forbidden):
"RAM cheated during the test."
"AJCKEY was caught cheating."

GOOD (required):
"RAM was flagged for behavioral review based on repeated side-oriented head movement recorded across multiple frames."
"The system detected a mobile phone visible in AJCKEY's frames during the time window 10:23:05 → 10:24:12."

Required phrasing:
- "was flagged for review"
- "observable behavior was recorded"
- "the system detected"
- "the evidence indicates"
- "potentially suspicious behavior"
- "recorded for human review"

If the evidence is insufficient to answer, say so clearly.
When evidence images are available, mention their evidence frame IDs.
Give timestamps when available.
Keep answers concise.
"""),
            ("human", """Conversation history:
{history}

User question:
{question}

Retrieved evidence:
{evidence_text}
""")
        ])

        self.answer_chain = answer_prompt | chat_model | StrOutputParser()

    # CHAT  (full pipeline i,e frm plan → retrieve → answer to save )
    
    def chat(
        self,
        test_id,
        session_id,
        question
    ):

        # MEMORY

        history = (
            self.memory.format_history(
                session_id
            )
        )

        # QUERY PLANNING

        plan = (
            self.plan_query(
                question,
                history
            )
        )

        candidate_id = (
            plan.get(
                "candidate_id"
            )
        )

        search_query = (
            plan.get(
                "search_query",
                question
            )
        )

        # RETRIEVAL

        results = (
            self.retriever.search(
                test_id=test_id,
                query=search_query,
                top_k=8,
                candidate_id=candidate_id
            )
        )

        # ANSWER
    
        answer = (
            self.generate_answer(
                question=question,
                history=history,
                results=results
            )
        )

        # SAVE MEMORY

        self.memory.save_user_message(
            session_id,
            question
        )

        self.memory.save_assistant_message(
            session_id,
            answer
        )

        return {

            "answer":
                answer,

            "query_plan":
                plan,

            "results":
                results,

            "evidence":
                self.get_evidence(
                    results
                )
        }

    # RETRIEVE QUESTION (used by orchestrator to fetch evidence for crew answers)

    def retrieve_question(
        self,
        test_id,
        question
    ):

        results = (
            self.retriever.search(
                test_id=test_id,
                query=question,
                top_k=8
            )
        )

        return {

            "results":
                results,

            "evidence":
                self.get_evidence(
                    results
                )
        }
    # RETRIEVE FOR CANDIDATE (used by LangGraph as in candidate timeline tool)

    def retrieve_for_candidate(
        self,
        test_id,
        candidate_id,
        query=None
    ):

        events = (
            self.database.get_candidate_timeline(
                test_id,
                candidate_id
            )
        )

        return {
            "candidate_id": candidate_id,
            "events": events,
            "count": len(events)
        }

    # QUERY PLANNER ( standalone method for LangGraph nodes)

    def plan_query(
        self,
        question,
        history
    ):

        try:
            plan = self.planner_chain.invoke({
                "history": history,
                "question": question
            })
            if isinstance(plan, dict):
                return plan
            return self.parse_json(
                str(plan),
                {
                    "intent": "general",
                    "candidate_id": None,
                    "search_query": question
                }
            )
        except Exception:
            try:
                chat_model = getattr(self.llm, "llm", self.llm)
                messages = [
                    {"role": "system", "content": "You are a query planner. Return ONLY valid JSON schema."},
                    {"role": "user", "content": f"Generate search query JSON for: '{question}' with history: '{history}'"}
                ]
                raw_response = chat_model.invoke(messages)
                return self.parse_json(
                    raw_response.content,
                    {
                        "intent": "general",
                        "candidate_id": None,
                        "search_query": question
                    }
                )
            except Exception:
                return {
                    "intent": "general",
                    "candidate_id": None,
                    "search_query": question
                }

    # ANSWER GENERATOR( as in standalone method for LangGraph nodes)

    def generate_answer(
        self,
        question,
        history,
        results,
        tool_context=None
    ):

        evidence_text = (
            self.format_results(
                results
            )
        )

        if tool_context:
            evidence_text += (
                "\n\nADDITIONAL TOOL RESULTS "
                "(not individual events, but real data "
                "retrieved during this investigation - "
                "use them too):\n"
                + "\n\n".join(tool_context)
            )

        try:
            return self.answer_chain.invoke({
                "history": history,
                "question": question,
                "evidence_text": evidence_text
            })
        except Exception as error:
            chat_model = getattr(self.llm, "llm", self.llm)
            system_prompt = """
You are a careful assistant for a post-test behavioral analysis system. CRITICAL RULE: You MUST NEVER state that a person definitely cheated. Only describe OBSERVABLE EVIDENCE.
"""
            user_prompt = f"History: {history}\nQuestion: {question}\nEvidence: {evidence_text}"
            try:
                response = chat_model.invoke([
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ])
                return response.content
            except Exception:
                return f"Error generating answer: {error}"

    # FORMAT RESULTS

    @staticmethod
    def format_results(
        results
    ):

        if not results:

            return (
                "No relevant behavioral "
                "events were retrieved."
            )

        chunks = []

        for index, item in enumerate(
            results,
            start=1
        ):

            evidence = item.get(
                "evidence_json",
                "[]"
            )

            chunks.append(
                f"""
RESULT {index}

Event ID:
{item.get("event_id")}

Candidate:
{item.get("candidate_id")}

Event:
{item.get("event_type")}

Start:
{item.get("start_time")}

End:
{item.get("end_time")}

Duration:
{item.get("duration")}s

Confidence:
{item.get("confidence")}

Cluster:
{item.get("cluster_label", "not clustered")}

Suspicious:
{bool(item.get("is_suspicious"))}

Description:
{item.get("description")}

Evidence Frames:
{evidence}

Retrieval Score:
{item.get("hybrid_score", 0)}
"""
            )

        return "\n".join(
            chunks
        )
    
    # EVIDENCE

    def get_evidence(
        self,
        results
    ):

        evidence = []

        seen_frame_ids = set()

        for result in results:

            raw = result.get(
                "evidence_json",
                "[]"
            )

            try:

                frames = json.loads(
                    raw
                )

            except Exception:

                frames = []

            for frame_id in frames:

                if frame_id in seen_frame_ids:
                    continue

                seen_frame_ids.add(frame_id)

                frame = (
                    self.get_frame(
                        frame_id
                    )
                )

                if frame:

                    evidence.append(
                        {
                            "event_id":
                                result[
                                    "event_id"
                                ],

                            "frame_id":
                                frame_id,

                            "image_path":
                                frame[
                                    "image_path"
                                ],

                            "timestamp":
                                frame[
                                    "timestamp"
                                ],

                            "candidate_id":
                                frame[
                                    "candidate_id"
                                ],

                            "event_type":
                                result.get(
                                    "event_type"
                                )
                        }
                    )

        return evidence

    # GET FRAME

    def get_frame(
        self,
        frame_id
    ):

        connection = (
            self.database.connect()
        )

        row = connection.execute(
            """
            SELECT *
            FROM frames
            WHERE frame_id = ?
            """,
            (
                frame_id,
            )
        ).fetchone()

        connection.close()

        if row is None:

            return None

        return dict(row)

    # JSON PARSER

    @staticmethod
    def parse_json(
        raw,
        fallback
    ):
        """
        fallback: the exact value to return if `raw` can't be parsed
        as JSON either directly or via best-effort extraction. Callers
        own their own fallback shape - this method has no opinion on
        what a "sensible default" looks like for a given call site.
        """

        try:

            return json.loads(
                raw
            )

        except Exception:

            pass
        match = re.search(
            r"\{.*\}",
            raw,
            re.DOTALL
        )

        if match:

            try:

                return json.loads(
                    match.group(0)
                )

            except Exception:

                pass

        return fallback