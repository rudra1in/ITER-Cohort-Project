from datetime import datetime
from pathlib import Path
import json

from src.state import VerificationState


LEDGER_PATH = Path(
    "data/ledger/verification_ledger.jsonl"
)


def ledger_agent(
    state: VerificationState,
) -> VerificationState:
    """
    Record the final face-verification result
    in an append-only JSONL ledger.
    """

    ledger_entry = {
        "timestamp": datetime.now().isoformat(),

        "id_image_path": state.get(
            "id_image_path"
        ),

        "video_path": state.get(
            "video_path"
        ),

        "verification_result": state.get(
            "verification_result"
        ),

        "face_similarity": state.get(
            "face_similarity"
        ),

        "face_similarities": state.get(
            "face_similarities",
            []
        ),

        "chroma_match_id": state.get(
            "chroma_match_id"
        ),

        "chroma_distance": state.get(
            "chroma_distance"
        ),

        "verification_reason": state.get(
            "verification_reason"
        ),
    }

    try:

        LEDGER_PATH.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with LEDGER_PATH.open(
            "a",
            encoding="utf-8",
        ) as file:

            file.write(
                json.dumps(
                    ledger_entry
                )
                + "\n"
            )

        return {
            **state,
            "ledger_entry": ledger_entry,
        }

    except Exception as exc:

        return {
            **state,
            "errors": [
                *state.get("errors", []),
                f"Ledger write failed: {exc}",
            ],
        }