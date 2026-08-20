from typing import TypedDict


class VerificationState(TypedDict, total=False):
    # -----------------------------
    # INPUTS
    # -----------------------------

    id_image_path: str
    video_path: str

    # -----------------------------
    # VIDEO PROCESSING
    # -----------------------------

    frame_paths: list[str]

    # -----------------------------
    # VISION AGENT OUTPUT
    # -----------------------------

    identity_data: dict
    video_identity_data: dict

    # -----------------------------
    # FACE EMBEDDINGS
    # -----------------------------

    id_face_embedding: list[float]
    video_face_embeddings: list[list[float]]

    # -----------------------------
    # FACE MATCHING
    # -----------------------------

    face_similarities: list[float]
    face_similarity: float

    # -----------------------------
    # VERIFICATION
    # -----------------------------

    verification_result: str
    verification_reason: str

    # -----------------------------
    # LEDGER
    # -----------------------------

    ledger_entry: dict

    chroma_match_id: str
    chroma_distance: float
    chroma_identity_id: str
    chroma_match_id: str
    chroma_distance: float

    # -----------------------------
    # ERRORS
    # -----------------------------

    errors: list[str]