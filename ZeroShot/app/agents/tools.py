"""
Investigation tools for both:
  - LangGraph ReAct tool loop (called as plain Python functions)
  - CrewAI agents (wrapped as crewai.tools.BaseTool instances)
Each tool is conservative: it only surfaces observable behavioral
evidence and never makes guilt determinations.
"""

import json
from typing import Optional, Type
from pydantic import BaseModel, Field

try:
    from crewai.tools import BaseTool
    CREWAI_TOOLS_AVAILABLE = True
except ImportError:
    try:
        from crewai_tools import BaseTool
        CREWAI_TOOLS_AVAILABLE = True
    except ImportError:
        CREWAI_TOOLS_AVAILABLE = False
        BaseTool = object


 
# PYDANTIC SCHEMAS (for CrewAI tool validation)
 

class SearchInput(BaseModel):
    query: str = Field(
        ...,
        description="The behavioral concept or name to search for"
    )
    candidate_id: Optional[str] = Field(
        None,
        description="Limit results to a specific candidate (optional)"
    )


class CandidateInput(BaseModel):
    candidate_id: str = Field(
        ...,
        description="The candidate identifier to retrieve events for"
    )


class EventInput(BaseModel):
    event_id: str = Field(
        ...,
        description="The unique event ID to retrieve full detail for"
    )


class TestOnlyInput(BaseModel):
    pass   # test_id is injected at runtime


 
# TOOL FACTORY
 

class InvestigationTools:

    def __init__(
        self,
        database,
        retriever
    ):

        self.database = database
        self.retriever = retriever

     
    # PLAIN PYTHON HELPERS (used by LangGraph directly)
     

    def search_events(
        self,
        test_id: str,
        query: str,
        candidate_id: str = None,
        top_k: int = 8
    ):
        """Hybrid semantic + keyword retrieval of behavioral events."""

        return self.retriever.search(
            test_id=test_id,
            query=query,
            top_k=top_k,
            candidate_id=candidate_id
        )

    def candidate_events(
        self,
        test_id: str,
        candidate_id: str
    ):
        """All behavioral events for one candidate sorted by time."""

        return self.database.get_candidate_timeline(
            test_id,
            candidate_id
        )

    def suspicious_events(
        self,
        test_id: str
    ):
        """All events flagged as suspicious."""

        return self.database.get_suspicious_events(test_id)

    def event_detail(
        self,
        event_id: str
    ):
        """Full record for one event including evidence frame IDs."""

        return self.database.get_event(event_id)

    def compare_candidates(
        self,
        test_id: str
    ):
        """Per-candidate, per-event-type aggregate statistics."""

        return self.database.get_test_statistics(test_id)

     
    # CREWAI TOOL WRAPPERS
     

    def search_events_tool(self, test_id: str = ""):

        if not CREWAI_TOOLS_AVAILABLE:
            return None

        db = self.database
        retriever = self.retriever
        _test_id = test_id

        class SearchEventsTool(BaseTool):

            name: str = "search_behavioral_events"

            description: str = (
                "Search the behavioral event database using a natural "
                "language query. Returns the most relevant events with "
                "candidate IDs, timestamps, event types, and evidence "
                "frame IDs. Use this to find specific behavior patterns."
            )

            args_schema: Type[BaseModel] = SearchInput

            def _run(
                self,
                query: str,
                candidate_id: Optional[str] = None
            ) -> str:

                results = retriever.search(
                    test_id=_test_id,
                    query=query,
                    top_k=8,
                    candidate_id=candidate_id
                )

                if not results:
                    return "No behavioral events found for this query."

                lines = []
                for r in results[:6]:
                    lines.append(
                        f"[{r.get('event_type')}] "
                        f"Candidate: {r.get('candidate_id')} | "
                        f"{r.get('start_time')} → {r.get('end_time')} "
                        f"({r.get('duration')}s) | "
                        f"conf={r.get('confidence')} | "
                        f"desc: {r.get('description','')[:120]}"
                    )

                return "\n".join(lines)

        return SearchEventsTool()

    def candidate_events_tool(self, test_id: str = ""):

        if not CREWAI_TOOLS_AVAILABLE:
            return None

        db = self.database
        _test_id = test_id

        class CandidateEventsTool(BaseTool):

            name: str = "get_candidate_events"

            description: str = (
                "Retrieve ALL behavioral events for a specific candidate "
                "in chronological order. Use this when you need a complete "
                "timeline for one person."
            )

            args_schema: Type[BaseModel] = CandidateInput

            def _run(self, candidate_id: str) -> str:

                events = db.get_candidate_timeline(
                    _test_id,
                    candidate_id
                )

                if not events:
                    return (
                        f"No events found for candidate "
                        f"{candidate_id}."
                    )

                lines = [
                    f"Timeline for {candidate_id} "
                    f"({len(events)} events):"
                ]

                for e in events:
                    flag = (
                        "⚑ FLAGGED"
                        if e.get("is_suspicious")
                        else ""
                    )
                    lines.append(
                        f"  {e.get('start_time')} "
                        f"[{e.get('event_type')}] "
                        f"{e.get('duration')}s "
                        f"conf={e.get('confidence')} "
                        f"{flag}"
                    )

                return "\n".join(lines)

        return CandidateEventsTool()

    def suspicious_events_tool(self, test_id: str = ""):

        if not CREWAI_TOOLS_AVAILABLE:
            return None

        db = self.database
        _test_id = test_id

        class SuspiciousEventsTool(BaseTool):

            name: str = "get_suspicious_events"

            description: str = (
                "Retrieve all behavioral events that have been flagged "
                "as suspicious by the clustering algorithm. Use this "
                "for overview and ranking questions."
            )

            args_schema: Type[BaseModel] = TestOnlyInput

            def _run(self) -> str:

                events = db.get_suspicious_events(_test_id)

                if not events:
                    return (
                        "No events have been flagged as suspicious yet. "
                        "Run clustering first via POST /tests/{id}/cluster."
                    )

                # Group by candidate.
                by_candidate = {}
                for e in events:
                    cid = e.get("candidate_id", "unknown")
                    by_candidate.setdefault(cid, []).append(e)

                lines = [
                    f"{len(events)} suspicious event(s) across "
                    f"{len(by_candidate)} candidate(s):\n"
                ]

                for cid, evts in sorted(by_candidate.items()):
                    lines.append(f"  {cid}: {len(evts)} event(s)")
                    for e in evts[:4]:
                        lines.append(
                            f"    [{e.get('event_type')}] "
                            f"{e.get('start_time')} "
                            f"({e.get('duration')}s)"
                        )

                return "\n".join(lines)

        return SuspiciousEventsTool()

    def compare_candidates_tool(self, test_id: str = ""):

        if not CREWAI_TOOLS_AVAILABLE:
            return None

        db = self.database
        _test_id = test_id

        class CompareCandidatesTool(BaseTool):

            name: str = "compare_candidates"

            description: str = (
                "Return per-candidate behavioral aggregate statistics "
                "to compare candidates across event types, durations, "
                "and suspicious event counts."
            )

            args_schema: Type[BaseModel] = TestOnlyInput

            def _run(self) -> str:

                stats = db.get_test_statistics(_test_id)

                if not stats:
                    return (
                        "No behavioral statistics available. "
                        "Run analysis and clustering first."
                    )

                # Group by candidate.
                by_candidate = {}
                for row in stats:
                    cid = row["candidate_id"]
                    by_candidate.setdefault(cid, []).append(row)

                lines = ["Candidate behavioral summary:\n"]

                for cid in sorted(by_candidate.keys()):
                    rows = by_candidate[cid]
                    total_events = sum(r["count"] for r in rows)
                    total_suspicious = sum(
                        r["suspicious_count"] for r in rows
                    )
                    total_duration = sum(
                        r["total_duration"] or 0 for r in rows
                    )

                    lines.append(
                        f"  {cid}: "
                        f"{total_events} event(s), "
                        f"{total_suspicious} suspicious, "
                        f"{total_duration:.1f}s total flagged duration"
                    )

                    for r in rows:
                        lines.append(
                            f"    [{r['event_type']}]: "
                            f"{r['count']} event(s), "
                            f"{r['total_duration'] or 0:.1f}s"
                        )

                return "\n".join(lines)

        return CompareCandidatesTool()