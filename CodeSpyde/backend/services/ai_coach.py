from __future__ import annotations

import os
import time
from typing import Type

from google import genai
from pydantic import BaseModel

from models.schemas import CoachAIResponse


# ============================================================
# Gemini Client
# ============================================================

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise RuntimeError(
        "GEMINI_API_KEY is not configured."
    )

client = genai.Client(
    api_key=GEMINI_API_KEY
)


# ============================================================
# Model Configuration
# ============================================================

MODEL_ROUTES = {
    "fast": os.getenv(
        "GEMINI_FAST_MODEL",
        "gemini-3.5-flash",
    ),

    "debug": os.getenv(
        "GEMINI_DEBUG_MODEL",
        "gemini-3.5-flash",
    ),

    "coach": os.getenv(
        "GEMINI_COACH_MODEL",
        "gemini-3.6-flash",
    ),
}


# ============================================================
# System Instruction
# ============================================================

COACH_SYSTEM_PROMPT = """
You are CodeMentor, an expert Data Structures and
Algorithms programming coach.

Your job is to help a student understand WHY their
solution is failing instead of immediately giving them
the complete solution.

IMPORTANT RULES:

1. Never invent an error.

2. Never claim a specific line is incorrect unless
   the supplied code analysis or execution traceback
   supports that conclusion.

3. Use the execution result as the source of truth
   for runtime errors and wrong answers.

4. Explain the underlying DSA concept.

5. Identify the relevant problem-solving pattern.

6. Give a progressive hint instead of immediately
   revealing the complete solution.

7. Consider the student's previous mistakes when
   student history is supplied.

8. If the student's solution is correct, acknowledge
   that and provide complexity feedback.

9. Keep explanations concise and useful.

10. Do not provide a complete solution unless the
    request explicitly asks for it or the hint level
    permits it.

11. Do not pretend that RAG sources say something
    they do not say.

12. If the available information is insufficient to
    determine the exact error, explicitly say that.

Return ONLY the requested structured response.
"""


# ============================================================
# Model Router
# ============================================================

def select_model(
    request_type: str,
    has_execution_error: bool,
    has_syntax_error: bool,
    hint_level: int,
) -> str:
    """
    Select a logical model route.

    The actual Gemini model names are configured through
    environment variables.

    Routes:
        fast  -> lightweight hints/simple explanations
        debug -> runtime/wrong-answer debugging
        coach -> deeper DSA reasoning
    """

    if has_syntax_error:
        return "fast"

    if has_execution_error:
        return "debug"

    if request_type == "hint":
        return "fast"

    return "coach"


# ============================================================
# Prompt Builder
# ============================================================

def build_coach_prompt(
    *,
    prompt: str,
) -> str:
    """
    The LangGraph layer already prepares the complete
    context.

    This function keeps the Gemini service independent
    from LangGraph.
    """

    return prompt


# ============================================================
# Real Gemini Generation
# ============================================================

def generate_coach_response(
    prompt: str,
    model_name: str,
) -> tuple[CoachAIResponse, dict, int]:
    """
    Generate a real structured response from Gemini.

    Returns:

        CoachAIResponse
        token usage dictionary
        latency in milliseconds
    """

    started = time.perf_counter()

    # --------------------------------------------------------
    # Resolve logical route to actual Gemini model
    # --------------------------------------------------------

    actual_model = MODEL_ROUTES.get(
        model_name,
        model_name,
    )

    if not actual_model:
        raise RuntimeError(
            "No Gemini model configured."
        )

    # --------------------------------------------------------
    # Generate structured response
    # --------------------------------------------------------

    response = client.models.generate_content(
        model=actual_model,

        contents=prompt,

        config={
            "system_instruction": (
                COACH_SYSTEM_PROMPT
            ),

            "response_mime_type": (
                "application/json"
            ),

            "response_schema": (
                CoachAIResponse
            ),
        },
    )

    # --------------------------------------------------------
    # Parse Gemini response
    # --------------------------------------------------------

    if not response.text:
        raise RuntimeError(
            "Gemini returned an empty response."
        )

    try:

        ai_response = (
            CoachAIResponse
            .model_validate_json(
                response.text
            )
        )

    except Exception as exc:

        raise RuntimeError(
            "Gemini returned an invalid "
            "CoachAIResponse structure."
        ) from exc

    # --------------------------------------------------------
    # Token usage
    # --------------------------------------------------------

    usage = {
        "prompt_tokens": 0,
        "completion_tokens": 0,
        "total_tokens": 0,
    }

    metadata = getattr(
        response,
        "usage_metadata",
        None,
    )

    if metadata:

        usage["prompt_tokens"] = (
            getattr(
                metadata,
                "prompt_token_count",
                0,
            )
            or 0
        )

        usage["completion_tokens"] = (
            getattr(
                metadata,
                "candidates_token_count",
                0,
            )
            or 0
        )

        usage["total_tokens"] = (
            getattr(
                metadata,
                "total_token_count",
                0,
            )
            or 0
        )

    # --------------------------------------------------------
    # Latency
    # --------------------------------------------------------

    latency_ms = int(
        (
            time.perf_counter()
            - started
        )
        * 1000
    )

    return (
        ai_response,
        usage,
        latency_ms,
    )