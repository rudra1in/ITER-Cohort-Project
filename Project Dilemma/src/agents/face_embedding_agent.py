from pathlib import Path

import cv2
import numpy as np
from insightface.app import FaceAnalysis

from src.state import VerificationState


face_app = FaceAnalysis(
    name="buffalo_l",
    providers=["CPUExecutionProvider"],
)

face_app.prepare(
    ctx_id=0,
    det_size=(640, 640),
)


def get_face_embedding_from_image(
    image: np.ndarray,
) -> list[float]:

    faces = face_app.get(image)

    if not faces:
        raise ValueError(
            "No face detected."
        )

    # Largest face = primary subject
    face = max(
        faces,
        key=lambda f: (
            (f.bbox[2] - f.bbox[0])
            * (f.bbox[3] - f.bbox[1])
        ),
    )

    embedding = face.embedding.astype(
        np.float32
    )

    norm = np.linalg.norm(embedding)

    if norm == 0:
        raise ValueError(
            "Invalid face embedding."
        )

    embedding /= norm

    return embedding.tolist()


def get_face_embedding(
    image_path: str,
) -> list[float]:
    """
    Get a face embedding from an image
    without rotation handling.
    """

    image = cv2.imread(
        str(Path(image_path))
    )

    if image is None:
        raise ValueError(
            f"Could not read image: {image_path}"
        )

    return get_face_embedding_from_image(
        image
    )


def cosine_similarity(
    a: list[float],
    b: list[float],
) -> float:

    a = np.asarray(
        a,
        dtype=np.float32,
    )

    b = np.asarray(
        b,
        dtype=np.float32,
    )

    denominator = (
        np.linalg.norm(a)
        * np.linalg.norm(b)
    )

    if denominator == 0:
        return 0.0

    return float(
        np.dot(a, b) / denominator
    )


def get_best_oriented_id_embedding(
    image_path: str,
    video_embeddings: list[list[float]],
) -> list[float]:

    image = cv2.imread(
        str(Path(image_path))
    )

    if image is None:
        raise ValueError(
            f"Could not read image: {image_path}"
        )

    # Try all four possible orientations.
    orientations = [
        image,
        cv2.rotate(
            image,
            cv2.ROTATE_90_CLOCKWISE,
        ),
        cv2.rotate(
            image,
            cv2.ROTATE_180,
        ),
        cv2.rotate(
            image,
            cv2.ROTATE_90_COUNTERCLOCKWISE,
        ),
    ]

    candidates = []

    for orientation_index, oriented_image in enumerate(
        orientations
    ):

        try:

            embedding = (
                get_face_embedding_from_image(
                    oriented_image
                )
            )

            if video_embeddings:

                similarities = [
                    cosine_similarity(
                        embedding,
                        video_embedding,
                    )
                    for video_embedding
                    in video_embeddings
                ]

                score = float(
                    np.mean(similarities)
                )

            else:
                score = 0.0

            candidates.append(
                (
                    score,
                    orientation_index,
                    embedding,
                )
            )

        except Exception:
            continue

    if not candidates:
        raise ValueError(
            "Could not detect a face in any "
            "ID image orientation."
        )

    # Choose orientation with strongest
    # agreement with the video faces.
    best = max(
        candidates,
        key=lambda item: item[0],
    )

    return best[2]


def face_embedding_agent(
    state: VerificationState,
) -> VerificationState:

    errors = list(
        state.get("errors", [])
    )

    result = {
        **state,
        "errors": errors,
    }

    # -----------------------------------------
    # VIDEO EMBEDDINGS FIRST
    # -----------------------------------------

    frame_paths = state.get(
        "frame_paths",
        []
    )

    video_embeddings = []

    if frame_paths:

        step = max(
            1,
            len(frame_paths) // 10,
        )

        selected_frames = frame_paths[
            ::step
        ][:10]

        for frame_path in selected_frames:

            try:

                embedding = get_face_embedding(
                    frame_path
                )

                video_embeddings.append(
                    embedding
                )

            except Exception:
                continue

        if video_embeddings:

            result[
                "video_face_embeddings"
            ] = video_embeddings

        else:

            errors.append(
                "No face detected in video frames."
            )

    else:

        errors.append(
            "No video frames available."
        )

    # -----------------------------------------
    # ID EMBEDDING
    # -----------------------------------------

    id_image_path = state.get(
        "id_image_path"
    )

    if id_image_path:

        try:

            # Use video embeddings to determine
            # the best orientation of the ID.
            id_embedding = (
                get_best_oriented_id_embedding(
                    id_image_path,
                    video_embeddings,
                )
            )

            result[
                "id_face_embedding"
            ] = id_embedding

        except Exception as exc:

            errors.append(
                f"ID face embedding failed: {exc}"
            )

    else:

        errors.append(
            "ID image path is missing."
        )

    result["errors"] = errors

    return result