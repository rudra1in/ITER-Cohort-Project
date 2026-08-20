from app.agents.coach_agent import run_coach_agent
from app.agents.code_agent import run_code_agent


def classify_request(
    message: str,
    mode: str | None = None,
) -> str:
    """
    Decide which agent should handle the request.
    """

    message_lower = message.lower()

    # ==========================================================
    # CODE-RELATED KEYWORDS
    # ==========================================================

    code_keywords = [
        "my code",
        "my solution",
        "why does my code",
        "debug",
        "bug",
        "error",
        "wrong answer",
        "runtime error",
        "compile error",
        "time complexity of my code",
        "space complexity of my code",
    ]

    # Code-related requests go to the Code Agent.
    for keyword in code_keywords:

        if keyword in message_lower:
            return "code"

    # ==========================================================
    # DEFAULT → COACH AGENT
    # ==========================================================

    return "coach"


def run_orchestrator(
    message: str,
    mode: str | None = None,
    language: str = "java",
    code: str = "",
    problem: dict | None = None,
    conversation: list[dict] | None = None,
):
    """
    Main entry point for the multi-agent system.

    The orchestrator decides whether the request should
    be handled by the Coach Agent or Code Agent.
    """

    agent = classify_request(
        message=message,
        mode=mode,
    )

    # ==========================================================
    # COACH AGENT
    # ==========================================================

    if agent == "coach":

        return run_coach_agent(
            query=message,
            mode=mode or "explain",
            code=code,
            problem=problem,
            conversation=conversation or [],
        )

    # ==========================================================
    # CODE AGENT
    # ==========================================================

    if agent == "code":

        return run_code_agent(
            query=message,
            mode=mode or "review",
            language=language,
            code=code,
            problem=problem,
            conversation=conversation or [],
        )

    # ==========================================================
    # UNKNOWN AGENT
    # ==========================================================

    raise ValueError(
        f"Unknown agent: {agent}"
    )