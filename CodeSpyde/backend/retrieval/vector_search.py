from typing import Optional

from database import get_db_cursor

from embeddings.gemini_embeddings import (
    create_embedding
)

from config import (
    VECTOR_SEARCH_LIMIT
)


def vector_search(
    query: str,
    topic: Optional[str] = None,
    subtopic: Optional[str] = None,
    pattern: Optional[str] = None,
    difficulty: Optional[str] = None,
    chunk_type: Optional[str] = None,
    limit: int = VECTOR_SEARCH_LIMIT
) -> list[dict]:

    """
    Perform semantic vector search using pgvector.

    Filters are applied before similarity ranking.
    """

    query_embedding = create_embedding(
        query
    )

    return vector_search_by_embedding(
        query_embedding=query_embedding,
        topic=topic,
        subtopic=subtopic,
        pattern=pattern,
        difficulty=difficulty,
        chunk_type=chunk_type,
        limit=limit
    )


def vector_search_by_embedding(
    query_embedding: list[float],
    topic: Optional[str] = None,
    subtopic: Optional[str] = None,
    pattern: Optional[str] = None,
    difficulty: Optional[str] = None,
    chunk_type: Optional[str] = None,
    limit: int = VECTOR_SEARCH_LIMIT
) -> list[dict]:

    conditions = []
    params = []

    # -----------------------------------------------------
    # Metadata filtering
    # -----------------------------------------------------

    if topic:

        conditions.append(
            "LOWER(topic) = LOWER(%s)"
        )

        params.append(topic)

    if subtopic:

        conditions.append(
            "LOWER(subtopic) = LOWER(%s)"
        )

        params.append(subtopic)

    if pattern:

        conditions.append(
            "LOWER(pattern) = LOWER(%s)"
        )

        params.append(pattern)

    if difficulty:

        conditions.append(
            "LOWER(difficulty) = LOWER(%s)"
        )

        params.append(difficulty)

    if chunk_type:

        conditions.append(
            "LOWER(chunk_type) = LOWER(%s)"
        )

        params.append(chunk_type)

    where_clause = ""

    if conditions:

        where_clause = (
            "WHERE "
            + " AND ".join(
                conditions
            )
        )

    sql = f"""
        SELECT
            id,
            document_id,
            chunk_index,
            chunk_type,
            title,
            content,
            topic,
            subtopic,
            pattern,
            difficulty,
            code,
            language,
            time_complexity,
            space_complexity,
            source_reference,
            token_count,
            metadata,

            1 - (
                embedding
                <=> %s::vector
            ) AS similarity

        FROM dsa_chunks

        {where_clause}

        ORDER BY
            embedding <=> %s::vector

        LIMIT %s
    """

    # Embedding appears twice in SQL.
    # One is used for similarity selection,
    # one for ordering.

    sql_params = [
        query_embedding,
        *params,
        query_embedding,
        limit
    ]

    with get_db_cursor(
        dict_cursor=True
    ) as cursor:

        cursor.execute(
            sql,
            sql_params
        )

        rows = cursor.fetchall()

    results = []

    for row in rows:

        item = dict(row)

        item["similarity"] = float(
            item["similarity"]
        )

        results.append(item)

    return results