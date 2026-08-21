import json
from pathlib import Path
from app.tracker import PersonTracker
from app.pose_analyzer import PoseAnalyzer
from app.behavior import BehaviorAnalyzer
from app.event_engine import EventEngine
from app.gemini_fallback import GeminiEscalation


class BehavioralAnalysisService:

    def __init__(
        self,
        database,
        tracker,
        pose_analyzer,
        event_engine,
        gemini_escalation=None
    ):

        self.database = database

        self.tracker = tracker

        self.pose_analyzer = (
            pose_analyzer
        )

        self.event_engine = (
            event_engine
        )

        self.gemini_escalation = (
            gemini_escalation
            or GeminiEscalation()
        )

     
    # ANALYZE TEST
     

    def analyze_test(
        self,
        test_id
    ):

        frames = (
            self.database.get_frames(
                test_id
            )
        )

        if not frames:

            raise ValueError(
                "No frames found for "
                f"test {test_id}"
            )

         
        # Sort frames
         

        frames.sort(
            key=lambda frame: (
                frame.get(
                    "timestamp"
                ) or "",
                frame["filename"]
            )
        )

        image_paths = [

            frame["image_path"]

            for frame in frames

        ]

         
        # TRACK PEOPLE
         

        try:
            tracking_results = (
                self.tracker.track(
                    image_paths
                )
            )
        except Exception as e:
            import traceback
            traceback.print_exc()
            raise e

        observations = []

        previous_centers = {}

        for index, frame in enumerate(
            frames
        ):

            detections = (
                tracking_results[index]
                if index
                < len(tracking_results)
                else []
            )

             
            # POSE
             

            pose_results = (
                self.pose_analyzer.analyze(
                    frame["image_path"]
                )
            )

             
            # OBJECT DETECTIONS FROM PART 1
             

            object_names = (
                self.get_frame_objects(
                    frame["frame_id"]
                )
            )

            person_count = len(
                detections
            )

             
            # MATCH TRACKED PEOPLE TO POSE
             

            for person_index, tracked in enumerate(
                detections
            ):

                track_id = (
                    tracked["track_id"]
                )

                if track_id is None:

                    continue

                if person_index < len(
                    pose_results
                ):

                    pose = (
                        pose_results[
                            person_index
                        ]
                    )

                else:

                    pose = {

                        "head_yaw":
                            0.0,

                        "head_pitch":
                            0.0,

                        "head_direction":
                            "unknown",

                        "body_direction":
                            "unknown",

                        "pose_confidence":
                            0.0
                    }

                 
                # OPTIONAL GEMINI ESCALATION (ambiguous frames only)
                 

                escalated_by = None

                if (
                    self.gemini_escalation
                    and self.gemini_escalation.enabled
                    and self.gemini_escalation.is_ambiguous(pose)
                ):

                    escalation_result = (
                        self.gemini_escalation.escalate(
                            frame["image_path"]
                        )
                    )

                    if escalation_result is not None:

                        pose["head_direction"] = (
                            escalation_result["head_direction"]
                        )

                        pose["pose_confidence"] = max(
                            pose.get("pose_confidence", 0.0),
                            escalation_result["confidence"]
                        )

                        escalated_by = (
                            escalation_result["escalated_by"]
                        )

                        gemini_phone_visible = (
                            escalation_result.get(
                                "phone_visible",
                                False
                            )
                        )

                    else:

                        gemini_phone_visible = False

                else:

                    gemini_phone_visible = False

                 
                # CENTER
                 

                center = (

                    (
                        tracked["x1"]
                        + tracked["x2"]
                    ) / 2,

                    (
                        tracked["y1"]
                        + tracked["y2"]
                    ) / 2

                )

                previous_center = (
                    previous_centers.get(
                        track_id
                    )
                )

                movement_score = (
                    BehaviorAnalyzer.movement_score(
                        previous_center,
                        center
                    )
                )

                previous_centers[
                    track_id
                ] = center

                 
                # MOVEMENT
                 

                movement = (
                    BehaviorAnalyzer.movement_label(
                        movement_score
                    )
                )

                 
                # CANDIDATE
                 

                candidate_id = (
                    frame["candidate_id"]
                )

                 
                # FEATURE VECTOR
                 

                feature_vector = (
                    BehaviorAnalyzer.feature_vector(
                        pose=pose,
                        detection_info=object_names,
                        previous_center=previous_center,
                        current_center=center
                    )
                )

                observation = {

                    "frame_id":
                        frame["frame_id"],

                    "test_id":
                        test_id,

                    "candidate_id":
                        candidate_id,

                    "track_id":
                        track_id,

                    "timestamp":
                        frame["timestamp"],

                    "head_direction":
                        pose.get(
                            "head_direction",
                            "unknown"
                        ),

                    "head_yaw":
                        pose.get(
                            "head_yaw",
                            0.0
                        ),

                    "head_pitch":
                        pose.get(
                            "head_pitch",
                            0.0
                        ),

                    "body_direction":
                        pose.get(
                            "body_direction",
                            "unknown"
                        ),

                    "movement":
                        movement,

                    "movement_score":
                        movement_score,

                    "phone_visible":
                        (
                            "cell phone"
                            in object_names
                        )
                        or gemini_phone_visible,

                    "escalated_by":
                        escalated_by,

                    "paper_visible":
                        (
                            "book"
                            in object_names
                            or
                            "paper"
                            in object_names
                        ),

                    "person_count":
                        person_count,

                    "pose_confidence":
                        pose.get(
                            "pose_confidence",
                            0.0
                        ),

                    "feature_json":
                        json.dumps(
                            feature_vector.tolist()
                        )
                }

                self.database.insert_behavior_observation(
                    observation
                )

                observations.append(
                    observation
                )

         
        # BUILD EVENTS
         

        events = (
            self.event_engine.build_events(
                observations
            )
        )

        for event in events:

            self.database.insert_behavior_event(
                event
            )

        return {

            "test_id":
                test_id,

            "frames_analyzed":
                len(frames),

            "observations":
                len(observations),

            "events":
                len(events),

            "event_details":
                events
        }

     
    # FRAME OBJECTS
     

    def get_frame_objects(
        self,
        frame_id
    ):

        connection = (
            self.database.connect()
        )

        rows = connection.execute(
            """
            SELECT class_name
            FROM detections
            WHERE frame_id = ?
            """,
            (
                frame_id,
            )
        ).fetchall()

        connection.close()

        return [
            row["class_name"]
            for row in rows
        ]