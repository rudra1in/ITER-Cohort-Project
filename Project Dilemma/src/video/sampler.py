import cv2
from pathlib import Path


def sample_frames(
    video_path: str,
    output_dir: str = "data/frames",
    target_fps: int = 10,
) -> list[str]:
    """
    Sample frames from a video and save them to disk.

    Returns:
        List of paths to sampled frame images.
    """

    if target_fps <= 0:
        raise ValueError("target_fps must be greater than 0")

    video_path = Path(video_path)
    output_dir = Path(output_dir)

    output_dir.mkdir(parents=True, exist_ok=True)

    cap = cv2.VideoCapture(str(video_path))

    if not cap.isOpened():
        raise FileNotFoundError(
            f"Could not open video: {video_path}"
        )

    original_fps = cap.get(cv2.CAP_PROP_FPS)

    if original_fps <= 0:
        cap.release()
        raise ValueError("Could not determine video FPS")

    frame_interval = max(
        int(round(original_fps / target_fps)),
        1,
    )

    frame_paths = []
    frame_index = 0
    sample_index = 0

    while True:
        success, frame = cap.read()

        if not success:
            break

        if frame_index % frame_interval == 0:

            frame_path = output_dir / f"frame_{sample_index:04d}.jpg"

            cv2.imwrite(
                str(frame_path),
                frame,
            )

            frame_paths.append(str(frame_path))

            sample_index += 1

        frame_index += 1

    cap.release()

    return frame_paths