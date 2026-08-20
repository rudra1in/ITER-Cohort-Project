from fastapi import APIRouter
from pydantic import BaseModel, Field

from retrieval.retriever import (
    DSAQuery,
    retrieve
)

from rag.context_builder import (
    build_context
)


router = APIRouter(
    prefix="/api/rag",
    tags=["RAG"]
)


class RAGSearchRequest(BaseModel):

    query: str = Field(
        min_length=2
    )

    topic: str | None = None

    subtopic: str | None = None

    pattern: str | None = None

    difficulty: str | None = None

    chunk_type: str | None = None

    top_k: int = Field(
        default=6,
        ge=1,
        le=10
    )


@router.post("/search")
async def search(
    request: RAGSearchRequest
):

    query = DSAQuery(
        query=request.query,

        topic=request.topic,

        subtopic=request.subtopic,

        pattern=request.pattern,

        difficulty=request.difficulty,

        chunk_type=request.chunk_type
    )

    results = retrieve(
        query
    )

    context = build_context(
        results,
        max_chunks=request.top_k
    )

    return {
        "query": request.query,

        "retrieval": {
            "candidate_count":
                len(results),

            "final_count":
                context["count"]
        },

        "results": results,

        "context": context["context"],

        "sources": context["sources"]
    }