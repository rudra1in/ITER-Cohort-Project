from typing import Optional

from retrieval.vector_search import (
    vector_search_by_embedding
)

from retrieval.keyword_search import (
    keyword_search
)

from embeddings.gemini_embeddings import (
    create_embedding
)

from config import (
    VECTOR_SEARCH_LIMIT,
    KEYWORD_SEARCH_LIMIT,
    HYBRID_SEARCH_LIMIT
)


RRF_K = 60


def _rrf_score(
    rank: int
) -> float:

    return 1.0 / (
        RRF_K + rank
    )


def hybrid_search(
    query: str,
    topic: Optional[str] = None,
    subtopic: Optional[str] = None,
    pattern: Optional[str] = None,
    difficulty: Optional[str] = None,
    chunk_type: Optional[str] = None,
    limit: int = HYBRID_SEARCH_LIMIT
) -> list[dict]:

    # -----------------------------------------------------
    # Generate embedding ONLY ONCE
    # -----------------------------------------------------

    query_embedding = create_embedding(
        query
    )

    # -----------------------------------------------------
    # Semantic search
    # -----------------------------------------------------

    vector_results = (
        vector_search_by_embedding(
            query_embedding=query_embedding,
            topic=topic,
            subtopic=subtopic,
            pattern=pattern,
            difficulty=difficulty,
            chunk_type=chunk_type,
            limit=VECTOR_SEARCH_LIMIT
        )
    )

    # -----------------------------------------------------
    # Keyword search
    # -----------------------------------------------------

    keyword_results = keyword_search(
        query=query,
        topic=topic,
        subtopic=subtopic,
        pattern=pattern,
        difficulty=difficulty,
        chunk_type=chunk_type,
        limit=KEYWORD_SEARCH_LIMIT
    )

    # -----------------------------------------------------
    # Merge using RRF
    # -----------------------------------------------------

    candidates = {}

    # Vector ranking

    for rank, result in enumerate(
        vector_results,
        start=1
    ):

        chunk_id = str(
            result["id"]
        )

        if chunk_id not in candidates:

            candidates[chunk_id] = {
                "chunk": result,
                "vector_rank": None,
                "keyword_rank": None,
                "rrf_score": 0.0
            }

        candidates[
            chunk_id
        ]["vector_rank"] = rank

        candidates[
            chunk_id
        ]["rrf_score"] += _rrf_score(
            rank
        )

    # Keyword ranking

    for rank, result in enumerate(
        keyword_results,
        start=1
    ):

        chunk_id = str(
            result["id"]
        )

        if chunk_id not in candidates:

            candidates[chunk_id] = {
                "chunk": result,
                "vector_rank": None,
                "keyword_rank": None,
                "rrf_score": 0.0
            }

        candidates[
            chunk_id
        ]["keyword_rank"] = rank

        candidates[
            chunk_id
        ]["rrf_score"] += _rrf_score(
            rank
        )

    # -----------------------------------------------------
    # Sort
    # -----------------------------------------------------

    ranked = sorted(
        candidates.values(),
        key=lambda item: item[
            "rrf_score"
        ],
        reverse=True
    )

    # -----------------------------------------------------
    # Return candidate pool
    # -----------------------------------------------------

    return ranked[:limit]