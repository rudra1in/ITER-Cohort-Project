# ============================================================
# FILE: src/agent/graph.py
# ============================================================

from __future__ import annotations

import json
from datetime import datetime, timezone
from typing import Any, Dict, List

from langgraph.graph import (
    END,
    START,
    StateGraph,
)

from .state import AudioAgentState

from .ollama_reasoner import (
    OllamaReasoner,
)

from ..audio.analyzer import (
    analyze_audio_chunk,
)

from ..rag.store import (
    AudioRAGStore,
)


# ============================================================
# GRAPH
# ============================================================

class AudioReActGraph:
    """
    LangGraph Audio ReAct Agent with student-scoped
    semantic RAG.

    Architecture:

        CURRENT OBSERVATION
                |
                v
        AUDIO ANALYZER
                |
                v
        EVENT + CONFIDENCE
                |
                v
        SEMANTIC SEARCH
                |
                v
        SAME STUDENT HISTORY
                |
                v
        OLLAMA REASONER
                |
          +-----+------+
          |            |
        LABEL        REVIEW
          |
          v
        STORE

    Low-confidence cases can additionally request REANALYZE.

    Important:

        Confidence is evidence.

        Historical observations are evidence.

        Agent decisions are NOT evidence.
    """

    def __init__(
        self,
        rag_store: AudioRAGStore,
        reasoner: OllamaReasoner,
        low_confidence_threshold: float = 0.60,
        high_confidence_threshold: float = 0.80,
        max_react_steps: int = 3,
        semantic_top_k: int = 5,
    ):

        self.rag = rag_store

        self.reasoner = reasoner

        self.low_confidence_threshold = (
            low_confidence_threshold
        )

        self.high_confidence_threshold = (
            high_confidence_threshold
        )

        self.max_react_steps = (
            max_react_steps
        )

        self.semantic_top_k = (
            semantic_top_k
        )

        # ----------------------------------------------------
        # BUILD LANGGRAPH
        # ----------------------------------------------------

        builder = StateGraph(
            AudioAgentState
        )

        builder.add_node(
            "retrieve",
            self.retrieve,
        )

        builder.add_node(
            "analyze",
            self.analyze,
        )

        builder.add_node(
            "semantic_search",
            self.semantic_search,
        )

        builder.add_node(
            "reason",
            self.reason,
        )

        builder.add_node(
            "reanalyze",
            self.reanalyze,
        )

        builder.add_node(
            "label",
            self.label,
        )

        builder.add_node(
            "store",
            self.store,
        )

        builder.add_node(
            "update_context",
            self.update_context,
        )

        builder.add_node(
            "next_chunk",
            self.next_chunk,
        )

        # ----------------------------------------------------
        # BASIC FLOW
        # ----------------------------------------------------

        builder.add_edge(
            START,
            "retrieve",
        )

        builder.add_edge(
            "retrieve",
            "analyze",
        )

        builder.add_edge(
            "analyze",
            "semantic_search",
        )

        builder.add_edge(
            "semantic_search",
            "reason",
        )

        # ----------------------------------------------------
        # REASON ROUTING
        # ----------------------------------------------------

        builder.add_conditional_edges(
            "reason",
            self.route_reason,
            {
                "REANALYZE": "reanalyze",
                "LABEL": "label",
                "REVIEW": "label",
                "END": END,
            },
        )

        builder.add_edge(
            "reanalyze",
            "semantic_search",
        )

        # ----------------------------------------------------
        # STORE
        # ----------------------------------------------------

        builder.add_edge(
            "label",
            "store",
        )

        builder.add_edge(
            "store",
            "update_context",
        )

        builder.add_edge(
            "update_context",
            "next_chunk",
        )

        # ----------------------------------------------------
        # NEXT CHUNK
        # ----------------------------------------------------

        builder.add_conditional_edges(
            "next_chunk",
            self.route_next,
            {
                "CONTINUE": "retrieve",
                "END": END,
            },
        )

        self.graph = (
            builder.compile()
        )

    # ========================================================
    # RETRIEVE CURRENT CHUNK
    # ========================================================

    def retrieve(
        self,
        state: AudioAgentState,
    ) -> Dict[str, Any]:

        position = int(
            state.get(
                "current_position",
                0,
            )
        )

        chunks = state.get(
            "chunks",
            [],
        )

        if position >= len(
            chunks
        ):

            return {
                "next_action": "END"
            }

        chunk = chunks[position]

        print()
        print(
            f"[LangGraph] "
            f"Processing chunk "
            f"{position + 1}/"
            f"{len(chunks)}"
        )

        print(
            f"[LangGraph] Chunk: "
            f"{chunk.get('chunk_id')}"
        )

        print(
            f"[LangGraph] Student: "
            f"{state.get('student_id')}"
        )

        return {
            "current_chunk": chunk,
            "processing_status": "ANALYZING",

            "react_steps": 0,

            "context_retrieved": False,

            "retrieved_context": [],

            "context_result_count": 0,

            "context_top_similarity": 0.0,

            "context_interpretation": "",

            "context_search_query": "",

            "reanalyzed": False,

            "next_action": "",

            "reasoning": "",

            "review_required": False,

            "assigned_label": "OTHER",
        }

    # ========================================================
    # ANALYZE
    # ========================================================

    def analyze(
        self,
        state: AudioAgentState,
    ) -> Dict[str, Any]:

        chunk = state[
            "current_chunk"
        ]

        print(
            "[Audio] Initial analysis..."
        )

        analysis = analyze_audio_chunk(
            chunk[
                "storage_path"
            ]
        )

        confidence = float(
            analysis.get(
                "confidence",
                0.0,
            )
        )

        event = str(
            analysis.get(
                "event",
                "OTHER",
            )
        )

        confidence_band = (
            self._confidence_band(
                confidence
            )
        )

        print(
            f"[Audio] Event: "
            f"{event}"
        )

        print(
            f"[Audio] Confidence: "
            f"{confidence:.3f}"
        )

        print(
            f"[Audio] Band: "
            f"{confidence_band}"
        )

        return {
            "current_analysis": analysis,

            "detected_event": event,

            "confidence_score": confidence,

            "confidence_band": (
                confidence_band
            ),

            "analysis_result": json.dumps(
                analysis,
                sort_keys=True,
            ),

            "processing_status": (
                "SEMANTIC_SEARCH"
            ),
        }

    # ========================================================
    # SEMANTIC SEARCH
    # ========================================================

    def semantic_search(
        self,
        state: AudioAgentState,
    ) -> Dict[str, Any]:

        student_id = str(
            state.get(
                "student_id",
                "unknown_student",
            )
        )

        chunk = state[
            "current_chunk"
        ]

        analysis = dict(
            state.get(
                "current_analysis",
                {},
            )
        )

        event = str(
            state.get(
                "detected_event",
                analysis.get(
                    "event",
                    "OTHER",
                ),
            )
        )

        confidence = float(
            state.get(
                "confidence_score",
                analysis.get(
                    "confidence",
                    0.0,
                ),
            )
        )

        chunk_id = str(
            chunk.get(
                "chunk_id",
                "",
            )
        )

        audio_file_id = str(
            state.get(
                "audio_file_id",
                "",
            )
        )

        print()
        print(
            "[RAG] Semantic search..."
        )

        print(
            f"[RAG] Student scope: "
            f"{student_id}"
        )

        print(
            f"[RAG] Current event: "
            f"{event}"
        )

        print(
            f"[RAG] Current confidence: "
            f"{confidence:.3f}"
        )

        try:

            context = (
                self.rag
                .retrieve_semantic_context(
                    student_id=student_id,
                    current_chunk_id=chunk_id,
                    current_audio_file_id=(
                        audio_file_id
                    ),
                    current_event=event,
                    current_confidence=(
                        confidence
                    ),
                    current_analysis=analysis,
                    top_k=(
                        self.semantic_top_k
                    ),
                )
            )

        except Exception as exc:

            print(
                "[RAG] Semantic retrieval "
                f"failed: {exc}"
            )

            context = []

        top_similarity = 0.0

        if context:

            similarities = [
                float(
                    item.get(
                        "similarity",
                        0.0,
                    )
                    or 0.0
                )
                for item in context
            ]

            if similarities:

                top_similarity = max(
                    similarities
                )

        print(
            f"[RAG] Retrieved "
            f"{len(context)} "
            f"historical observations."
        )

        for item in context:

            print(
                "  "
                f"{item.get('chunk_id')} | "
                f"{item.get('event')} | "
                f"confidence="
                f"{item.get('confidence')} | "
                f"similarity="
                f"{item.get('similarity')}"
            )

        if not context:

            print(
                "[RAG] No historical "
                "semantic evidence found."
            )

        return {
            "retrieved_context": context,

            "context_retrieved": True,

            "context_result_count": (
                len(context)
            ),

            "context_top_similarity": (
                top_similarity
            ),

            "context_search_query": (
                f"{event} "
                f"confidence={confidence:.3f}"
            ),

            "processing_status": (
                "REASONING"
            ),
        }

    # ========================================================
    # REASON
    # ========================================================

    def reason(
        self,
        state: AudioAgentState,
    ) -> Dict[str, Any]:

        current_step = int(
            state.get(
                "react_steps",
                0,
            )
        )

        if current_step >= (
            self.max_react_steps
        ):

            return {
                "next_action": "REVIEW",

                "reasoning": (
                    "Maximum ReAct reasoning "
                    "steps were reached."
                ),

                "review_required": True,
            }

        reasoning_step = (
            current_step + 1
        )

        analysis = state.get(
            "current_analysis",
            {},
        )

        confidence = float(
            analysis.get(
                "confidence",
                state.get(
                    "confidence_score",
                    0.0,
                ),
            )
        )

        detected_event = str(
            analysis.get(
                "event",
                state.get(
                    "detected_event",
                    "OTHER",
                ),
            )
        )

        context = state.get(
            "retrieved_context",
            [],
        )

        print()
        print(
            f"[ReAct] Reasoning step "
            f"{reasoning_step}/"
            f"{self.max_react_steps}"
        )

        print(
            f"[ReAct] Event: "
            f"{detected_event}"
        )

        print(
            f"[ReAct] Confidence: "
            f"{confidence:.3f}"
        )

        print(
            "[ReAct] Historical evidence: "
            f"{len(context)}"
        )

        try:

            decision = (
                self.reasoner.reason(
                    student_id=state.get(
                        "student_id"
                    ),
                    detected_event=(
                        detected_event
                    ),
                    confidence_score=(
                        confidence
                    ),
                    context=context,
                    previous_labels=(
                        state.get(
                            "previous_labels",
                            [],
                        )
                    ),
                    recent_events=(
                        state.get(
                            "recent_events",
                            [],
                        )
                    ),
                    reanalyzed=bool(
                        state.get(
                            "reanalyzed",
                            False,
                        )
                    ),
                    context_retrieved=bool(
                        state.get(
                            "context_retrieved",
                            False,
                        )
                    ),
                )
            )

        except Exception as exc:

            print(
                "[ERROR] Reasoning failed:"
            )

            print(
                exc
            )

            decision = {
                "action": "REVIEW",
                "reasoning": (
                    "Reasoning failed. "
                    "Manual review is required."
                ),
                "review_required": True,
            }

        action = str(
            decision.get(
                "action",
                "REVIEW",
            )
        ).upper().strip()

        reasoning = str(
            decision.get(
                "reasoning",
                "",
            )
        )

        review_required = bool(
            decision.get(
                "review_required",
                False,
            )
        )

        allowed_actions = {
            "REANALYZE",
            "LABEL",
            "REVIEW",
        }

        if action not in (
            allowed_actions
        ):

            action = "REVIEW"

            reasoning = (
                "Unsupported reasoning "
                "action. Manual review "
                "is required."
            )

            review_required = True

        # ----------------------------------------------------
        # Never allow endless re-analysis.
        # ----------------------------------------------------

        if (
            action == "REANALYZE"
            and state.get(
                "reanalyzed",
                False,
            )
        ):

            action = "REVIEW"

            reasoning = (
                "A second analysis has "
                "already been completed. "
                "The remaining uncertainty "
                "requires review."
            )

            review_required = True

        # ----------------------------------------------------
        # Final reasoning step cannot request another
        # re-analysis.
        # ----------------------------------------------------

        if (
            reasoning_step
            >= self.max_react_steps
            and action
            == "REANALYZE"
        ):

            action = "REVIEW"

            reasoning = (
                "The maximum reasoning "
                "budget was reached before "
                "a final decision could be "
                "established."
            )

            review_required = True

        print(
            f"[ReAct] Action: "
            f"{action}"
        )

        print(
            f"[ReAct] Reasoning: "
            f"{reasoning}"
        )

        return {
            "next_action": action,

            "reasoning": reasoning,

            "review_required": (
                review_required
            ),

            "react_steps": (
                reasoning_step
            ),

            "processing_status": (
                "REASONING"
            ),
        }

    # ========================================================
    # REANALYZE
    # ========================================================

    def reanalyze(
        self,
        state: AudioAgentState,
    ) -> Dict[str, Any]:

        print(
            "[ReAct] Running independent "
            "second-pass analysis..."
        )

        analysis = analyze_audio_chunk(
            state[
                "current_chunk"
            ][
                "storage_path"
            ]
        )

        confidence = float(
            analysis.get(
                "confidence",
                0.0,
            )
        )

        event = str(
            analysis.get(
                "event",
                "OTHER",
            )
        )

        print(
            f"[Audio] Re-analysis event: "
            f"{event}"
        )

        print(
            f"[Audio] Re-analysis confidence: "
            f"{confidence:.3f}"
        )

        return {
            "current_analysis": analysis,

            "detected_event": event,

            "confidence_score": confidence,

            "confidence_band": (
                self._confidence_band(
                    confidence
                )
            ),

            "analysis_result": json.dumps(
                analysis,
                sort_keys=True,
            ),

            "reanalyzed": True,

            "processing_status": (
                "SEMANTIC_SEARCH"
            ),
        }

    # ========================================================
    # LABEL
    # ========================================================

    def label(
        self,
        state: AudioAgentState,
    ) -> Dict[str, Any]:

        event = str(
            state.get(
                "detected_event",
                "OTHER",
            )
        )

        label_map = {
            "KEYBOARD": "KEYBOARD",
            "HUMAN_SPEECH": (
                "HUMAN_SPEECH"
            ),
            "MULTIPLE_VOICES": (
                "MULTIPLE_VOICES"
            ),
            "VEHICLE_NOISE": (
                "VEHICLE_NOISE"
            ),
            "ENVIRONMENTAL_NOISE": (
                "ENVIRONMENTAL_NOISE"
            ),
            "SILENCE": "SILENCE",
            "OTHER": "OTHER",
        }

        label = label_map.get(
            event,
            "OTHER",
        )

        review_required = bool(
            state.get(
                "review_required",
                False,
            )
        )

        print(
            f"[ReAct] Final label: "
            f"{label}"
        )

        if review_required:

            print(
                "[ReAct] Status: "
                "REVIEW_REQUIRED"
            )

        else:

            print(
                "[ReAct] Status: "
                "ACCEPTED"
            )

        return {
            "assigned_label": label,

            "processing_status": (
                "REVIEW_REQUIRED"
                if review_required
                else "LABELED"
            ),
        }

    # ========================================================
    # STORE
    # ========================================================

    def store(
        self,
        state: AudioAgentState,
    ) -> Dict[str, Any]:

        print(
            "[RAG] Storing final observation "
            "and decision..."
        )

        chunk = dict(
            state[
                "current_chunk"
            ]
        )

        student_id = str(
            state.get(
                "student_id",
                "unknown_student",
            )
        )

        audio_file_id = str(
            state[
                "audio_file_id"
            ]
        )

        chunk[
            "student_id"
        ] = student_id

        chunk[
            "audio_file_id"
        ] = audio_file_id

        review_required = bool(
            state.get(
                "review_required",
                False,
            )
        )

        chunk[
            "processing_status"
        ] = (
            "REVIEW_REQUIRED"
            if review_required
            else "COMPLETED"
        )

        analysis = dict(
            state.get(
                "current_analysis",
                {},
            )
        )

        # IMPORTANT:
        #
        # Store the actual detected event in the observation.
        #
        # Do NOT overwrite it with the agent's final label.
        #
        # This keeps observation != decision.

        analysis[
            "event"
        ] = state.get(
            "detected_event",
            analysis.get(
                "event",
                "OTHER",
            ),
        )

        analysis[
            "confidence"
        ] = float(
            state.get(
                "confidence_score",
                analysis.get(
                    "confidence",
                    0.0,
                ),
            )
        )

        # ----------------------------------------------------
        # Store actual observation
        # ----------------------------------------------------

        self.rag.upsert_chunk(
            chunk=chunk,
            analysis=analysis,
            student_id=student_id,
        )

        # ----------------------------------------------------
        # Build decision
        # ----------------------------------------------------

        decision = {
            "student_id": student_id,

            "audio_file_id": (
                audio_file_id
            ),

            "chunk_id": chunk[
                "chunk_id"
            ],

            "chunk_index": chunk[
                "chunk_index"
            ],

            "start_timestamp": chunk[
                "start_timestamp"
            ],

            "end_timestamp": chunk[
                "end_timestamp"
            ],

            "detected_event": state.get(
                "detected_event",
                "OTHER",
            ),

            "assigned_label": state.get(
                "assigned_label",
                "OTHER",
            ),

            "confidence_score": float(
                state.get(
                    "confidence_score",
                    0.0,
                )
            ),

            "confidence_band": state.get(
                "confidence_band",
                "LOW",
            ),

            "processing_status": chunk[
                "processing_status"
            ],

            "review_required": (
                review_required
            ),

            "reasoning": state.get(
                "reasoning",
                "",
            ),

            "context_used": bool(
                state.get(
                    "context_retrieved",
                    False,
                )
            ),

            "context_result_count": int(
                state.get(
                    "context_result_count",
                    0,
                )
            ),

            "context_top_similarity": float(
                state.get(
                    "context_top_similarity",
                    0.0,
                )
            ),

            "context_interpretation": (
                state.get(
                    "context_interpretation",
                    "",
                )
            ),

            "context_observations": (
                state.get(
                    "retrieved_context",
                    [],
                )
            ),

            "reanalyzed": bool(
                state.get(
                    "reanalyzed",
                    False,
                )
            ),

            "react_steps": int(
                state.get(
                    "react_steps",
                    0,
                )
            ),
        }

        # ----------------------------------------------------
        # Store decision separately.
        #
        # It will NOT be used by semantic search.
        # ----------------------------------------------------

        self.rag.store_decision(
            decision
        )

        print(
            "[RAG] Observation stored."
        )

        print(
            "[RAG] Decision stored separately."
        )

        return {
            "report_results": (
                state.get(
                    "report_results",
                    [],
                )
                + [decision]
            ),

            "processing_status": (
                chunk[
                    "processing_status"
                ]
            ),
        }

    # ========================================================
    # UPDATE CONTEXT
    # ========================================================

    def update_context(
        self,
        state: AudioAgentState,
    ) -> Dict[str, Any]:

        event = {
            "chunk_id": state[
                "current_chunk"
            ][
                "chunk_id"
            ],

            "start_timestamp": (
                state[
                    "current_chunk"
                ][
                    "start_timestamp"
                ]
            ),

            "end_timestamp": (
                state[
                    "current_chunk"
                ][
                    "end_timestamp"
                ]
            ),

            "event": state.get(
                "detected_event",
                "OTHER",
            ),

            "label": state.get(
                "assigned_label",
                "OTHER",
            ),

            "confidence": float(
                state.get(
                    "confidence_score",
                    0.0,
                )
            ),

            "review_required": bool(
                state.get(
                    "review_required",
                    False,
                )
            ),
        }

        history_entry = {
            "timestamp": (
                datetime.now(
                    timezone.utc
                ).isoformat()
            ),

            "student_id": state.get(
                "student_id"
            ),

            "chunk_id": state[
                "current_chunk"
            ][
                "chunk_id"
            ],

            "action": state.get(
                "next_action",
                "",
            ),

            "reasoning": state.get(
                "reasoning",
                "",
            ),

            "react_steps": state.get(
                "react_steps",
                0,
            ),

            "context_used": bool(
                state.get(
                    "context_retrieved",
                    False,
                )
            ),
        }

        return {
            "previous_labels": (
                state.get(
                    "previous_labels",
                    [],
                )
                + [
                    state.get(
                        "assigned_label",
                        "OTHER",
                    )
                ]
            )[-10:],

            "recent_events": (
                state.get(
                    "recent_events",
                    [],
                )
                + [event]
            )[-10:],

            "processing_history": (
                state.get(
                    "processing_history",
                    [],
                )
                + [history_entry]
            )[-50:],
        }

    # ========================================================
    # NEXT CHUNK
    # ========================================================

    def next_chunk(
        self,
        state: AudioAgentState,
    ) -> Dict[str, Any]:

        next_position = (
            int(
                state.get(
                    "current_position",
                    0,
                )
            )
            + 1
        )

        return {
            "current_position": (
                next_position
            ),

            "react_steps": 0,

            "context_retrieved": False,

            "retrieved_context": [],

            "context_result_count": 0,

            "context_top_similarity": 0.0,

            "context_interpretation": "",

            "context_search_query": "",

            "reanalyzed": False,

            "next_action": "",

            "reasoning": "",

            "review_required": False,

            "assigned_label": "OTHER",
        }

    # ========================================================
    # ROUTE REASON
    # ========================================================

    def route_reason(
        self,
        state: AudioAgentState,
    ) -> str:

        action = str(
            state.get(
                "next_action",
                "REVIEW",
            )
        ).upper().strip()

        if action == "REANALYZE":

            return "REANALYZE"

        if action == "LABEL":

            return "LABEL"

        if action == "REVIEW":

            return "REVIEW"

        return "REVIEW"

    # ========================================================
    # ROUTE NEXT
    # ========================================================

    def route_next(
        self,
        state: AudioAgentState,
    ) -> str:

        position = int(
            state.get(
                "current_position",
                0,
            )
        )

        chunks = state.get(
            "chunks",
            [],
        )

        if position < len(
            chunks
        ):

            return "CONTINUE"

        return "END"

    # ========================================================
    # RUN
    # ========================================================

    def run(
        self,
        audio_file_id: str,
        source_file: str,
        chunks: List[Dict[str, Any]],
        student_id: str = "student_default",
        precomputed_analyses: Dict[
            str,
            Dict[str, Any],
        ] | None = None,
    ) -> Dict[str, Any]:

        # ----------------------------------------------------
        # Attach student ID.
        # ----------------------------------------------------

        for chunk in chunks:

            chunk[
                "student_id"
            ] = student_id

            chunk[
                "audio_file_id"
            ] = audio_file_id

        # ----------------------------------------------------
        # Register chunk structure.
        # ----------------------------------------------------

        self.rag.register_chunks(
            chunks=chunks,
            audio_file_id=(
                audio_file_id
            ),
            student_id=student_id,
        )

        print()
        print(
            "======================================"
        )

        print(
            "[LangGraph] Starting Audio ReAct Agent"
        )

        print(
            "======================================"
        )

        print(
            f"[LangGraph] Student: "
            f"{student_id}"
        )

        print(
            f"[LangGraph] Audio: "
            f"{audio_file_id}"
        )

        print(
            f"[LangGraph] Chunks: "
            f"{len(chunks)}"
        )

        print(
            f"[LangGraph] Semantic top-k: "
            f"{self.semantic_top_k}"
        )

        print(
            f"[LangGraph] Max ReAct steps: "
            f"{self.max_react_steps}"
        )

        initial: AudioAgentState = {
            "student_id": student_id,

            "audio_file_id": (
                audio_file_id
            ),

            "source_file": (
                source_file
            ),

            "chunks": chunks,

            "current_position": 0,

            "previous_labels": [],

            "recent_events": [],

            "processing_history": [],

            "report_results": [],

            "react_steps": 0,

            "max_react_steps": (
                self.max_react_steps
            ),

            "review_required": False,

            "context_retrieved": False,

            "retrieved_context": [],

            "context_result_count": 0,

            "context_top_similarity": 0.0,

            "context_interpretation": "",

            "context_search_query": "",

            "reanalyzed": False,

            "next_action": "",

            "reasoning": "",

            "processing_status": (
                "STARTED"
            ),
        }

        # ----------------------------------------------------
        # Dynamic recursion limit.
        #
        # Prevents the previous 100-step failure on longer
        # recordings.
        # ----------------------------------------------------

        recursion_limit = max(
            200,
            len(chunks)
            * (
                12
                + (
                    self.max_react_steps
                    * 3
                )
            )
            + 50,
        )

        print(
            f"[LangGraph] Recursion limit: "
            f"{recursion_limit}"
        )

        final_state = (
            self.graph.invoke(
                initial,
                config={
                    "recursion_limit":
                        recursion_limit
                },
            )
        )

        print()
        print(
            "[LangGraph] Execution completed."
        )

        return dict(
            final_state
        )

    # ========================================================
    # CONFIDENCE BAND
    # ========================================================

    def _confidence_band(
        self,
        confidence: float,
    ) -> str:

        if (
            confidence
            >= self.high_confidence_threshold
        ):

            return "HIGH"

        if (
            confidence
            >= self.low_confidence_threshold
        ):

            return "MEDIUM"

        return "LOW"