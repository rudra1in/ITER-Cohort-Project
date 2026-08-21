from __future__ import annotations

from typing import Any, TypedDict


class DSAAgentState(TypedDict, total=False):

    # ==============================
    # Request identity
    # ==============================

    user_id: str
    thread_id: str

    # ==============================
    # Problem
    # ==============================

    problem_id: str
    problem: dict[str, Any]

    # ==============================
    # Student submission
    # ==============================

    code: str
    language: str

    # ==============================
    # User request
    # ==============================

    request_type: str
    hint_level: int

    # ==============================
    # Code analysis
    # ==============================

    syntax_result: dict[str, Any]
    static_analysis: dict[str, Any]

    has_syntax_error: bool

    # ==============================
    # Execution
    # ==============================

    execution_result: dict[str, Any]

    solved: bool
    has_runtime_error: bool
    has_wrong_answer: bool
    timed_out: bool

    # ==============================
    # Student memory
    # ==============================

    student_history: list[dict[str, Any]]
    recurring_errors: list[dict[str, Any]]
    skill_profile: dict[str, Any]

    # ==============================
    # RAG
    # ==============================

    retrieval_query: str
    vector_results: list[dict[str, Any]]
    keyword_results: list[dict[str, Any]]
    hybrid_results: list[dict[str, Any]]
    reranked_results: list[dict[str, Any]]
    retrieved_context: str

    # ==============================
    # Agent decisions
    # ==============================

    next_action: str
    iteration: int

    # ==============================
    # LLM
    # ==============================

    selected_model: str
    coach_response: dict[str, Any]

    # ==============================
    # Observability
    # ==============================

    token_usage: dict[str, int]
    latency_ms: int
    trace: list[dict[str, Any]]

    # ==============================
    # Errors
    # ==============================

    errors: list[str]