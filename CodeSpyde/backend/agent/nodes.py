from __future__ import annotations

from typing import Any

from agent.state import DSAAgentState


# ============================================================
# TRACE HELPER
# ============================================================

def _add_trace(
    state: DSAAgentState,
    event: dict[str, Any],
) -> list[dict[str, Any]]:
    """
    Append an event to the existing agent trace.

    We do this explicitly because TypedDict state does not
    automatically append lists between LangGraph nodes.
    """

    return [
        *state.get("trace", []),
        event,
    ]


# ============================================================
# 1. LOAD PROBLEM
# ============================================================

def load_problem_node(
    state: DSAAgentState,
) -> dict[str, Any]:
    """
    Load the requested DSA problem from the existing
    problem registry.

    We reuse routes.problems.PROBLEMS because that is
    what the current application already uses.
    """

    from routes.problems import PROBLEMS

    problem_id = state.get(
        "problem_id"
    )

    if not problem_id:
        raise ValueError(
            "problem_id is required."
        )

    problem = None

    for item in PROBLEMS:

        if item.get("id") == problem_id:

            problem = item
            break

    if problem is None:

        raise ValueError(
            f"Problem not found: {problem_id}"
        )

    return {

        "problem": problem,

        "trace": _add_trace(
            state,
            {
                "node": "load_problem",
                "status": "completed",
                "problem_id": problem_id,
            },
        ),
    }


# ============================================================
# 2. STUDENT MEMORY
# ============================================================

def memory_node(
    state: DSAAgentState,
) -> dict[str, Any]:
    """
    Load the student's previous attempts and recurring
    mistakes.

    Uses the existing student_history service.
    """

    from services.student_history import (
        get_student_history,
        get_recurring_errors,
    )

    user_id = state.get(
        "user_id"
    )

    problem_id = state.get(
        "problem_id"
    )

    if not user_id:
        user_id = "anonymous"

    # --------------------------------------------------------
    # Previous attempts for this problem
    # --------------------------------------------------------

    history = get_student_history(
        user_id=user_id,

        problem_id=problem_id,

        limit=10,
    )

    # --------------------------------------------------------
    # Recurring mistakes across problems
    # --------------------------------------------------------

    recurring_errors = (
        get_recurring_errors(
            user_id=user_id,
            limit=10,
        )
    )

    return {

        "student_history": (
            history or []
        ),

        "recurring_errors": (
            recurring_errors or []
        ),

        "trace": _add_trace(
            state,
            {
                "node": "student_memory",

                "status": "completed",

                "history_count": len(
                    history or []
                ),

                "recurring_error_count": len(
                    recurring_errors or []
                ),
            },
        ),
    }


# ============================================================
# 3. CODE ANALYSIS
# ============================================================

def analyze_code_node(
    state: DSAAgentState,
) -> dict[str, Any]:
    """
    Run the existing static code analyzer.

    Important:
    - We do NOT execute code here.
    - Syntax errors are handled before execution.
    """

    from services.code_analyzer import (
        analyze_code,
    )

    code = state.get(
        "code",
        "",
    )

    language = state.get(
        "language",
        "python",
    )

    result = analyze_code(
        code=code,

        language=language,
    )

    valid = result.get(
        "valid",
        True,
    )

    has_syntax_error = not valid

    update: dict[str, Any] = {

        "syntax_result": result,

        "static_analysis": result,

        "has_syntax_error": (
            has_syntax_error
        ),
    }

    # --------------------------------------------------------
    # If syntax is invalid, create a standardized
    # execution result so the rest of the application
    # can still process/save the attempt.
    # --------------------------------------------------------

    if has_syntax_error:

        issues = result.get(
            "issues",
            [],
        )

        first_issue = (
            issues[0]
            if issues
            else None
        )

        error_message = (
            first_issue.get(
                "message",
                "Syntax error.",
            )
            if isinstance(
                first_issue,
                dict,
            )
            else "Syntax error."
        )

        error_line = (
            first_issue.get(
                "line"
            )
            if isinstance(
                first_issue,
                dict,
            )
            else None
        )

        update[
            "execution_result"
        ] = {

            "status": "syntax_error",

            "stdout": "",

            "stderr": error_message,

            "runtime_ms": 0,

            "error_type": (
                "SyntaxError"
            ),

            "error_line": error_line,

            "test_results": [],
        }

        update[
            "has_runtime_error"
        ] = False

        update[
            "has_wrong_answer"
        ] = False

        update[
            "timed_out"
        ] = False

        update[
            "solved"
        ] = False

    update["trace"] = _add_trace(
        state,
        {
            "node": "code_analysis",

            "status": "completed",

            "valid": valid,

            "has_syntax_error": (
                has_syntax_error
            ),
        },
    )

    return update


# ============================================================
# 4. EXECUTE CODE
# ============================================================

def execute_code_node(
    state: DSAAgentState,
) -> dict[str, Any]:
    """
    Execute the student's Python code using the EXISTING
    code executor.

    We preserve the exact execution functions already
    used by routes/coach.py.
    """

    from services.code_executor import (
        execute_python,
        execute_python_with_tests,
    )

    from config import (
        CODE_EXECUTION_TIMEOUT,
    )

    problem = state.get(
        "problem",
        {},
    )

    code = state.get(
        "code",
        "",
    )

    # --------------------------------------------------------
    # Test cases
    # --------------------------------------------------------

    test_cases = problem.get(
        "test_cases",
        [],
    )

    # --------------------------------------------------------
    # Execute against test cases
    # --------------------------------------------------------

    if test_cases:

        execution_result = (
            execute_python_with_tests(

                code=code,

                test_cases=test_cases,

                timeout=(
                    CODE_EXECUTION_TIMEOUT
                ),
            )
        )

    # --------------------------------------------------------
    # Execute without test cases
    # --------------------------------------------------------

    else:

        execution_result = execute_python(

            code=code,

            timeout=(
                CODE_EXECUTION_TIMEOUT
            ),
        )

    # --------------------------------------------------------
    # Normalize execution status
    # --------------------------------------------------------

    status = str(
        execution_result.get(
            "status",
            "unknown",
        )
    ).lower()

    solved = status in {
        "accepted",
        "success",
        "passed",
    }

    has_runtime_error = status in {
        "runtime_error",
        "runtime error",
        "executor_error",
        "executor error",
    }

    timed_out = status in {
        "timeout",
        "timed_out",
        "time_limit_exceeded",
    }

    has_wrong_answer = status in {
        "wrong_answer",
        "wrong answer",
        "failed",
    }

    return {

        "execution_result": (
            execution_result
        ),

        "solved": solved,

        "has_runtime_error": (
            has_runtime_error
        ),

        "has_wrong_answer": (
            has_wrong_answer
        ),

        "timed_out": timed_out,

        "trace": _add_trace(
            state,
            {
                "node": "code_execution",

                "status": "completed",

                "execution_status": status,

                "solved": solved,
            },
        ),
    }


# ============================================================
# 5. RUN EXISTING RAG
# ============================================================

def rag_node(
    state: DSAAgentState,
) -> dict[str, Any]:
    """
    Run the EXISTING RAG pipeline.

    The existing pipeline already performs:

        DSA query construction
            ↓
        metadata-aware retrieval
            ↓
        hybrid search
            ↓
        RRF/fusion
            ↓
        cross-encoder reranking
            ↓
        context building
            ↓
        coach prompt construction

    Therefore LangGraph does NOT implement another
    retriever or reranker.
    """

    from rag.pipeline import (
        run_coach_rag,
    )

    rag_data = run_coach_rag(

        problem=state.get(
            "problem",
            {},
        ),

        code=state.get(
            "code",
            "",
        ),

        execution_result=state.get(
            "execution_result",
            {},
        ),

        syntax_result=state.get(
            "syntax_result",
            {},
        ),

        student_history=state.get(
            "student_history",
            [],
        ),

        recurring_errors=state.get(
            "recurring_errors",
            [],
        ),

        request_type=state.get(
            "request_type",
            "debug",
        ),

        hint_level=state.get(
            "hint_level",
            1,
        ),
    )

    # --------------------------------------------------------
    # Extract final retrieval results
    # --------------------------------------------------------

    results = rag_data.get(
        "retrieved_results",
        [],
    )

    # --------------------------------------------------------
    # Extract context
    # --------------------------------------------------------

    context_data = rag_data.get(
        "context",
        {},
    )

    if not isinstance(
        context_data,
        dict,
    ):

        context_data = {}

    retrieved_context = (
        context_data.get(
            "context",
            "",
        )
    )

    # --------------------------------------------------------
    # Final prompt generated by existing RAG pipeline
    # --------------------------------------------------------

    prompt = rag_data.get(
        "prompt",
        "",
    )

    # --------------------------------------------------------
    # Retrieval query
    # --------------------------------------------------------

    retrieval_query = rag_data.get(
        "query",
        "",
    )

    return {

        "retrieval_query": (
            retrieval_query
        ),

        # Candidate/final retrieval results
        # are preserved for observability.
        "hybrid_results": results,

        # IMPORTANT:
        # These are already reranked results because
        # retrieval.retrieve() calls rerank().
        "reranked_results": results,

        "retrieved_context": (
            retrieved_context
        ),

        # This is the actual prompt that will
        # be sent to Gemini.
        "rag_prompt": prompt,

        # Keep complete RAG output in state.
        "rag_data": rag_data,

        "trace": _add_trace(
            state,
            {
                "node": "rag",

                "status": "completed",

                "retrieved_chunks": len(
                    results
                ),

                "final_context_chunks": len(
                    context_data.get(
                        "sources",
                        [],
                    )
                ),
            },
        ),
    }


# ============================================================
# 6. MODEL ROUTER
# ============================================================

def model_router_node(
    state: DSAAgentState,
) -> dict[str, Any]:
    """
    Select the logical Gemini model route.

    The actual Gemini model IDs are configured in .env.

    Routes:
        fast  -> simple hints / syntax explanations
        debug -> runtime errors / wrong answers
        coach -> deeper DSA reasoning
    """

    from services.ai_coach import (
        select_model,
    )

    request_type = state.get(
        "request_type",
        "debug",
    )

    has_execution_error = (
        state.get(
            "has_runtime_error",
            False,
        )
        or state.get(
            "has_wrong_answer",
            False,
        )
        or state.get(
            "timed_out",
            False,
        )
    )

    has_syntax_error = (
        state.get(
            "has_syntax_error",
            False,
        )
    )

    hint_level = state.get(
        "hint_level",
        1,
    )

    selected_model = select_model(

        request_type=request_type,

        has_execution_error=(
            has_execution_error
        ),

        has_syntax_error=(
            has_syntax_error
        ),

        hint_level=hint_level,
    )

    return {

        "selected_model": (
            selected_model
        ),

        "trace": _add_trace(
            state,
            {
                "node": "model_router",

                "status": "completed",

                "selected_model": (
                    selected_model
                ),

                "request_type": (
                    request_type
                ),

                "syntax_error": (
                    has_syntax_error
                ),

                "execution_error": (
                    has_execution_error
                ),
            },
        ),
    }


# ============================================================
# 7. BUILD NON-RAG PROMPT
# ============================================================

def build_direct_coach_prompt(
    state: DSAAgentState,
) -> str:
    """
    Build a prompt for cases where RAG was intentionally
    skipped, primarily syntax errors.

    For syntax errors, deterministic analysis is more
    important than retrieving unrelated DSA knowledge.
    """

    problem = state.get(
        "problem",
        {},
    )

    code = state.get(
        "code",
        "",
    )

    language = state.get(
        "language",
        "python",
    )

    syntax_result = state.get(
        "syntax_result",
        {},
    )

    execution_result = state.get(
        "execution_result",
        {},
    )

    history = state.get(
        "student_history",
        [],
    )

    recurring_errors = state.get(
        "recurring_errors",
        [],
    )

    return f"""
DSA PROBLEM
-----------
Title:
{problem.get("title", "")}

Topic:
{problem.get("topic", "")}

Pattern:
{problem.get("pattern", "")}

Difficulty:
{problem.get("difficulty", "")}

PROBLEM DESCRIPTION
-------------------
{problem.get("description", "")}

STUDENT CODE
------------
```{language}
{code}
```

SYNTAX ANALYSIS
---------------
{syntax_result}

EXECUTION RESULT
----------------
{execution_result}

STUDENT HISTORY
---------------
{history}

RECURRING ERRORS
----------------
{recurring_errors}
"""


# ============================================================
# 8. BUILD RETRIEVAL QUERY NODE
# ============================================================

def build_retrieval_query_node(
    state: DSAAgentState,
) -> dict[str, Any]:
    """
    Build the retrieval query string from problem + code +
    execution context.
    """

    from rag.pipeline import build_debug_query

    problem = state.get("problem", {})
    code = state.get("code", "")
    execution_result = state.get(
        "execution_result", {},
    )
    syntax_result = state.get(
        "syntax_result", {},
    )

    query_text = build_debug_query(
        problem=problem,
        code=code,
        execution_result=execution_result,
        syntax_result=syntax_result,
    )

    return {
        "retrieval_query": query_text,

        "trace": _add_trace(
            state,
            {
                "node": "build_query",
                "status": "completed",
            },
        ),
    }


# ============================================================
# 9. RETRIEVE NODE
# ============================================================

def retrieve_node(
    state: DSAAgentState,
) -> dict[str, Any]:
    """
    Run hybrid search (vector + keyword + RRF).
    """

    from retrieval.hybrid_search import (
        hybrid_search,
    )
    from config import HYBRID_SEARCH_LIMIT

    query_text = state.get(
        "retrieval_query", "",
    )

    problem = state.get("problem", {})

    candidates = hybrid_search(
        query=query_text,
        topic=problem.get("topic"),
        subtopic=problem.get("subtopic"),
        pattern=problem.get("pattern"),
        difficulty=problem.get("difficulty"),
        limit=HYBRID_SEARCH_LIMIT,
    )

    return {
        "hybrid_results": candidates,

        "trace": _add_trace(
            state,
            {
                "node": "retrieve",
                "status": "completed",
                "candidate_count": len(
                    candidates
                ),
            },
        ),
    }


# ============================================================
# 10. RERANK NODE
# ============================================================

def rerank_node(
    state: DSAAgentState,
) -> dict[str, Any]:
    """
    Cross-encoder reranking + context building.
    """

    from retrieval.reranker import rerank
    from rag.context_builder import build_context
    from rag.prompts import build_coach_prompt
    from config import RERANK_LIMIT

    candidates = state.get(
        "hybrid_results", [],
    )
    query_text = state.get(
        "retrieval_query", "",
    )

    reranked = rerank(
        candidates=candidates,
        query=query_text,
        limit=RERANK_LIMIT,
    )

    # Normalize reranked results for downstream use
    normalized = []
    for rank, item in enumerate(reranked, 1):
        chunk = item["chunk"]
        normalized.append({
            "rank": rank,
            "chunk_id": str(chunk.get("id", "")),
            "document_id": str(
                chunk.get("document_id", "")
            ),
            "chunk_type": chunk.get(
                "chunk_type", ""
            ),
            "title": chunk.get("title", ""),
            "content": chunk.get("content", ""),
            "topic": chunk.get("topic", ""),
            "subtopic": chunk.get("subtopic", ""),
            "pattern": chunk.get("pattern", ""),
            "difficulty": chunk.get(
                "difficulty", ""
            ),
            "code": chunk.get("code", ""),
            "language": chunk.get("language", ""),
            "time_complexity": chunk.get(
                "time_complexity", ""
            ),
            "space_complexity": chunk.get(
                "space_complexity", ""
            ),
            "source_reference": chunk.get(
                "source_reference", ""
            ),
            "hybrid_score": item.get(
                "rrf_score", 0
            ),
            "rerank_score": item.get(
                "rerank_score", 0
            ),
            "final_score": item.get(
                "final_score", 0
            ),
        })

    # Build context from reranked results
    context_data = build_context(reranked)
    retrieved_context = context_data.get(
        "context", ""
    )

    # Build the final coach prompt
    problem = state.get("problem", {})
    code = state.get("code", "")
    execution_result = state.get(
        "execution_result", {},
    )
    syntax_result = state.get(
        "syntax_result", {},
    )
    student_history = state.get(
        "student_history", [],
    )
    recurring_errors = state.get(
        "recurring_errors", [],
    )
    request_type = state.get(
        "request_type", "debug",
    )
    hint_level = state.get("hint_level", 1)

    prompt = build_coach_prompt(
        problem=problem,
        student_code=code,
        execution_result=execution_result,
        syntax_result=syntax_result,
        retrieved_context=retrieved_context,
        student_history=student_history,
        recurring_errors=recurring_errors,
        request_type=request_type,
        hint_level=hint_level,
    )

    return {
        "reranked_results": normalized,
        "retrieved_context": retrieved_context,
        "rag_prompt": prompt,

        "trace": _add_trace(
            state,
            {
                "node": "rerank",
                "status": "completed",
                "reranked_count": len(normalized),
                "context_length": len(
                    retrieved_context
                ),
            },
        ),
    }


# ============================================================
# 11. SELECT MODEL NODE
# ============================================================

def select_model_node(
    state: DSAAgentState,
) -> dict[str, Any]:
    """
    Select the logical Gemini model route.
    """

    from services.ai_coach import select_model

    request_type = state.get(
        "request_type", "debug",
    )

    has_execution_error = (
        state.get("has_runtime_error", False)
        or state.get("has_wrong_answer", False)
        or state.get("timed_out", False)
    )

    has_syntax_error = state.get(
        "has_syntax_error", False,
    )

    hint_level = state.get("hint_level", 1)

    selected_model = select_model(
        request_type=request_type,
        has_execution_error=has_execution_error,
        has_syntax_error=has_syntax_error,
        hint_level=hint_level,
    )

    return {
        "selected_model": selected_model,

        "trace": _add_trace(
            state,
            {
                "node": "model_router",
                "status": "completed",
                "selected_model": selected_model,
            },
        ),
    }


# ============================================================
# 12. COACH NODE
# ============================================================

def coach_node(
    state: DSAAgentState,
) -> dict[str, Any]:
    """
    Call real Gemini API with the prepared prompt.
    """

    from services.ai_coach import (
        generate_coach_response,
    )

    # Use RAG prompt if available, otherwise
    # build a direct prompt for syntax errors.
    prompt = state.get("rag_prompt", "")

    if not prompt:
        prompt = build_direct_coach_prompt(state)

    selected_model = state.get(
        "selected_model", "coach",
    )

    ai_response, usage, latency_ms = (
        generate_coach_response(
            prompt=prompt,
            model_name=selected_model,
        )
    )

    coach_response = ai_response.model_dump()

    return {
        "coach_response": coach_response,

        "token_usage": {
            "prompt_tokens": usage.get(
                "prompt_tokens", 0
            ),
            "completion_tokens": usage.get(
                "completion_tokens", 0
            ),
            "total_tokens": usage.get(
                "total_tokens", 0
            ),
        },

        "latency_ms": latency_ms,

        "trace": _add_trace(
            state,
            {
                "node": "coach",
                "status": "completed",
                "model": selected_model,
                "latency_ms": latency_ms,
                "total_tokens": usage.get(
                    "total_tokens", 0
                ),
            },
        ),
    }


# ============================================================
# 13. SUCCESS NODE
# ============================================================

def success_node(
    state: DSAAgentState,
) -> dict[str, Any]:
    """
    Handle accepted solutions.
    Provides complexity feedback via Gemini.
    """

    from services.ai_coach import (
        generate_coach_response,
    )

    problem = state.get("problem", {})
    code = state.get("code", "")
    language = state.get("language", "python")

    prompt = f"""
The student's solution for "{problem.get("title", "")}"
has been ACCEPTED. All test cases passed.

Problem topic: {problem.get("topic", "")}
Pattern: {problem.get("pattern", "")}
Difficulty: {problem.get("difficulty", "")}

Student code:
```{language}
{code}
```

Please:
1. Acknowledge the correct solution.
2. Analyze the time and space complexity.
3. Identify the DSA pattern used.
4. Suggest any possible optimization.
5. Do NOT invent any error.
6. Set error_line to null.
7. Set error_type to null.
8. Set status to "Correct".
"""

    ai_response, usage, latency_ms = (
        generate_coach_response(
            prompt=prompt,
            model_name="coach",
        )
    )

    coach_response = ai_response.model_dump()

    return {
        "coach_response": coach_response,
        "solved": True,

        "token_usage": {
            "prompt_tokens": usage.get(
                "prompt_tokens", 0
            ),
            "completion_tokens": usage.get(
                "completion_tokens", 0
            ),
            "total_tokens": usage.get(
                "total_tokens", 0
            ),
        },

        "latency_ms": latency_ms,

        "trace": _add_trace(
            state,
            {
                "node": "success",
                "status": "completed",
                "latency_ms": latency_ms,
            },
        ),
    }