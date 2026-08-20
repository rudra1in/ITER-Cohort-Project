from src.state import VerificationState
from src.video.sampler import sample_frames


def video_agent(state: VerificationState) -> VerificationState:
    """
    Video processing node for the LangGraph workflow.

    Takes the uploaded video path from the shared state,
    samples representative frames, saves them to disk,
    and places their paths back into the shared state.
    """

    video_path = state.get("video_path")

    if not video_path:
        return {
            **state,
            "errors": [
                *state.get("errors", []),
                "Video path is missing.",
            ],
        }

    try:
        frame_paths = sample_frames(
            video_path=video_path,
            output_dir="data/frames",
            target_fps=10,
        )

        if not frame_paths:
            return {
                **state,
                "errors": [
                    *state.get("errors", []),
                    "No frames could be sampled from the video.",
                ],
            }

        return {
            **state,
            "frame_paths": frame_paths,
        }

    except Exception as exc:
        return {
            **state,
            "errors": [
                *state.get("errors", []),
                f"Video processing failed: {exc}",
            ],
        }