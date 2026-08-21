from functools import lru_cache

from config import (
    RERANKER_ENABLED,
    RERANKER_MODEL,
    RERANK_LIMIT
)


@lru_cache(maxsize=1)
def get_reranker():

    if not RERANKER_ENABLED:

        return None

    try:

        from sentence_transformers import (
            CrossEncoder
        )

        return CrossEncoder(
            RERANKER_MODEL
        )

    except ImportError as error:

        raise RuntimeError(
            "sentence-transformers is "
            "required for reranking. "
            "Install it with: "
            "pip install sentence-transformers"
        ) from error


def build_reranker_text(
    chunk: dict
) -> str:

    parts = [
        f"Title: {chunk.get('title', '')}",
        f"Type: {chunk.get('chunk_type', '')}",
        f"Topic: {chunk.get('topic', '')}",
        f"Subtopic: {chunk.get('subtopic', '')}",
        f"Pattern: {chunk.get('pattern', '')}",
        f"Difficulty: {chunk.get('difficulty', '')}",
        "",
        chunk.get("content", "")
    ]

    return "\n".join(
        parts
    )


def _metadata_bonus(
    chunk: dict,
    query: str
) -> float:

    """
    Small deterministic bonus for DSA-specific
    relevance.

    This is intentionally much smaller than the
    cross-encoder score.
    """

    query_lower = query.lower()

    bonus = 0.0

    pattern = (
        chunk.get("pattern")
        or ""
    ).lower()

    topic = (
        chunk.get("topic")
        or ""
    ).lower()

    chunk_type = (
        chunk.get("chunk_type")
        or ""
    ).lower()

    if pattern and pattern in query_lower:

        bonus += 0.08

    if topic and topic in query_lower:

        bonus += 0.05

    # Coaching questions should favor
    # intuition/mistake/approach chunks
    # over complete solutions.

    coaching_words = [
        "why",
        "mistake",
        "wrong",
        "error",
        "hint",
        "stuck",
        "understand",
        "explain"
    ]

    if any(
        word in query_lower
        for word in coaching_words
    ):

        if chunk_type == "mistakes":

            bonus += 0.08

        elif chunk_type == "intuition":

            bonus += 0.06

        elif chunk_type == "approach":

            bonus += 0.04

        elif chunk_type == "solution":

            bonus -= 0.03

    return bonus


def rerank(
    candidates: list[dict],
    query: str,
    limit: int = RERANK_LIMIT
) -> list[dict]:

    if not candidates:

        return []

    # -----------------------------------------------------
    # If disabled, return hybrid ranking.
    # -----------------------------------------------------

    if not RERANKER_ENABLED:

        return candidates[:limit]

    reranker = get_reranker()

    if reranker is None:

        return candidates[:limit]

    # -----------------------------------------------------
    # Build cross-encoder pairs
    # -----------------------------------------------------

    pairs = []

    for candidate in candidates:

        chunk = candidate[
            "chunk"
        ]

        chunk_text = build_reranker_text(
            chunk
        )

        pairs.append(
            [
                query,
                chunk_text
            ]
        )

    # -----------------------------------------------------
    # Predict relevance
    # -----------------------------------------------------

    scores = reranker.predict(
        pairs,
        show_progress_bar=False
    )

    # -----------------------------------------------------
    # Attach scores
    # -----------------------------------------------------

    ranked = []

    for candidate, score in zip(
        candidates,
        scores
    ):

        chunk = candidate[
            "chunk"
        ]

        cross_score = float(
            score
        )

        metadata_bonus = (
            _metadata_bonus(
                chunk,
                query
            )
        )

        final_score = (
            cross_score
            + metadata_bonus
        )

        item = {
            **candidate,

            "rerank_score":
                cross_score,

            "metadata_bonus":
                metadata_bonus,

            "final_score":
                final_score
        }

        ranked.append(
            item
        )

    # -----------------------------------------------------
    # Final ranking
    # -----------------------------------------------------

    ranked.sort(
        key=lambda item: item[
            "final_score"
        ],
        reverse=True
    )

    return ranked[:limit]