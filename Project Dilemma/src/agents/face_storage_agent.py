from src.state import VerificationState
from src.vectorstore.chroma import store_identity


def face_storage_agent(
    state: VerificationState,
) -> VerificationState:

    id_embedding = state.get(
        "id_face_embedding"
    )

    errors = list(
        state.get("errors", [])
    )

    if not id_embedding:

        errors.append(
            "Cannot store face: "
            "ID face embedding is missing."
        )

        return {
            **state,
            "errors": errors,
        }

    try:

        identity_id = "current_identity"

        identity_data = state.get(
            "identity_data",
            {},
        )

        metadata = {
            "name": identity_data.get(
                "name",
                "Unknown",
            ),
            "type": identity_data.get(
                "document_type",
                "identity_document",
            ),
        }

        store_identity(
            identity_id=identity_id,
            face_embedding=id_embedding,
            metadata=metadata,
        )

        return {
            **state,
            "chroma_identity_id": identity_id,
        }

    except Exception as exc:

        errors.append(
            f"Face storage failed: {exc}"
        )

        return {
            **state,
            "errors": errors,
        }