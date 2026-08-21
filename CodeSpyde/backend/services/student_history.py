from typing import Optional

from database import get_db_cursor


def save_attempt(
    user_id: Optional[str],
    problem_id: str,
    code: str,
    language: str,
    status: str,
    error_type: Optional[str],
    error_line: Optional[int],
    error_message: Optional[str],
    solved: bool,
    execution_result: dict,
    coach_response: Optional[dict]
):

    with get_db_cursor() as cursor:

        # -------------------------------------------------
        # Count previous attempts
        # -------------------------------------------------

        cursor.execute(
            """
            SELECT COUNT(*)
            FROM student_attempts

            WHERE
                problem_id = %s

                AND (
                    user_id = %s
                    OR (
                        user_id IS NULL
                        AND %s IS NULL
                    )
                )
            """,
            (
                problem_id,
                user_id,
                user_id
            )
        )

        previous_attempts = (
            cursor.fetchone()[0]
        )

        attempts = (
            previous_attempts + 1
        )

        # -------------------------------------------------
        # Insert attempt
        # -------------------------------------------------

        cursor.execute(
            """
            INSERT INTO student_attempts
            (
                user_id,
                problem_id,
                code,
                language,
                status,
                error_type,
                error_line,
                error_message,
                attempts,
                solved,
                execution_result,
                coach_response
            )

            VALUES
            (
                %s,%s,%s,%s,%s,
                %s,%s,%s,%s,%s,
                %s::jsonb,
                %s::jsonb
            )
            """,
            (
                user_id,

                problem_id,

                code,

                language,

                status,

                error_type,

                error_line,

                error_message,

                attempts,

                solved,

                _json(execution_result),

                _json(coach_response)
            )
        )

        return attempts


def get_student_history(
    user_id: Optional[str],
    problem_id: str,
    limit: int = 5
) -> list[dict]:

    if user_id is None:

        return []

    with get_db_cursor(
        dict_cursor=True
    ) as cursor:

        cursor.execute(
            """
            SELECT
                id,
                problem_id,
                status,
                error_type,
                error_line,
                error_message,
                attempts,
                solved,
                created_at
            FROM student_attempts

            WHERE
                user_id = %s
                AND problem_id = %s

            ORDER BY
                created_at DESC

            LIMIT %s
            """,
            (
                user_id,
                problem_id,
                limit
            )
        )

        rows = cursor.fetchall()

    return [
        dict(row)
        for row in rows
    ]


def get_recurring_errors(
    user_id: Optional[str],
    limit: int = 10
) -> list[dict]:

    if user_id is None:

        return []

    with get_db_cursor(
        dict_cursor=True
    ) as cursor:

        cursor.execute(
            """
            SELECT
                error_type,
                COUNT(*) AS occurrences

            FROM student_attempts

            WHERE
                user_id = %s
                AND error_type IS NOT NULL

            GROUP BY
                error_type

            ORDER BY
                occurrences DESC

            LIMIT %s
            """,
            (
                user_id,
                limit
            )
        )

        rows = cursor.fetchall()

    return [
        dict(row)
        for row in rows
    ]


def _json(value):

    import json

    return json.dumps(
        value or {},
        default=str
    )