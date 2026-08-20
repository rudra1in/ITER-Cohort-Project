from src.state import VerificationState


def id_agent(state: VerificationState) -> VerificationState:
    """
    Validate that an ID image has been provided.
    Actual visual analysis is handled by vision_agent.
    """

    id_image_path = state.get("id_image_path")

    if not id_image_path:
        return {
            **state,
            "errors": [
                *state.get("errors", []),
                "ID image path is missing.",
            ],
        }

    return state