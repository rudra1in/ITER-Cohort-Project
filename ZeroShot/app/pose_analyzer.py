import math
from ultralytics import YOLO

class PoseAnalyzer:

    def __init__(
        self,
        model_name="yolo11n-pose.pt",
        confidence=0.35,
        face_refiner=None
    ):

        self.model = YOLO(
            model_name
        )
        self.confidence = confidence
        self.face_refiner = face_refiner

    # ANALYZE IMAGE

    def analyze(
        self,
        image_path
    ):

        results = self.model.predict(
            source=image_path,
            conf=self.confidence,
            verbose=False
        )

        if not results:
            return []

        result = results[0]

        if result.keypoints is None or result.keypoints.xy is None:
            return []

        output = []

        try:
            keypoints = (
                result.keypoints.xy
                .data
                .cpu()
                .numpy()
            )
        except Exception:
            return []

        confidences = None
        if result.keypoints.conf is not None:
            try:
                confidences = (
                    result.keypoints.conf
                    .data
                    .cpu()
                    .numpy()
                )
            except Exception:
                confidences = None

        boxes = None
        if result.boxes is not None and result.boxes.xyxy is not None:
            try:
                boxes = (
                    result.boxes.xyxy
                    .data
                    .cpu()
                    .numpy()
                )
            except Exception:
                boxes = None

        for person_index, points in enumerate(
            keypoints
        ):
            person_conf = None
            if confidences is not None:
                try:
                    if person_index < len(confidences):
                        person_conf = confidences[person_index]
                    elif len(confidences) > 0:
                        person_conf = confidences[0]
                except Exception:
                    person_conf = None

            person = self.extract_features(
                points,
                person_conf
            )

            person["person_index"] = person_index

            # Optional MediaPipe refinement, if wired in 

            if (
                self.face_refiner is not None
                and self.face_refiner.available
                and boxes is not None
                and person_index < len(boxes)
            ):

                try:
                    refined = self.face_refiner.refine(
                        image_path,
                        boxes[person_index]
                    )
                except Exception:
                    refined = None

                if refined is not None:

                    person["head_yaw"] = refined["head_yaw"]
                    person["head_pitch"] = refined["head_pitch"]
                    person["head_direction"] = refined["head_direction"]
                    person["pose_confidence"] = max(
                        person["pose_confidence"],
                        refined["confidence"]
                    )
                    person["refined_by"] = refined["refined_by"]

            output.append(person)

        return output

    # KEYPOINT FEATURES

    def extract_features(
        self,
        points,
        confidence
    ):

        # YOLO pose COCO format:
        #Kept for my referance no code usage
        # 0  nose
        # 1  left eye
        # 2  right eye
        # 3  left ear
        # 4  right ear
        # 5  left shoulder
        # 6  right shoulder
        # 7  left elbow
        # 8  right elbow
        # 9  left wrist
        # 10 right wrist
        # 11 left hip
        # 12 right hip

        nose = self.point(
            points,
            0
        )

        left_shoulder = self.point(
            points,
            5
        )

        right_shoulder = self.point(
            points,
            6
        )

        left_hip = self.point(
            points,
            11
        )

        right_hip = self.point(
            points,
            12
        )

        # HEAD DIRECTION

        head_yaw = 0.0

        if (
            nose is not None
            and left_shoulder is not None
            and right_shoulder is not None
        ):

            shoulder_center_x = (
                left_shoulder[0]
                + right_shoulder[0]
            ) / 2

            shoulder_width = abs(
                right_shoulder[0]
                - left_shoulder[0]
            )

            if shoulder_width > 1:

                head_yaw = (
                    (
                        nose[0]
                        - shoulder_center_x
                    )
                    / shoulder_width
                ) * 90

        # BODY DIRECTION

        body_direction = (
            self.body_direction(
                left_shoulder,
                right_shoulder
            )
        )

        # HEAD DIRECTION LABEL

        if head_yaw < -15:

            head_direction = "left"

        elif head_yaw > 15:

            head_direction = "right"

        else:

            head_direction = "forward"

        return {

            "head_yaw":
                round(
                    float(head_yaw),
                    3
                ),

            "head_pitch":
                0.0,

            "head_direction":
                head_direction,

            "body_direction":
                body_direction,

            "pose_confidence":
                self.average_confidence(
                    confidence
                )
        }

    # POINT

    @staticmethod
    def point(
        points,
        index
    ):

        if (
            points is None
            or index >= len(points)
        ):

            return None

        x = float(
            points[index][0]
        )

        y = float(
            points[index][1]
        )

        if x == 0 and y == 0:

            return None

        return (
            x,
            y
        )

    # BODY DIRECTION

    @staticmethod
    def body_direction(
        left_shoulder,
        right_shoulder
    ):

        if (
            left_shoulder is None
            or right_shoulder is None
        ):

            return "unknown"

        dx = (
            right_shoulder[0]
            - left_shoulder[0]
        )

        if abs(dx) < 10:

            return "side"

        if dx < 0:

            return "forward"

        return "away"

    # CONFIDENCE

    @staticmethod
    def average_confidence(
        confidence
    ):

        if confidence is None:

            return 0.0

        valid = [
            float(value)
            for value in confidence
            if value > 0
        ]

        if not valid:

            return 0.0
        return round(
            sum(valid) / len(valid),
            3
        )