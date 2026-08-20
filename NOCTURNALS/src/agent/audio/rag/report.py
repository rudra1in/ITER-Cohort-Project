from pathlib import Path
import json
from datetime import datetime, timezone


def save_report(
    audio_file_id: str,
    source_file: str,
    results: list[dict],
    output_dir: str = "./data/audio_reports",
) -> str:
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    review_events = [
        r for r in results
        if r.get("review_required") or r.get("processing_status") == "REVIEW_REQUIRED"
    ]

    report = {
        "audio_file_id": audio_file_id,
        "source_file": source_file,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total_chunks": len(results),
        "review_required_count": len(review_events),
        "labels": {},
        "results": results,
    }

    for row in results:
        label = row.get("assigned_label", "OTHER")
        report["labels"][label] = report["labels"].get(label, 0) + 1

    path = Path(output_dir) / f"{audio_file_id}_report.json"
    path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    return str(path)