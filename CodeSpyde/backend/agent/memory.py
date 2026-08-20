from __future__ import annotations

from typing import Any


def get_student_context(
    *,
    user_id: str,
    problem_id: str,
) -> dict[str, Any]:

    from services.student_history import (
        get_student_history,
        get_recurring_errors,
        get_skill_profile,
    )

    history = get_student_history(
        user_id=user_id,
        problem_id=problem_id,
        limit=10,
    )

    recurring_errors = get_recurring_errors(
        user_id=user_id,
        limit=10,
    )

    skill_profile = get_skill_profile(
        user_id=user_id,
    )

    return {
        "history": history or [],
        "recurring_errors": recurring_errors or [],
        "skill_profile": skill_profile or {},
    }