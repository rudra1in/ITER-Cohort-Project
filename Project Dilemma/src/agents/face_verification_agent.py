import numpy as np

from src.state import VerificationState
from src.vectorstore.chroma import search_identity


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


def face_verification_agent(
    state: VerificationState,
) -> VerificationState:

    id_embedding = state.get(
        "id_face_embedding"
    )

    video_embeddings = state.get(
        "video_face_embeddings",
        []
    )

    errors = list(
        state.get("errors", [])
    )

    if not id_embedding:

        errors.append(
            "ID face embedding is missing."
        )

        return {
            **state,
            "errors": errors,
        }

    if not video_embeddings:

        errors.append(
            "Video face embeddings are missing."
        )

        return {
            **state,
            "errors": errors,
        }

    try:

        # -----------------------------------------
        # Query Chroma using the ID embedding
        # -----------------------------------------

        chroma_result = search_identity(
            id_embedding,
            n_results=1,
        )

        matched_ids = chroma_result.get(
            "ids",
            [[]],
        )

        matched_distances = chroma_result.get(
            "distances",
            [[]],
        )

        matched_identity = (
            matched_ids[0][0]
            if matched_ids and matched_ids[0]
            else None
        )

        chroma_distance = (
            matched_distances[0][0]
            if matched_distances
            and matched_distances[0]
            else None
        )

        # -----------------------------------------
        # Compare each video face with ID face
        # -----------------------------------------

        similarities = []

        for video_embedding in video_embeddings:

            similarity = cosine_similarity(
                id_embedding,
                video_embedding,
            )

            similarities.append(
                similarity
            )

        if not similarities:

            errors.append(
                "No face similarities calculated."
            )

            return {
                **state,
                "errors": errors,
            }

        # -----------------------------------------
        # Aggregate video evidence
        # -----------------------------------------

        mean_similarity = float(
            np.mean(similarities)
        )

        max_similarity = float(
            np.max(similarities)
        )

        min_similarity = float(
            np.min(similarities)
        )

        # -----------------------------------------
        # Prototype decision
        # -----------------------------------------

        threshold = 0.40

        verified = (
            mean_similarity >= threshold
        )

        result = (
            "VERIFIED"
            if verified
            else "NOT VERIFIED"
        )

        return {
            **state,

            "face_similarities": similarities,

            "face_similarity": mean_similarity,

            "verification_result": result,

            "verification_reason": (
                f"Mean face similarity: "
                f"{mean_similarity:.4f}; "
                f"max: {max_similarity:.4f}; "
                f"min: {min_similarity:.4f}; "
                f"threshold: {threshold:.2f}."
            ),

            "chroma_match_id": (
                matched_identity
            ),

            "chroma_distance": (
                chroma_distance
            ),
        }

    except Exception as exc:

        errors.append(
            f"Face verification failed: {exc}"
        )

        return {
            **state,
            "errors": errors,
        }