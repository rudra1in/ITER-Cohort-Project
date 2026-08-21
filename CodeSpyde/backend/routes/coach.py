from fastapi import (
    APIRouter,
    HTTPException,
)

from models.schemas import (
    CoachRequest,
    CoachResponse,
)

from services.student_history import (
    save_attempt,
)

from services.token_tracker import (
    save_token_usage,
)

from agent.graph import (
    dsa_coach_graph,
)


# ============================================================
# ROUTER
# ============================================================

router = APIRouter(
    prefix="/api/coach",
    tags=["AI Coach"],
)


# ============================================================
# MAIN AI COACH ENDPOINT
# ============================================================

@router.post(
    "",
    response_model=CoachResponse,
)
async def coach(
    request: CoachRequest,
):
    """
    Main AI DSA Coach endpoint.

    LangGraph is responsible for:

        1. Loading the problem
        2. Loading student memory
        3. Static code analysis
        4. Code execution
        5. RAG retrieval
        6. Reranking
        7. Model routing
        8. Gemini coaching
        9. Structured AI response

    This route is responsible for:

        1. Receiving the API request
        2. Creating the agent thread
        3. Invoking LangGraph
        4. Saving the attempt
        5. Saving token usage
        6. Returning the response
    """

    # ========================================================
    # CREATE THREAD ID
    # ========================================================

    thread_id = (
        f"{request.user_id}:"
        f"{request.problem_id}"
    )

    # ========================================================
    # INITIAL LANGGRAPH STATE
    # ========================================================

    initial_state = {

        "user_id": request.user_id,

        "thread_id": thread_id,

        "problem_id": request.problem_id,

        "code": request.code,

        "language": request.language,

        "request_type": (
            request.request_type
        ),

        "hint_level": (
            request.hint_level
        ),

        "iteration": 0,

        "errors": [],

        "trace": [],
    }

    # ========================================================
    # LANGGRAPH CONFIG
    # ========================================================

    config = {
        "configurable": {
            "thread_id": thread_id,
        }
    }

    # ========================================================
    # RUN DSA COACH AGENT
    # ========================================================

    try:

        result = (
            dsa_coach_graph.invoke(
                initial_state,
                config=config,
            )
        )

    except HTTPException:
        raise

    except Exception as exc:

        print(
            "DSA Coach agent error:",
            str(exc),
        )

        raise HTTPException(
            status_code=500,
            detail=(
                "The AI Coach could not "
                "process this request."
            ),
        ) from exc

    # ========================================================
    # EXTRACT AGENT RESULTS
    # ========================================================

    ai_response = result.get(
        "coach_response",
        {},
    )

    execution_result = result.get(
        "execution_result",
        {},
    )

    syntax_result = result.get(
        "syntax_result",
        {},
    )

    usage = result.get(
        "token_usage",
        {
            "prompt_tokens": 0,
            "completion_tokens": 0,
            "total_tokens": 0,
        },
    )

    latency_ms = result.get(
        "latency_ms",
        0,
    )

    selected_model = result.get(
        "selected_model",
        "unknown",
    )

    reranked_results = result.get(
        "reranked_results",
        [],
    )

    trace = result.get(
        "trace",
        [],
    )

    # ========================================================
    # BUILD CLEAN SOURCE LIST
    # ========================================================

    sources = []

    for item in reranked_results:

        sources.append(
            {
                "chunk_id": item.get(
                    "chunk_id"
                ),

                "title": item.get(
                    "title",
                    "DSA Knowledge",
                ),

                "topic": item.get(
                    "topic",
                    "",
                ),

                "pattern": item.get(
                    "pattern",
                    "",
                ),

                "chunk_type": item.get(
                    "chunk_type",
                    "knowledge",
                ),

                "score": item.get(
                    "score",
                    item.get(
                        "reranker_score",
                        0,
                    ),
                ),

                "snippet": item.get(
                    "content",
                    "",
                ),
            }
        )

    # ========================================================
    # ADD RAG SOURCES TO AI RESPONSE
    # ========================================================

    if hasattr(
        ai_response,
        "sources",
    ):

        ai_response.sources = (
            sources
        )

    elif isinstance(
        ai_response,
        dict,
    ):

        ai_response[
            "sources"
        ] = sources

    # ========================================================
    # EXTRACT ERROR INFORMATION
    # ========================================================

    if hasattr(
        ai_response,
        "error_line",
    ):

        error_line = (
            ai_response.error_line
        )

        error_type = (
            ai_response.error_type
        )

        error_message = (
            ai_response.diagnosis
        )

    elif isinstance(
        ai_response,
        dict,
    ):

        error_line = ai_response.get(
            "error_line"
        )

        error_type = ai_response.get(
            "error_type"
        )

        error_message = (
            ai_response.get(
                "diagnosis",
                "",
            )
        )

    else:

        error_line = None

        error_type = None

        error_message = ""

    # ========================================================
    # EXECUTION STATUS
    # ========================================================

    execution_status = (
        execution_result.get(
            "status",
            "unknown",
        )
    )

    # ========================================================
    # SOLVED STATUS
    # ========================================================

    solved = result.get(
        "solved",
        execution_status
        in {
            "accepted",
            "success",
            "passed",
        },
    )

    # Make sure this is a boolean.
    solved = bool(solved)

    # ========================================================
    # CONVERT AI RESPONSE FOR DATABASE
    # ========================================================

    if hasattr(
        ai_response,
        "model_dump",
    ):

        coach_response_data = (
            ai_response.model_dump()
        )

    elif isinstance(
        ai_response,
        dict,
    ):

        coach_response_data = (
            ai_response
        )

    else:

        coach_response_data = {}

    # ========================================================
    # SAVE STUDENT ATTEMPT
    # ========================================================

    try:

        save_attempt(

            user_id=request.user_id,

            problem_id=request.problem_id,

            code=request.code,

            language=request.language,

            status=execution_status,

            error_type=error_type,

            error_line=error_line,

            error_message=error_message,

            solved=solved,

            execution_result=(
                execution_result
            ),

            coach_response=(
                coach_response_data
            ),
        )

    except Exception as db_err:

        # Database failures should not make
        # the AI Coach unusable.

        print(
            "Skipping save_attempt. "
            "Database error:",
            str(db_err),
        )

    # ========================================================
    # SAVE TOKEN USAGE
    # ========================================================

    try:

        save_token_usage(

            user_id=request.user_id,

            problem_id=request.problem_id,

            model_name=selected_model,

            request_type=(
                request.request_type
            ),

            usage=usage,

            retrieved_chunks=len(
                reranked_results
            ),

            latency_ms=latency_ms,
        )

    except Exception as db_err:

        print(
            "Skipping save_token_usage. "
            "Database error:",
            str(db_err),
        )

    # ========================================================
    # FINAL RESPONSE
    # ========================================================

    return CoachResponse(

        status="success",

        model_used=selected_model,

        response=ai_response,

        retrieved_chunks=len(
            reranked_results
        ),

        sources=sources,

        token_usage={
            **usage,

            "latency_ms": (
                latency_ms
            ),
        },
    )