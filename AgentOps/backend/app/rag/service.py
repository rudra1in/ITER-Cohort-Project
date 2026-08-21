from app.rag.retriever import similarity_search
from app.rag.generator import generate_answer


def ask_dsa_coach(
    query: str,
    top_k: int = 5,
) -> dict:
    """
    Complete RAG pipeline:

    Query
      ↓
    Retriever
      ↓
    Retrieved chunks
      ↓
    Gemini
      ↓
    Answer
    """

    documents = similarity_search(
        query=query,
        top_k=top_k,
    )

    answer = generate_answer(
        query=query,
        documents=documents,
    )

    sources = []

    for document in documents:

        sources.append(
            {
                "problem_id": document.metadata.get(
                    "problem_id"
                ),
                "title": document.metadata.get(
                    "title"
                ),
                "section": document.metadata.get(
                    "section"
                ),
                "distance": document.metadata.get(
                    "distance"
                ),
                "rerank_score": document.metadata.get(
                    "rerank_score"
                ),
            }
        )

    return {
        "query": query,
        "answer": answer,
        "sources": sources,
    }