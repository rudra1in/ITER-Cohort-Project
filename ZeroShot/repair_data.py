"""
One-time repair script.

Why this exists
----------------
The original app.image_utils.ImageUtils.extract_timestamp() used a regex
without word boundaries, so on filenames like:

    WIN_20260812_10_51_04_Pro.jpg   (actual capture time: 10:51:04)

it matched the WRONG substring ("12_10_51" -> tail of the date + start of
the time) instead of the real time ("10_51_04"). Because almost every
photo from the same session shares the same date, this made nearly all
frames collapse onto a handful of near-identical fake timestamps.

That, in turn, silently broke event generation: EventEngine.finish_event()
computes duration as (end_time - start_time) in seconds and discards any
event shorter than MIN_EVENT_DURATION (default 3s). With corrupted
timestamps, computed durations were almost always 0-1 seconds even when
an event spanned 30+ frames, so every event got filtered out and the
events list stayed empty -- even though detection and tracking were
working fine.

app/image_utils.py has already been fixed (the regex now uses
(?<!\\d) / (?!\\d) so it can't start matching in the middle of a longer
digit run like a date). This script re-derives correct timestamps for
data that was already ingested with the OLD, buggy code, and rebuilds
the behavior_events table from it. Run it once after pulling the fix.

Usage:
    python repair_data.py
"""

import sqlite3
from datetime import datetime

from app.config import DATABASE_PATH
from app.image_utils import ImageUtils
from app.event_engine import EventEngine
from app.config import MIN_EVENT_DURATION, EVENT_GAP_SECONDS


def main():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row

    # -----------------------------------------------------
    # 0. Normalize any Windows-style backslash paths
    #    (from data originally ingested on Windows) so
    #    image lookups also work on Linux/Mac. This must
    #    run BEFORE the processed-image reconstruction
    #    step below, since Path() on Linux treats a
    #    backslashed string as one literal filename, not
    #    a multi-segment path.
    # -----------------------------------------------------
    frames_with_paths = connection.execute(
        "SELECT frame_id, image_path FROM frames"
    ).fetchall()

    updated_paths = 0

    for frame in frames_with_paths:
        old_path = frame["image_path"]

        if old_path and "\\" in old_path:
            new_path = old_path.replace("\\", "/")
            connection.execute(
                "UPDATE frames SET image_path = ? WHERE frame_id = ?",
                (new_path, frame["frame_id"])
            )
            updated_paths += 1

    print(f"Image paths normalized (backslash -> forward slash): {updated_paths}")
    connection.commit()

    # -----------------------------------------------------
    # -1. Reconstruct data/processed/ from data/raw/ where
    #     missing. Ingestion copies raw -> processed, but
    #     the processed copies were not included in the
    #     GitHub repo (only data/raw was), so image_path
    #     references files that don't exist on disk yet.
    # -----------------------------------------------------
    from pathlib import Path
    import shutil

    frames_for_files = connection.execute(
        "SELECT frame_id, test_id, candidate_id, filename, image_path FROM frames"
    ).fetchall()

    restored = 0
    missing_source = 0

    for frame in frames_for_files:
        dest = Path(frame["image_path"])

        if dest.exists():
            continue

        source = (
            Path("data/raw")
            / frame["test_id"]
            / (frame["candidate_id"] or "")
            / frame["filename"]
        )

        if not source.exists():
            missing_source += 1
            continue

        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, dest)
        restored += 1

    print(f"Processed images restored from data/raw: {restored}")
    if missing_source:
        print(f"WARNING: {missing_source} frames have no matching raw source file")

    # -----------------------------------------------------
    # 1. Recompute frame timestamps from filenames
    # -----------------------------------------------------
    frames = connection.execute(
        "SELECT frame_id, filename, timestamp FROM frames"
    ).fetchall()

    updated_frames = 0
    frame_new_timestamp = {}

    for frame in frames:
        new_ts = ImageUtils.extract_timestamp(frame["filename"])
        frame_new_timestamp[frame["frame_id"]] = new_ts

        if new_ts and new_ts != frame["timestamp"]:
            connection.execute(
                "UPDATE frames SET timestamp = ? WHERE frame_id = ?",
                (new_ts, frame["frame_id"])
            )
            updated_frames += 1

    print(f"Frames updated: {updated_frames} / {len(frames)}")

    # -----------------------------------------------------
    # 2. Recompute behavior_observations timestamps
    #    (they were copied from the frame at analysis time)
    # -----------------------------------------------------
    observations = connection.execute(
        "SELECT observation_id, frame_id, timestamp FROM behavior_observations"
    ).fetchall()

    updated_observations = 0

    for obs in observations:
        new_ts = frame_new_timestamp.get(obs["frame_id"])

        if new_ts and new_ts != obs["timestamp"]:
            connection.execute(
                "UPDATE behavior_observations SET timestamp = ? WHERE observation_id = ?",
                (new_ts, obs["observation_id"])
            )
            updated_observations += 1

    print(f"Behavior observations updated: {updated_observations} / {len(observations)}")

    connection.commit()

    # -----------------------------------------------------
    # 3. Rebuild behavior_events per test using corrected timestamps
    # -----------------------------------------------------
    test_ids = [
        row["test_id"]
        for row in connection.execute("SELECT test_id FROM tests").fetchall()
    ]

    engine = EventEngine(
        min_duration=MIN_EVENT_DURATION,
        gap_seconds=EVENT_GAP_SECONDS
    )

    total_events = 0

    for test_id in test_ids:

        # Wipe old (bogus / empty) events for this test.
        connection.execute(
            "DELETE FROM behavior_events WHERE test_id = ?",
            (test_id,)
        )
        connection.execute(
            "DELETE FROM event_fts WHERE candidate_id IN "
            "(SELECT DISTINCT candidate_id FROM behavior_observations WHERE test_id = ?)",
            (test_id,)
        )

        rows = connection.execute(
            "SELECT * FROM behavior_observations WHERE test_id = ? "
            "ORDER BY track_id, timestamp",
            (test_id,)
        ).fetchall()

        observations = [dict(row) for row in rows]

        events = engine.build_events(observations)

        for event in events:
            connection.execute(
                """
                INSERT OR REPLACE INTO behavior_events
                (
                    event_id, test_id, candidate_id, track_id, event_type,
                    start_time, end_time, duration, confidence,
                    description, evidence_json, created_at
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    event["event_id"], test_id, event["candidate_id"],
                    event["track_id"], event["event_type"],
                    event["start_time"], event["end_time"],
                    event["duration"], event["confidence"],
                    event["description"], event["evidence_json"],
                    datetime.utcnow().isoformat()
                )
            )
            connection.execute(
                """
                INSERT INTO event_fts
                (event_id, candidate_id, event_type, description, start_time, end_time)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    event["event_id"], event["candidate_id"], event["event_type"],
                    event["description"], event["start_time"], event["end_time"]
                )
            )

        print(f"Test {test_id}: rebuilt {len(events)} events")
        total_events += len(events)

    connection.commit()
    connection.close()

    print(f"\nDone. Total events rebuilt: {total_events}")
    print("Note: if you use the RAG/chat feature, re-run POST /tests/{test_id}/index "
          "so the vector store picks up the corrected events.")


if __name__ == "__main__":
    main()
