from __future__ import annotations

from typing import Literal

from agent.state import DSAAgentState


def after_analysis(
    state: DSAAgentState,
) -> Literal[
    "coach",
    "execute",
]:

    if state.get(
        "has_syntax_error",
        False,
    ):
        return "coach"

    return "execute"


def after_execution(
    state: DSAAgentState,
) -> Literal[
    "success",
    "retrieve",
    "coach",
]:

    if state.get(
        "solved",
        False,
    ):
        return "success"

    if state.get(
        "timed_out",
        False,
    ):
        return "coach"

    return "retrieve"