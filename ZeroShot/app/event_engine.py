import uuid
import json


# THRESHOLDS so far i think

# Movement score above this triggers excessive_movement.
EXCESSIVE_MOVEMENT_THRESHOLD = 60.0
# body_direction values that trigger body_turned_away.
TURNED_AWAY_DIRECTIONS = {"away", "side"}
# Minimum consecutive frames to consider for absent/extra person.
MIN_STREAK_FRAMES = 1


class EventEngine:

    def __init__(
        self,
        min_duration=3,
        gap_seconds=3,
        excessive_movement_threshold=EXCESSIVE_MOVEMENT_THRESHOLD
    ):

        self.min_duration = (
            min_duration
        )

        self.gap_seconds = (
            gap_seconds
        )

        self.excessive_movement_threshold = (
            excessive_movement_threshold
        )

     
    # BUILD EVENTS
     

    def build_events(
        self,
        observations
    ):
        """
        Build behavioral events from a flat list of observations.

        Also synthesises two frame-level events that cannot be derived
        from per-person observations alone:

        - absent_from_frame:    frames where a candidate's expected
                                person count drops to zero.
        - extra_person_detected: frames where person_count > 1
                                 (extra person in frame).

        Those require the full per-frame view so they are handled
        before the per-track loop.
        """

         
        # PER-TRACK GROUPS
         

        grouped = {}

        for observation in observations:

            key = (
                observation["test_id"],
                observation["track_id"]
            )

            grouped.setdefault(
                key,
                []
            ).append(
                observation
            )

        events = []

        for key, items in grouped.items():

            items.sort(
                key=lambda item:
                item.get(
                    "timestamp"
                ) or ""
            )

            events.extend(
                self.process_track(
                    items
                )
            )

         
        # FRAME-LEVEL EVENTS (absent / extra person)
         

        events.extend(
            self.process_frame_level(
                observations
            )
        )

        return events

     
    # FRAME-LEVEL EVENTS
     

    def process_frame_level(
        self,
        observations
    ):
        """
        Detect absent_from_frame and extra_person_detected by
        grouping observations by (test_id, candidate_id, frame_id).
        """

        if not observations:
            return []

        # Group by (test_id, candidate_id, timestamp / frame_id).
        # We use frame_id as the key to get one record per frame.

        frame_map = {}

        for obs in observations:

            key = (
                obs["test_id"],
                obs["candidate_id"],
                obs["frame_id"]
            )

            frame_map[key] = obs

        # Sort by timestamp.
        frames = sorted(
            frame_map.values(),
            key=lambda o: (
                o["candidate_id"],
                o.get("timestamp") or ""
            )
        )

        # Group by (test_id, candidate_id).
        by_candidate = {}

        for obs in frames:

            key = (
                obs["test_id"],
                obs["candidate_id"]
            )

            by_candidate.setdefault(
                key,
                []
            ).append(obs)

        events = []

        for (test_id, candidate_id), items in by_candidate.items():

            events.extend(
                self.detect_absent(
                    test_id,
                    candidate_id,
                    items
                )
            )

            events.extend(
                self.detect_extra_person(
                    test_id,
                    candidate_id,
                    items
                )
            )

        return events

     
    # ABSENT FROM FRAME
     

    def detect_absent(
        self,
        test_id,
        candidate_id,
        items
    ):

        events = []
        current = None

        for obs in items:

            is_absent = (
                int(obs.get("person_count", 1)) == 0
            )

            if is_absent:

                if current is None:

                    current = {
                        "event_id":
                            self.new_event_id(),
                        "test_id":
                            test_id,
                        "candidate_id":
                            candidate_id,
                        "track_id":
                            obs.get("track_id"),
                        "event_type":
                            "absent_from_frame",
                        "start_time":
                            obs.get("timestamp"),
                        "end_time":
                            obs.get("timestamp"),
                        "evidence": [
                            obs["frame_id"]
                        ],
                        "confidences": [0.9]
                    }

                else:

                    current["end_time"] = (
                        obs.get("timestamp")
                    )

                    current["evidence"].append(
                        obs["frame_id"]
                    )

                    current["confidences"].append(0.9)

            else:

                if current is not None:

                    finished = self.finish_event(
                        current
                    )

                    if finished:
                        events.append(finished)

                    current = None

        if current is not None:

            finished = self.finish_event(current)

            if finished:
                events.append(finished)

        return events

     
    # EXTRA PERSON DETECTED
     

    def detect_extra_person(
        self,
        test_id,
        candidate_id,
        items
    ):

        events = []
        current = None

        for obs in items:

            has_extra = (
                int(obs.get("person_count", 1)) > 1
            )

            if has_extra:

                if current is None:

                    current = {
                        "event_id":
                            self.new_event_id(),
                        "test_id":
                            test_id,
                        "candidate_id":
                            candidate_id,
                        "track_id":
                            obs.get("track_id"),
                        "event_type":
                            "extra_person_detected",
                        "start_time":
                            obs.get("timestamp"),
                        "end_time":
                            obs.get("timestamp"),
                        "evidence": [
                            obs["frame_id"]
                        ],
                        "confidences": [
                            obs.get(
                                "pose_confidence",
                                0.6
                            )
                        ],
                        "extra_counts": [
                            int(obs.get("person_count", 1)) - 1
                        ]
                    }

                else:

                    current["end_time"] = (
                        obs.get("timestamp")
                    )

                    current["evidence"].append(
                        obs["frame_id"]
                    )

                    current["confidences"].append(
                        obs.get("pose_confidence", 0.6)
                    )

                    current["extra_counts"].append(
                        int(obs.get("person_count", 1)) - 1
                    )

            else:

                if current is not None:

                    finished = self.finish_event(
                        current
                    )

                    if finished:
                        events.append(finished)

                    current = None

        if current is not None:

            finished = self.finish_event(current)

            if finished:
                events.append(finished)

        return events

     
    # TRACK EVENTS
     

    def process_track(
        self,
        observations
    ):

        events = []

        current_event = None

        for observation in observations:

            direction = (
                observation[
                    "head_direction"
                ]
            )

            body_direction = (
                observation.get(
                    "body_direction",
                    "unknown"
                )
            )

            phone_visible = (
                observation[
                    "phone_visible"
                ]
            )

            movement_score = float(
                observation.get(
                    "movement_score",
                    0.0
                )
            )

             
            # DETERMINE EVENT TYPE (priority order)
             

            event_type = None

            if phone_visible:

                event_type = "phone_visible"

            elif direction in ("left", "right"):

                event_type = "repeated_side_looking"

            elif body_direction in TURNED_AWAY_DIRECTIONS:

                event_type = "body_turned_away"

            elif (
                movement_score
                > self.excessive_movement_threshold
            ):

                event_type = "excessive_movement"

             
            # NO EVENT
             

            if event_type is None:

                if current_event:

                    completed = (
                        self.finish_event(
                            current_event
                        )
                    )

                    if completed:

                        events.append(
                            completed
                        )

                    current_event = None

                continue

             
            # START EVENT
             

            if current_event is None:

                current_event = {

                    "event_id":
                        self.new_event_id(),

                    "test_id":
                        observation[
                            "test_id"
                        ],

                    "candidate_id":
                        observation[
                            "candidate_id"
                        ],

                    "track_id":
                        observation[
                            "track_id"
                        ],

                    "event_type":
                        event_type,

                    "start_time":
                        observation[
                            "timestamp"
                        ],

                    "end_time":
                        observation[
                            "timestamp"
                        ],

                    "evidence": [

                        observation[
                            "frame_id"
                        ]

                    ],

                    "directions": [

                        direction

                    ],

                    "body_directions": [

                        body_direction

                    ],

                    "movement_scores": [

                        movement_score

                    ],

                    "confidences": [

                        observation.get(
                            "pose_confidence",
                            0.5
                        )

                    ]
                }

                continue

             
            # CONTINUE EVENT (same type)
             

            if (
                current_event[
                    "event_type"
                ]
                == event_type
            ):

                current_event[
                    "end_time"
                ] = observation[
                    "timestamp"
                ]

                current_event[
                    "evidence"
                ].append(
                    observation[
                        "frame_id"
                    ]
                )

                current_event[
                    "directions"
                ].append(
                    direction
                )

                current_event.setdefault(
                    "body_directions",
                    []
                ).append(body_direction)

                current_event.setdefault(
                    "movement_scores",
                    []
                ).append(movement_score)

                current_event[
                    "confidences"
                ].append(
                    observation.get(
                        "pose_confidence",
                        0.5
                    )
                )

            else:

                # Event type changed — close the old one.

                completed = (
                    self.finish_event(
                        current_event
                    )
                )

                if completed:

                    events.append(
                        completed
                    )

                # Open new event of the new type.

                current_event = {

                    "event_id":
                        self.new_event_id(),

                    "test_id":
                        observation[
                            "test_id"
                        ],

                    "candidate_id":
                        observation[
                            "candidate_id"
                        ],

                    "track_id":
                        observation[
                            "track_id"
                        ],

                    "event_type":
                        event_type,

                    "start_time":
                        observation[
                            "timestamp"
                        ],

                    "end_time":
                        observation[
                            "timestamp"
                        ],

                    "evidence": [
                        observation["frame_id"]
                    ],

                    "directions": [direction],

                    "body_directions": [body_direction],

                    "movement_scores": [movement_score],

                    "confidences": [
                        observation.get(
                            "pose_confidence",
                            0.5
                        )
                    ]
                }

         
        # FINAL EVENT
         

        if current_event:

            completed = (
                self.finish_event(
                    current_event
                )
            )

            if completed:

                events.append(
                    completed
                )

        return events

     
    # FINISH EVENT
     

    def finish_event(
        self,
        event
    ):

        duration = (
            self.estimate_duration(
                event[
                    "start_time"
                ],
                event[
                    "end_time"
                ]
            )
        )

        if duration < self.min_duration:

            return None

        confidences = event.get("confidences", [0.5])

        confidence = (
            sum(confidences)
            / len(confidences)
        ) if confidences else 0.5

        description = self.build_description(event)

        return {

            "event_id":
                event["event_id"],

            "test_id":
                event["test_id"],

            "candidate_id":
                event["candidate_id"],

            "track_id":
                event["track_id"],

            "event_type":
                event["event_type"],

            "start_time":
                event["start_time"],

            "end_time":
                event["end_time"],

            "duration":
                duration,

            "confidence":
                round(
                    confidence,
                    3
                ),

            "description":
                description,

            "evidence_json":
                json.dumps(
                    event["evidence"]
                )
        }

     
    # DESCRIPTION BUILDER
     

    def build_description(
        self,
        event
    ):

        event_type = event["event_type"]

        directions = event.get("directions", [])

        body_directions = event.get(
            "body_directions", []
        )

        movement_scores = event.get(
            "movement_scores", []
        )

        extra_counts = event.get("extra_counts", [])

        frame_count = len(
            event.get("evidence", [])
        )

        if event_type == "repeated_side_looking":

            left_count = directions.count("left")

            right_count = directions.count("right")

            dominant = (
                "left"
                if left_count >= right_count
                else "right"
            )

            return (
                f"Repeated side-oriented head movement observed "
                f"across {frame_count} frame(s). "
                f"Head turned left in {left_count} frame(s), "
                f"right in {right_count} frame(s). "
                f"Dominant direction: {dominant}. "
                f"Flagged for human review."
            )

        elif event_type == "phone_visible":

            return (
                f"A mobile phone was visible in {frame_count} "
                f"consecutive frame(s) during this time window. "
                f"Flagged for human review."
            )

        elif event_type == "body_turned_away":

            side_count = body_directions.count("side")

            away_count = body_directions.count("away")

            return (
                f"Candidate's body was oriented away from the camera "
                f"across {frame_count} frame(s) "
                f"({side_count} side-profile, {away_count} facing away). "
                f"Observable behavior recorded; flagged for review."
            )

        elif event_type == "excessive_movement":

            avg_movement = (
                sum(movement_scores) / len(movement_scores)
                if movement_scores
                else 0.0
            )

            return (
                f"Excessive body movement detected across "
                f"{frame_count} frame(s). "
                f"Average movement score: {avg_movement:.1f}. "
                f"Observable behavior recorded."
            )

        elif event_type == "absent_from_frame":

            return (
                f"Candidate was not detected in the frame across "
                f"{frame_count} consecutive frame(s). "
                f"Observable behavior recorded; flagged for review."
            )

        elif event_type == "extra_person_detected":

            max_extra = (
                max(extra_counts)
                if extra_counts
                else 1
            )

            return (
                f"An additional person was detected in the frame "
                f"across {frame_count} frame(s). "
                f"Maximum {max_extra} extra person(s) observed. "
                f"Observable behavior recorded; flagged for review."
            )

        else:

            return (
                "A behavioral pattern was observed. "
                "Observable behavior recorded."
            )

     
    # DURATION
     

    @staticmethod
    def estimate_duration(
        start,
        end
    ):

        if not start or not end:

            return 0.0

        try:

            start_seconds = (
                EventEngine.time_to_seconds(
                    start
                )
            )

            end_seconds = (
                EventEngine.time_to_seconds(
                    end
                )
            )

            duration = (
                end_seconds
                - start_seconds
            )

            if duration < 0:

                duration += 24 * 3600

            return float(
                duration
            )

        except Exception:

            return 0.0

     
    # TIME
     

    @staticmethod
    def time_to_seconds(
        value
    ):

        parts = value.split(":")

        if len(parts) != 3:

            return 0

        hour = int(parts[0])

        minute = int(parts[1])

        second = int(
            float(parts[2])
        )

        return (
            hour * 3600
            + minute * 60
            + second
        )

     
    # ID
     

    @staticmethod
    def new_event_id():

        return (
            "EVT_"
            + uuid.uuid4().hex[:10]
        )