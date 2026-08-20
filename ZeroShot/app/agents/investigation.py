"""
CrewAI Investigation Crew
=========================

Three-pass investigation pipeline:
  1. RetrievalAgent   — searches behavioral database with tools
  2. EvidenceAgent    — organises and connects evidence (no hallucination)
  3. ReviewAgent      — produces a cautious, observable-behaviour summary
  4. SummaryAgent     — formats the final human-readable report

The LLM is wired as a CrewAI-native LLM, pointed at
whichever provider (Gemini API or local Ollama) is currently active on
the shared LocalLLM router. it refresh every time a crew is built, switching the
provider (e.g. via the Streamlit toggle) takes effect on the very next
investigation with no restart needed.
"""

import logging

from crewai import (
    Agent,
    Crew,
    Task,
    Process,
    LLM
)

from app.config import (
    LLM_MODEL,
    GEMINI_API_KEY,
    OLLAMA_MODEL,
    OLLAMA_BASE_URL
)

logger = logging.getLogger(__name__)


class InvestigationCrew:

    def __init__(
        self,
        database,
        retriever,
        llm_router=None
    ):

        self.database = database
        self.retriever = retriever
        self.llm_router = llm_router

     
    # BUILD LLM
     

    def _build_llm(self):
        """
        Return a CrewAI native LLM instance configured for whichever
        provider is currently active (via litellm's "gemini/<model>"
        or "ollama/<model>" provider prefix).
        """

        provider = (
            self.llm_router.provider
            if self.llm_router is not None
            else "gemini"
        )

        if provider == "ollama":

            model_name = OLLAMA_MODEL
            if not model_name.startswith("ollama/"):
                model_name = f"ollama/{model_name}"

            return LLM(
                model=model_name,
                base_url=OLLAMA_BASE_URL,
                temperature=0
            )

        model_name = LLM_MODEL
        if not model_name.startswith("gemini/"):
            model_name = f"gemini/{model_name}"

        return LLM(
            model=model_name,
            api_key=GEMINI_API_KEY,
            temperature=0
        )

     
    # BUILD CREW
     

    def build(
        self,
        test_id: str = ""
    ):

        from app.agents.tools import InvestigationTools

        tools = InvestigationTools(
            self.database,
            self.retriever
        )

        llm = self._build_llm()

        # Build CrewAI tool instances (may be None if crewai_tools
        # is not installed — agents will still work, just without tools)
        search_tool = tools.search_events_tool(test_id)
        candidate_tool = tools.candidate_events_tool(test_id)
        suspicious_tool = tools.suspicious_events_tool(test_id)
        compare_tool = tools.compare_candidates_tool(test_id)

        # Filter out None tools (in case crewai_tools not installed).
        retrieval_tools = [
            t for t in [
                search_tool,
                candidate_tool,
                suspicious_tool,
                compare_tool
            ]
            if t is not None
        ]

         
        # AGENT 1: RETRIEVAL
         

        retrieval_agent = Agent(

            role="Behavioral Retrieval Analyst",

            goal=(
                "Find the most relevant recorded behavioral events "
                "for the investigation using all available tools."
            ),

            backstory=(
                "You analyse structured behavioral evidence retrieved "
                "from an offline computer-vision system. You use search "
                "tools to gather relevant events and timelines before "
                "drawing any conclusions."
            ),

            tools=retrieval_tools,

            verbose=False,

            allow_delegation=False,

            llm=llm
        )

         
        # AGENT 2: EVIDENCE ORGANISER
         

        evidence_agent = Agent(

            role="Evidence Analyst",

            goal=(
                "Organise the retrieved evidence. Connect each event "
                "to: candidate, timestamps, duration, confidence, "
                "and evidence frame IDs."
            ),

            backstory=(
                "You are a forensic-style evidence organiser. "
                "You never invent information not present in the "
                "retrieved data and never make unsupported claims."
            ),

            verbose=False,

            allow_delegation=False,

            llm=llm
        )

         
        # AGENT 3: BEHAVIORAL REVIEW
         

        review_agent = Agent(

            role="Behavioral Review Analyst",

            goal=(
                "Produce a cautious review of the observable evidence. "
                "Clearly separate OBSERVATIONS from INTERPRETATIONS."
            ),

            backstory=(
                "You review behavioral evidence and distinguish what "
                "was objectively recorded from what might be inferred. "
                "You NEVER state that a candidate definitely cheated. "
                "You use phrases like 'flagged for review', "
                "'observable behavior was recorded', "
                "'potentially suspicious behavior observed'."
            ),

            verbose=False,

            allow_delegation=False,

            llm=llm
        )

         
        # AGENT 4: REPORT WRITER
         

        summary_agent = Agent(

            role="Investigation Report Writer",

            goal=(
                "Format the final investigation findings as a clear, "
                "structured report with section headers."
            ),

            backstory=(
                "You produce polished investigation summaries. "
                "Your reports always include: an overview, a per-candidate "
                "evidence table, flagged events, and a disclaimer stating "
                "that all findings are for human review only and no "
                "conclusions about academic dishonesty are made by the "
                "automated system."
            ),

            verbose=False,

            allow_delegation=False,

            llm=llm
        )

         
        # TASKS
         

        retrieval_task = Task(

            description=(
                """
                Test ID: {test_id}

                User question:
                {question}

                Search the behavioral database and retrieve the most
                relevant events. Use the search tools available to you.

                Return: candidate names, event types, timestamps,
                confidence values, and evidence frame IDs.
                """
            ),

            expected_output=(
                "A structured list of relevant behavioral events with "
                "candidate IDs, event types, timestamps, and evidence."
            ),

            agent=retrieval_agent
        )

        evidence_task = Task(

            description=(
                """
                Review the retrieved behavioral events from the previous
                step.

                For each relevant event, extract and organise:
                - candidate_id
                - event_type
                - start_time and end_time
                - duration
                - confidence score
                - evidence frame IDs
                - description

                Do not invent information that is not in the data.
                Do not infer guilt or intent.
                """
            ),

            expected_output=(
                "A concise, well-organised evidence table with all "
                "required fields for each event."
            ),

            agent=evidence_agent
        )

        review_task = Task(

            description=(
                """
                Based only on the evidence table from the previous step,
                answer the user's question.

                Guidelines:
                - Clearly label OBSERVED BEHAVIOR vs INTERPRETATION
                - NEVER state a candidate definitely cheated
                - Use phrases: "flagged for review", "potentially
                  suspicious", "observable behavior was recorded"
                - Include timestamps and duration when available
                - Note the number of evidence frames supporting each claim
                """
            ),

            expected_output=(
                "A concise, evidence-based behavioral review answer."
            ),

            agent=review_agent
        )

        summary_task = Task(

            description=(
                """
                Format the behavioral review as a final report with
                these sections:

                ## Overview
                Brief summary of the investigation scope.

                ## Behavioral Observations
                Per-candidate observed events, sorted by candidate.

                ## Flagged Events
                Events marked suspicious, if any.

                ## Disclaimer
                State clearly that this report is produced by an
                automated behavioral analysis system. No determination
                of academic dishonesty or cheating is made. All findings
                are for human review only.
                """
            ),

            expected_output=(
                "A structured investigation report in markdown format."
            ),

            agent=summary_agent
        )

         
        # CREW
         

        crew = Crew(

            agents=[
                retrieval_agent,
                evidence_agent,
                review_agent,
                summary_agent
            ],

            tasks=[
                retrieval_task,
                evidence_task,
                review_task,
                summary_task
            ],

            process=Process.sequential,

            verbose=False
        )

        return crew

     
    # INVESTIGATE
     

    def investigate(
        self,
        test_id: str,
        question: str
    ) -> str:

        try:

            crew = self.build(test_id=test_id)

            result = crew.kickoff(
                inputs={
                    "test_id": test_id,
                    "question": question
                }
            )

            return str(result)

        except Exception as exc:

            logger.error(
                "InvestigationCrew.investigate failed: %s",
                exc
            )

            return (
                f"The multi-agent investigation could not be completed. "
                f"Error: {exc}. "
                f"Please review the available events manually."
            )