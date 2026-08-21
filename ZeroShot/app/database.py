import sqlite3
import json
from datetime import datetime
from app.config import DATABASE_PATH


class Database:

    def __init__(
        self
    ):

        self.path = DATABASE_PATH

        self.initialize()

     
    # CONNECTION
     

    def connect(
        self
    ):

        connection = sqlite3.connect(
            self.path,
            check_same_thread=False
        )

        connection.row_factory = (
            sqlite3.Row
        )

        return connection

     
    # INITIALIZE
     

    def initialize(
        self
    ):

        connection = self.connect()

        connection.executescript(
            """

            CREATE TABLE IF NOT EXISTS tests (

                test_id TEXT PRIMARY KEY,

                created_at TEXT NOT NULL

            );


            CREATE TABLE IF NOT EXISTS frames (

                frame_id TEXT PRIMARY KEY,

                test_id TEXT NOT NULL,

                candidate_id TEXT,

                filename TEXT NOT NULL,

                image_path TEXT NOT NULL,

                timestamp TEXT,

                sha256 TEXT,

                phash TEXT,

                width INTEGER,

                height INTEGER,

                file_size INTEGER,

                is_exact_duplicate INTEGER DEFAULT 0,

                duplicate_of TEXT,

                is_near_duplicate INTEGER DEFAULT 0,

                near_duplicate_of TEXT,

                is_change_point INTEGER DEFAULT 0,

                change_score REAL DEFAULT 0,

                yolo_processed INTEGER DEFAULT 0,

                created_at TEXT NOT NULL

            );


            CREATE TABLE IF NOT EXISTS detections (

                detection_id INTEGER PRIMARY KEY AUTOINCREMENT,

                frame_id TEXT NOT NULL,

                class_id INTEGER,

                class_name TEXT,

                confidence REAL,

                x1 REAL,

                y1 REAL,

                x2 REAL,

                y2 REAL,

                created_at TEXT NOT NULL

            );


            CREATE TABLE IF NOT EXISTS behavior_observations (

                observation_id INTEGER PRIMARY KEY AUTOINCREMENT,

                frame_id TEXT NOT NULL,

                test_id TEXT NOT NULL,

                candidate_id TEXT,

                track_id INTEGER,

                timestamp TEXT,

                head_direction TEXT,

                head_yaw REAL,

                head_pitch REAL,

                body_direction TEXT,

                movement TEXT,

                movement_score REAL,

                phone_visible INTEGER DEFAULT 0,

                paper_visible INTEGER DEFAULT 0,

                person_count INTEGER DEFAULT 0,

                feature_json TEXT,

                created_at TEXT NOT NULL

            );


            CREATE TABLE IF NOT EXISTS behavior_events (

                event_id TEXT PRIMARY KEY,

                test_id TEXT NOT NULL,

                candidate_id TEXT,

                track_id INTEGER,

                event_type TEXT,

                start_time TEXT,

                end_time TEXT,

                duration REAL,

                confidence REAL,

                description TEXT,

                evidence_json TEXT,

                created_at TEXT NOT NULL

            );


            CREATE TABLE IF NOT EXISTS chat_sessions (

                session_id TEXT PRIMARY KEY,

                test_id TEXT NOT NULL,

                created_at TEXT NOT NULL

            );


            CREATE TABLE IF NOT EXISTS chat_messages (

                message_id INTEGER PRIMARY KEY AUTOINCREMENT,

                session_id TEXT NOT NULL,

                role TEXT NOT NULL,

                content TEXT NOT NULL,

                created_at TEXT NOT NULL

            );


            CREATE VIRTUAL TABLE IF NOT EXISTS event_fts
            USING fts5(

                event_id UNINDEXED,

                candidate_id,

                event_type,

                description,

                start_time,

                end_time

            );


            CREATE INDEX IF NOT EXISTS idx_frames_test
            ON frames(test_id);


            CREATE INDEX IF NOT EXISTS idx_observations_test
            ON behavior_observations(test_id);


            CREATE INDEX IF NOT EXISTS idx_events_test
            ON behavior_events(test_id);


            CREATE INDEX IF NOT EXISTS idx_events_candidate
            ON behavior_events(candidate_id);

            """
        )

        connection.commit()

        connection.close()

        self.migrate()

     
    # MIGRATE
     

    def migrate(
        self
    ):

        connection = self.connect()

        existing_columns = [
            row["name"]
            for row in connection.execute(
                "PRAGMA table_info(behavior_events)"
            ).fetchall()
        ]

        migrations = [
            ("cluster_id", "INTEGER"),
            ("cluster_label", "TEXT"),
            ("is_suspicious", "INTEGER DEFAULT 0"),
        ]

        for column_name, column_type in migrations:

            if column_name not in existing_columns:

                connection.execute(
                    f"ALTER TABLE behavior_events "
                    f"ADD COLUMN {column_name} {column_type}"
                )

        existing_obs_columns = [
            row["name"]
            for row in connection.execute(
                "PRAGMA table_info(behavior_observations)"
            ).fetchall()
        ]

        if "escalated_by" not in existing_obs_columns:

            connection.execute(
                "ALTER TABLE behavior_observations "
                "ADD COLUMN escalated_by TEXT"
            )

        connection.commit()

        connection.close()

     
    # TEST
     

    def create_test(
        self,
        test_id
    ):

        connection = self.connect()

        connection.execute(
            """
            INSERT OR IGNORE INTO tests
            (
                test_id,
                created_at
            )
            VALUES (?, ?)
            """,
            (
                test_id,
                datetime.utcnow().isoformat()
            )
        )

        connection.commit()

        connection.close()

     
    # FRAME
     

    def insert_frame(
        self,
        frame
    ):

        connection = self.connect()

        connection.execute(
            """
            INSERT OR REPLACE INTO frames
            (
                frame_id,
                test_id,
                candidate_id,
                filename,
                image_path,
                timestamp,
                sha256,
                phash,
                width,
                height,
                file_size,
                is_exact_duplicate,
                duplicate_of,
                is_near_duplicate,
                near_duplicate_of,
                is_change_point,
                change_score,
                yolo_processed,
                created_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                frame["frame_id"],
                frame["test_id"],
                frame["candidate_id"],
                frame["filename"],
                frame["image_path"],
                frame["timestamp"],
                frame["sha256"],
                frame["phash"],
                frame["width"],
                frame["height"],
                frame["file_size"],
                int(frame["is_exact_duplicate"]),
                frame["duplicate_of"],
                int(frame["is_near_duplicate"]),
                frame["near_duplicate_of"],
                int(frame["is_change_point"]),
                frame["change_score"],
                int(frame["yolo_processed"]),
                datetime.utcnow().isoformat()
            )
        )

        connection.commit()

        connection.close()

     
    # DETECTION
     

    def insert_detection(
        self,
        frame_id,
        detection
    ):

        connection = self.connect()

        connection.execute(
            """
            INSERT INTO detections
            (
                frame_id,
                class_id,
                class_name,
                confidence,
                x1,
                y1,
                x2,
                y2,
                created_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                frame_id,
                detection["class_id"],
                detection["class_name"],
                detection["confidence"],
                detection["x1"],
                detection["y1"],
                detection["x2"],
                detection["y2"],
                datetime.utcnow().isoformat()
            )
        )

        connection.commit()

        connection.close()

     
    # BEHAVIOR OBSERVATION
     

    def insert_behavior_observation(
        self,
        observation
    ):

        connection = self.connect()

        connection.execute(
            """
            INSERT INTO behavior_observations
            (
                frame_id,
                test_id,
                candidate_id,
                track_id,
                timestamp,
                head_direction,
                head_yaw,
                head_pitch,
                body_direction,
                movement,
                movement_score,
                phone_visible,
                paper_visible,
                person_count,
                feature_json,
                escalated_by,
                created_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                observation["frame_id"],
                observation["test_id"],
                observation["candidate_id"],
                observation["track_id"],
                observation["timestamp"],
                observation["head_direction"],
                observation["head_yaw"],
                observation["head_pitch"],
                observation["body_direction"],
                observation["movement"],
                observation["movement_score"],
                int(observation["phone_visible"]),
                int(observation["paper_visible"]),
                observation["person_count"],
                observation["feature_json"],
                observation.get("escalated_by"),
                datetime.utcnow().isoformat()
            )
        )

        connection.commit()

        connection.close()

     
    # EVENT
     

    def insert_behavior_event(
        self,
        event
    ):

        connection = self.connect()

        connection.execute(
            """
            INSERT OR REPLACE INTO behavior_events
            (
                event_id,
                test_id,
                candidate_id,
                track_id,
                event_type,
                start_time,
                end_time,
                duration,
                confidence,
                description,
                evidence_json,
                created_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                event["event_id"],
                event["test_id"],
                event["candidate_id"],
                event["track_id"],
                event["event_type"],
                event["start_time"],
                event["end_time"],
                event["duration"],
                event["confidence"],
                event["description"],
                event["evidence_json"],
                datetime.utcnow().isoformat()
            )
        )

        connection.execute(
            """
            DELETE FROM event_fts
            WHERE event_id = ?
            """,
            (
                event["event_id"],
            )
        )

        connection.execute(
            """
            INSERT INTO event_fts
            (
                event_id,
                candidate_id,
                event_type,
                description,
                start_time,
                end_time
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                event["event_id"],
                event["candidate_id"],
                event["event_type"],
                event["description"],
                event["start_time"],
                event["end_time"]
            )
        )

        connection.commit()

        connection.close()

     
    # GET EVENTS
     

    def get_events(
        self,
        test_id,
        suspicious_only=False
    ):

        connection = self.connect()

        if suspicious_only:

            rows = connection.execute(
                """
                SELECT *
                FROM behavior_events
                WHERE test_id = ?
                AND is_suspicious = 1
                ORDER BY start_time
                """,
                (
                    test_id,
                )
            ).fetchall()

        else:

            rows = connection.execute(
                """
                SELECT *
                FROM behavior_events
                WHERE test_id = ?
                ORDER BY start_time
                """,
                (
                    test_id,
                )
            ).fetchall()

        connection.close()

        return [
            dict(row)
            for row in rows
        ]

     
    # UPDATE EVENT CLUSTER
     

    def update_event_cluster(
        self,
        event_id,
        cluster_id,
        cluster_label,
        is_suspicious
    ):

        connection = self.connect()

        connection.execute(
            """
            UPDATE behavior_events
            SET cluster_id = ?,
                cluster_label = ?,
                is_suspicious = ?
            WHERE event_id = ?
            """,
            (
                cluster_id,
                cluster_label,
                1 if is_suspicious else 0,
                event_id
            )
        )

        connection.commit()

        connection.close()

     
    # GET EVENT
     

    def get_event(
        self,
        event_id
    ):

        connection = self.connect()

        row = connection.execute(
            """
            SELECT *
            FROM behavior_events
            WHERE event_id = ?
            """,
            (
                event_id,
            )
        ).fetchone()

        connection.close()

        if row is None:

            return None

        return dict(row)

     
    # KEYWORD SEARCH
     

    def keyword_search_events(
        self,
        test_id,
        query,
        limit=8
    ):

        connection = self.connect()

        # SQLite FTS can interpret punctuation/operators  in user input. 
        #We convert the query into simple tokens for safer prototype searching.

        tokens = [

            token.strip(
                "\"'.,:;!?()[]{}"
            )

            for token in query.split()

            if token.strip(
                "\"'.,:;!?()[]{}"
            )
        ]

        tokens = [
            token
            for token in tokens
            if token
        ]

        if not tokens:

            connection.close()

            return []

        fts_query = " OR ".join(
            f'"{token}"'
            for token in tokens
        )

        rows = connection.execute(
            """
            SELECT
                e.*,
                bm25(event_fts) AS bm25_score

            FROM event_fts f

            JOIN behavior_events e
            ON f.event_id = e.event_id

            WHERE event_fts MATCH ?

            AND e.test_id = ?

            ORDER BY bm25(event_fts)

            LIMIT ?
            """,
            (
                fts_query,
                test_id,
                limit
            )
        ).fetchall()

        connection.close()

        return [
            dict(row)
            for row in rows
        ]

     
    # CHAT SESSION
     

    def create_chat_session(
        self,
        session_id,
        test_id
    ):

        connection = self.connect()

        connection.execute(
            """
            INSERT OR IGNORE INTO chat_sessions
            (
                session_id,
                test_id,
                created_at
            )
            VALUES (?, ?, ?)
            """,
            (
                session_id,
                test_id,
                datetime.utcnow().isoformat()
            )
        )

        connection.commit()

        connection.close()

     
    # SAVE MESSAGE
     

    def save_message(
        self,
        session_id,
        role,
        content
    ):

        connection = self.connect()

        connection.execute(
            """
            INSERT INTO chat_messages
            (
                session_id,
                role,
                content,
                created_at
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                session_id,
                role,
                content,
                datetime.utcnow().isoformat()
            )
        )

        connection.commit()

        connection.close()

     
    # GET MEMORY
     

    def get_messages(
        self,
        session_id,
        limit=8
    ):

        connection = self.connect()

        rows = connection.execute(
            """
            SELECT role, content, created_at
            FROM chat_messages
            WHERE session_id = ?
            ORDER BY message_id DESC
            LIMIT ?
            """,
            (
                session_id,
                limit
            )
        ).fetchall()

        connection.close()

        rows = list(
            reversed(rows)
        )

        return [
            dict(row)
            for row in rows
        ]

     
    # SUMMARY
     

    def get_test_summary(
        self,
        test_id
    ):

        connection = self.connect()

        frame_count = connection.execute(
            """
            SELECT COUNT(*) AS count
            FROM frames
            WHERE test_id = ?
            """,
            (
                test_id,
            )
        ).fetchone()["count"]

        detection_count = connection.execute(
            """
            SELECT COUNT(*) AS count

            FROM detections d

            JOIN frames f
            ON d.frame_id = f.frame_id

            WHERE f.test_id = ?
            """,
            (
                test_id,
            )
        ).fetchone()["count"]

        observation_count = connection.execute(
            """
            SELECT COUNT(*) AS count
            FROM behavior_observations
            WHERE test_id = ?
            """,
            (
                test_id,
            )
        ).fetchone()["count"]

        event_count = connection.execute(
            """
            SELECT COUNT(*) AS count
            FROM behavior_events
            WHERE test_id = ?
            """,
            (
                test_id,
            )
        ).fetchone()["count"]

        connection.close()

        return {

            "test_id":
                test_id,

            "frames":
                frame_count,

            "detections":
                detection_count,

            "behavior_observations":
                observation_count,

            "behavior_events":
                event_count
        }

     
    # GET FRAMES
     

    def get_frames(
        self,
        test_id
    ):

        connection = self.connect()

        rows = connection.execute(
            """
            SELECT *
            FROM frames
            WHERE test_id = ?
            ORDER BY timestamp
            """,
            (
                test_id,
            )
        ).fetchall()

        connection.close()

        return [
            dict(row)
            for row in rows
        ]
     
    # GET CANDIDATES
     

    def get_candidates(
        self,
        test_id
    ):

        connection = self.connect()

        rows = connection.execute(
            """
            SELECT DISTINCT candidate_id
            FROM behavior_events
            WHERE test_id = ?
            ORDER BY candidate_id
            """,
            (
                test_id,
            )
        ).fetchall()

        connection.close()

        return [
            row["candidate_id"]
            for row in rows
        ]

     
    # CANDIDATE TIMELINE
     

    def get_candidate_timeline(
        self,
        test_id,
        candidate_id
    ):
        """Return all events for a specific candidate, sorted by time."""

        connection = self.connect()

        rows = connection.execute(
            """
            SELECT *
            FROM behavior_events
            WHERE test_id = ?
            AND candidate_id = ?
            ORDER BY start_time
            """,
            (
                test_id,
                candidate_id
            )
        ).fetchall()

        connection.close()

        return [
            dict(row)
            for row in rows
        ]

     
    # SUSPICIOUS EVENTS
     

    def get_suspicious_events(
        self,
        test_id
    ):
        """Return all events flagged as suspicious for a test."""

        connection = self.connect()

        rows = connection.execute(
            """
            SELECT *
            FROM behavior_events
            WHERE test_id = ?
            AND is_suspicious = 1
            ORDER BY candidate_id, start_time
            """,
            (
                test_id,
            )
        ).fetchall()

        connection.close()

        return [
            dict(row)
            for row in rows
        ]

     
    # TEST STATISTICS
     

    def get_test_statistics(
        self,
        test_id
    ):
        """
        Return per-candidate, per-event-type aggregate statistics.

        Returns a list of rows: {
            candidate_id, event_type,
            count, total_duration, avg_confidence,
            suspicious_count
        }
        """

        connection = self.connect()

        rows = connection.execute(
            """
            SELECT
                candidate_id,
                event_type,
                COUNT(*) AS count,
                SUM(duration) AS total_duration,
                AVG(confidence) AS avg_confidence,
                SUM(CASE WHEN is_suspicious = 1 THEN 1 ELSE 0 END)
                    AS suspicious_count
            FROM behavior_events
            WHERE test_id = ?
            GROUP BY candidate_id, event_type
            ORDER BY candidate_id, count DESC
            """,
            (
                test_id,
            )
        ).fetchall()

        connection.close()

        return [
            dict(row)
            for row in rows
        ]

     
    # OBSERVATIONS FOR CANDIDATE
     

    def get_observations_for_candidate(
        self,
        test_id,
        candidate_id
    ):
        """Return raw behavior observations for one candidate."""

        connection = self.connect()

        rows = connection.execute(
            """
            SELECT *
            FROM behavior_observations
            WHERE test_id = ?
            AND candidate_id = ?
            ORDER BY timestamp
            """,
            (
                test_id,
                candidate_id
            )
        ).fetchall()

        connection.close()

        return [
            dict(row)
            for row in rows
        ]

     
    # GET TESTS
     

    def get_tests(self):
        connection = self.connect()

        rows = connection.execute(
            """
            SELECT *
            FROM tests
            ORDER BY created_at DESC
            """
        ).fetchall()

        connection.close()

        return [
            dict(row)
            for row in rows
        ]