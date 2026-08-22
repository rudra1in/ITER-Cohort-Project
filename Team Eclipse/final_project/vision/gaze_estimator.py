import cv2
import numpy as np
import mediapipe as mp


class GazeEstimator:
    def __init__(self):
        if hasattr(mp, "solutions") and hasattr(mp.solutions, "face_mesh"):
            self.mode = "legacy"
            self.face_mesh = mp.solutions.face_mesh.FaceMesh(
                max_num_faces=1,
                refine_landmarks=True,
                min_detection_confidence=0.5,
                min_tracking_confidence=0.5
            )
        else:
            self.mode = "fallback"

    def estimate_gaze(self, frame: np.ndarray) -> dict:
        if getattr(self, "mode", "legacy") == "legacy":
            h, w, _ = frame.shape
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.face_mesh.process(rgb_frame)

            if not results.multi_face_landmarks:
                return {"gaze_direction": "CENTER", "looking_away": False}
            landmarks = results.multi_face_landmarks[0].landmark
            left_iris = landmarks[468]
            right_iris = landmarks[473]

            if left_iris.x < 0.35 or right_iris.x < 0.35:
                return {"gaze_direction": "LEFT", "looking_away": True}
            elif left_iris.x > 0.65 or right_iris.x > 0.65:
                return {"gaze_direction": "RIGHT", "looking_away": True}

        return {"gaze_direction": "CENTER", "looking_away": False}