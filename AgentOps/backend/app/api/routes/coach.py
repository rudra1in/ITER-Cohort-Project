from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Any
from uuid import uuid4
import traceback

from app.agents.graph.graph import graph

# ============================================================
# ROUTER
# ============================================================

router = APIRouter(
    prefix="/api/coach",
    tags=["Coach"],
)

# ============================================================
# REQUEST SCHEMA
# ============================================================

class CoachRequest(BaseModel):
    """
    Request received from the frontend.
    """

    message: str = Field(..., min_length=1)

    mode: str = "explain"

    language: str = "java"

    code: str = ""

    problem: dict[str, Any] | None = None

    # --------------------------------------------------------
    # Conversation / session
    # --------------------------------------------------------

    thread_id: str | None = None

    user_id: str | None = None

# ============================================================
# SOURCE RESPONSE
# ============================================================

class CoachSource(BaseModel):
    problem_id: str | None = None
    title: str | None = None
    section: str | None = None
    distance: float | None = None
    rerank_score: float | None = None

# ============================================================
# RESPONSE SCHEMA
# ============================================================

class CoachResponse(BaseModel):
    query: str
    answer: str
    agent_type: str
    evaluation: str
    retry_count: int
    thread_id: str
    conversation: list[dict[str, Any]]
    sources: list[CoachSource]

# ============================================================
# HELPER — BUILD SOURCES
# ============================================================

def build_sources(
    documents: list[Any],
) -> list[CoachSource]:
    """
    Convert retrieved RAG documents into a safe API response.

    The exact document structure can vary depending on the
    retriever implementation, so this function handles common
    formats safely.
    """

    sources = []

    for document in documents or []:

        # ----------------------------------------------------
        # Dictionary-based document
        # ----------------------------------------------------

        if isinstance(document, dict):

            metadata = document.get(
                "metadata",
                {},
            )

            if not isinstance(metadata, dict):
                metadata = {}

            sources.append(
                CoachSource(
                    problem_id=(
                        metadata.get("problem_id")
                        or document.get("problem_id")
                    ),
                    title=(
                        metadata.get("title")
                        or document.get("title")
                    ),
                    section=(
                        metadata.get("section")
                        or document.get("section")
                    ),
                    distance=document.get(
                        "distance"
                    ),
                    rerank_score=metadata.get(
                        "rerank_score"
                    ),
                )
            )

            continue
        # ----------------------------------------------------
        # LangChain Document-like object
        # ----------------------------------------------------

        metadata = getattr(
            document,
            "metadata",
            {},
        )

        if not isinstance(metadata, dict):
            metadata = {}

        sources.append(
            CoachSource(
                problem_id=metadata.get(
                    "problem_id"
                ),
                title=metadata.get(
                    "title"
                ),
                section=metadata.get(
                    "section"
                ),
                distance=metadata.get(
                    "distance"
                ),
            )
        )
    return sources


# ============================================================
# ASK COACH
# ============================================================

@router.post("/ask", response_model=CoachResponse)
def ask_coach(request: CoachRequest):

    try:

        # ----------------------------------------------------
        # Generate thread ID if frontend doesn't provide one
        # ----------------------------------------------------

        thread_id = (
            request.thread_id
            or str(uuid4())
        )

        # ----------------------------------------------------
        # Build LangGraph configuration
        # ----------------------------------------------------

        config = {
            "configurable": {
                "thread_id": thread_id,
            }
        }

        # ----------------------------------------------------
        # Build graph input
        # ----------------------------------------------------

        graph_input = {
            "message": request.message,
            "mode": request.mode,
            "language": request.language,
            "code": request.code,
            "problem": request.problem,
            "user_id": request.user_id,
            "thread_id": thread_id,

            # ------------------------------------------------
            # Self-correction configuration
            # ------------------------------------------------

            "retry_count": 0,
            "max_retries": 2,
        }

        # ----------------------------------------------------
        # Invoke LangGraph
        # ----------------------------------------------------

        result = graph.invoke(
            graph_input,
            config,
        )

        # ----------------------------------------------------
        # Extract final answer
        # ----------------------------------------------------

        answer = result.get(
            "answer",
            "",
        )

        # ----------------------------------------------------
        # Extract conversation
        # ----------------------------------------------------

        conversation = result.get(
            "conversation",
            [],
        )

        # ----------------------------------------------------
        # Extract retrieved documents
        # ----------------------------------------------------

        documents = result.get(
            "retrieved_documents",
            [],
        )

        # ----------------------------------------------------
        # Build response
        # ----------------------------------------------------

        return CoachResponse(
            query=request.message,

            answer=answer,

            agent_type=result.get(
                "agent_type",
                "coach",
            ),

            evaluation=result.get(
                "evaluation",
                "good",
            ),

            retry_count=result.get(
                "retry_count",
                0,
            ),

            thread_id=thread_id,

            conversation=conversation,

            sources=build_sources(
                documents
            ),
        )

    except Exception as error:
        print("========== COACH ERROR ==========")
        traceback.print_exc()
        print("=================================")

        raise HTTPException(
            status_code=500,
            detail=str(error),
        )

    """except Exception as error:
    
        print(
            "Coach graph error:",
            error,
        )

        raise HTTPException(
            status_code=500,
            detail="Failed to generate coach response.",
        )"""