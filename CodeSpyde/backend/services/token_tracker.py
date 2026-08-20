import time
from typing import Optional

from database import get_db_cursor


def extract_usage(
    response
) -> dict:

    """
    Extract token usage from Gemini response.

    SDK response structures can evolve, so this function
    deliberately handles missing metadata safely.
    """

    usage = getattr(
        response,
        "usage_metadata",
        None
    )

    if usage is None:

        return {
            "input_tokens": 0,
            "output_tokens": 0,
            "total_tokens": 0
        }

    input_tokens = getattr(
        usage,
        "prompt_token_count",
        0
    ) or 0

    output_tokens = getattr(
        usage,
        "candidates_token_count",
        0
    ) or 0

    total_tokens = getattr(
        usage,
        "total_token_count",
        0
    ) or (
        input_tokens
        + output_tokens
    )

    return {
        "input_tokens": int(
            input_tokens
        ),

        "output_tokens": int(
            output_tokens
        ),

        "total_tokens": int(
            total_tokens
        )
    }


def save_token_usage(
    user_id: Optional[str],
    problem_id: Optional[str],
    model_name: str,
    request_type: str,
    usage: dict,
    retrieved_chunks: int,
    latency_ms: int
):

    with get_db_cursor() as cursor:

        cursor.execute(
            """
            INSERT INTO token_usage
            (
                user_id,
                problem_id,
                model_name,
                request_type,
                input_tokens,
                output_tokens,
                total_tokens,
                retrieved_chunks,
                latency_ms
            )
            VALUES
            (
                %s,%s,%s,%s,
                %s,%s,%s,%s,%s
            )
            """,
            (
                user_id,

                problem_id,

                model_name,

                request_type,

                usage.get(
                    "input_tokens",
                    usage.get(
                        "prompt_tokens",
                        0,
                    ),
                ),

                usage.get(
                    "output_tokens",
                    usage.get(
                        "completion_tokens",
                        0,
                    ),
                ),

                usage.get(
                    "total_tokens",
                    0,
                ),

                retrieved_chunks,

                latency_ms,
            )
        )


class TokenTimer:

    def __init__(self):

        self.start_time = None

    def start(self):

        self.start_time = time.perf_counter()

    def elapsed_ms(self) -> int:

        if self.start_time is None:
            return 0

        return int(
            (
                time.perf_counter()
                - self.start_time
            )
            * 1000
        )