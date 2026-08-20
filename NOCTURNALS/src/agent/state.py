# ============================================================
# FILE: src/agent/state.py
# ============================================================

from __future__ import annotations

from typing import Any, Dict, List, TypedDict


class AudioAgentState(TypedDict, total=False):
    """
    Shared LangGraph state for the local Audio ReAct Agent.

    The state deliberately separates:

        current observation
        historical semantic evidence
        agent decision
    """

    # ========================================================
    # SESSION / IDENTITY
    # ========================================================

    student_id: str

    audio_file_id: str

    source_file: str

    # ========================================================
    # CHUNKS
    # ========================================================

    chunks: List[Dict[str, Any]]

    current_position: int

    current_chunk: Dict[str, Any]

    # ========================================================
    # CURRENT AUDIO OBSERVATION
    # ========================================================

    current_analysis: Dict[str, Any]

    analysis_result: str

    detected_event: str

    confidence_score: float

    confidence_band: str

    # ========================================================
    # SEMANTIC RAG
    # ========================================================

    retrieved_context: List[
        Dict[str, Any]
    ]

    context_retrieved: bool

    context_search_query: str

    context_result_count: int

    context_top_similarity: float

    context_interpretation: str

    # ========================================================
    # REACT
    # ========================================================

    next_action: str

    reasoning: str

    react_steps: int

    max_react_steps: int

    reanalyzed: bool

    review_required: bool

    # ========================================================
    # LABEL
    # ========================================================

    assigned_label: str

    # ========================================================
    # SHORT-TERM MEMORY
    # ========================================================

    previous_labels: List[str]

    recent_events: List[
        Dict[str, Any]
    ]

    processing_history: List[
        Dict[str, Any]
    ]

    # ========================================================
    # OUTPUT
    # ========================================================

    report_results: List[
        Dict[str, Any]
    ]

    # ========================================================
    # PROCESSING
    # ========================================================

    processing_status: str