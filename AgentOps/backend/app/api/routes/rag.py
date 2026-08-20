from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.rag.service import ask_dsa_coach


router = APIRouter(
    prefix="/api/rag",
    tags=["RAG"],
)


class RAGRequest(BaseModel):
    query: str
    top_k: int = 5


@router.post("/ask")
def ask_rag(request: RAGRequest):

    if not request.query.strip():
        raise HTTPException(
            status_code=400,
            detail="Query cannot be empty.",
        )

    try:
        return ask_dsa_coach(
            query=request.query,
            top_k=request.top_k,
        )

    except Exception as error:
        print(f"RAG error: {error}")

        raise HTTPException(
            status_code=500,
            detail="Failed to generate DSA Coach response.",
        )