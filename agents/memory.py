
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
PROGRESS_FILE = BASE_DIR / "progress.json"

DEFAULT_PROGRESS = {
    "score_history": [],
    "avg_score": 0.0,
    "solved_ids": [],
    "submissions": 0,
}


def load_progress():
    if not PROGRESS_FILE.exists():
        return DEFAULT_PROGRESS.copy()

    try:
        data = json.loads(PROGRESS_FILE.read_text(encoding="utf-8"))
        scores = []
        for value in data.get("score_history", []):
            try:
                scores.append(max(0, min(10, int(float(value)))))
            except Exception:
                pass

        solved_ids = data.get("solved_ids", [])
        if not isinstance(solved_ids, list):
            solved_ids = []

        avg = sum(scores) / len(scores) if scores else 0.0

        return {
            "score_history": scores,
            "avg_score": avg,
            "solved_ids": solved_ids,
            "submissions": len(scores),
        }
    except Exception:
        return DEFAULT_PROGRESS.copy()


def save_progress(score_history, avg_score, solved_ids=None):
    clean_scores = []
    for value in score_history:
        try:
            clean_scores.append(max(0, min(10, int(float(value)))))
        except Exception:
            pass

    data = {
        "score_history": clean_scores,
        "avg_score": (
            sum(clean_scores) / len(clean_scores)
            if clean_scores else 0.0
        ),
        "solved_ids": solved_ids or [],
        "submissions": len(clean_scores),
    }

    PROGRESS_FILE.write_text(
        json.dumps(data, indent=2),
        encoding="utf-8",
    )
