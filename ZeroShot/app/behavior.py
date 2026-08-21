import json
import numpy as np

class BehaviorAnalyzer:

     
    # BUILD FEATURE VECTOR
     

    @staticmethod
    def feature_vector(
        pose,
        detection_info,
        previous_center=None,
        current_center=None
    ):

        head_yaw = float(
            pose.get(
                "head_yaw",
                0.0
            )
        )

        head_pitch = float(
            pose.get(
                "head_pitch",
                0.0
            )
        )

        movement_score = (
            BehaviorAnalyzer.movement_score(
                previous_center,
                current_center
            )
        )

        phone_visible = (
            "cell phone"
            in detection_info
        )

        paper_visible = (
            "book"
            in detection_info
            or
            "paper"
            in detection_info
        )

        vector = np.array(
            [
                head_yaw,
                head_pitch,
                movement_score,
                float(phone_visible),
                float(paper_visible)
            ],
            dtype=np.float32
        )

        return vector

     
    # MOVEMENT
     

    @staticmethod
    def movement_score(
        previous_center,
        current_center
    ):

        if (
            previous_center is None
            or current_center is None
        ):

            return 0.0

        dx = (
            current_center[0]
            - previous_center[0]
        )

        dy = (
            current_center[1]
            - previous_center[1]
        )

        distance = (
            dx ** 2
            + dy ** 2
        ) ** 0.5

        return float(
            distance
        )

     
    # HEAD DIRECTION
     

    @staticmethod
    def head_direction(
        yaw
    ):

        if yaw < -15:

            return "left"

        if yaw > 15:

            return "right"

        return "forward"

     
    # MOVEMENT LABEL
     

    @staticmethod
    def movement_label(
        score
    ):

        if score < 5:

            return "still"

        if score < 25:

            return "low"

        if score < 75:

            return "moderate"

        return "high"

     
    # SERIALIZE
     

    @staticmethod
    def serialize_vector(
        vector
    ):

        return json.dumps(
            vector.tolist()
        )