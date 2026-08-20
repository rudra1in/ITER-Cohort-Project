from typing import Optional

from database import get_db_cursor

from config import (
    KEYWORD_SEARCH_LIMIT
)


def keyword_search(
    query: str,
    topic: Optional[str] = None,
    subtopic: Optional[str] = None,
    pattern: Optional[str] = None,
    difficulty: Optional[str] = None,
    chunk_type: Optional[str] = None,
    limit: int = KEYWORD_SEARCH_LIMIT
) -> list[dict]:

    conditions = [
        """
        search_vector @@
        websearch_to_tsquery(
            'english',
            %s
        )
        """
    ]

    params = [query]

    # -----------------------------------------------------
    # Metadata filters
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

    where_clause = (
        " AND ".join(
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

            ts_rank_cd(
                search_vector,
                websearch_to_tsquery(
                    'english',
                    %s
                )
            ) AS keyword_score

        FROM dsa_chunks

        WHERE {where_clause}

        ORDER BY
            keyword_score DESC

        LIMIT %s
    """

    # Query appears once in WHERE and once in rank.

    sql_params = [
        query,
        *params,
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

        item["keyword_score"] = float(
            item["keyword_score"]
        )

        results.append(item)

    return results