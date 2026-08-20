"""
Optional head-pose refinement using MediaPipe's FaceLandmarker.
PoseAnalyzer's default head_yaw estimate comes from body-skeleton keypoints only (nose position relative to shoulder center). 

can be done but my system is i3 and it lagged so I skipped but it works as a standard module I have tried it.

Setup (one-time, requires internet - not run automatically):
    mkdir -p models
    wget -O models/face_landmarker.task \
        https://storage.googleapis.com/mediapipe-models/face_landmarker/face_landmarker/float16/1/face_landmarker.task

"""

import math
import numpy as np
import cv2

try:
    import mediapipe as mp
    MEDIAPIPE_AVAILABLE = True
except ImportError:
    MEDIAPIPE_AVAILABLE = False


class FaceMeshRefiner:

    def __init__(
        self,
        model_path="models/face_landmarker.task",
        yaw_threshold=15
    ):

        self.yaw_threshold = yaw_threshold
        self.available = False
        self._landmarker = None

        if not MEDIAPIPE_AVAILABLE:
            return

        import os

        if not os.path.exists(model_path):
            return

        try:
            base_options = mp.tasks.BaseOptions(
                model_asset_path=model_path
            )

            options = mp.tasks.vision.FaceLandmarkerOptions(
                base_options=base_options,
                running_mode=mp.tasks.vision.RunningMode.IMAGE,
                num_faces=1,
                min_face_detection_confidence=0.4,
                output_facial_transformation_matrixes=True
            )

            self._landmarker = (
                mp.tasks.vision.FaceLandmarker.create_from_options(options)
            )

            self.available = True

        except Exception:
            self.available = False

     
    # REFINE
     

    def refine(
        self,
        image_path,
        bbox
    ):
        """
        bbox: (x1, y1, x2, y2) in original image pixel coordinates,
              e.g. from YOLO pose's result.boxes.xyxy for the same person.

        Returns None if unavailable / no face detected, else a dict
        with a refined head_yaw / head_direction / confidence.
        """

        if not self.available:
            return None

        image = cv2.imread(image_path)

        if image is None:
            return None

        x1, y1, x2, y2 = [int(v) for v in bbox]

        # Pad the crop a little so the face isn't clipped at the box edge.
        pad_x = int((x2 - x1) * 0.15)
        pad_y = int((y2 - y1) * 0.15)

        h, w = image.shape[:2]

        x1 = max(0, x1 - pad_x)
        y1 = max(0, y1 - pad_y)
        x2 = min(w, x2 + pad_x)
        y2 = min(h, y2 + pad_y)

        crop = image[y1:y2, x1:x2]

        if crop.size == 0:
            return None

        crop_rgb = cv2.cvtColor(crop, cv2.COLOR_BGR2RGB)

        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=crop_rgb
        )

        try:
            result = self._landmarker.detect(mp_image)
        except Exception:
            return None

        if not result.facial_transformation_matrixes:
            return None

        matrix = np.array(
            result.facial_transformation_matrixes[0]
        )

        yaw, pitch, roll = self.matrix_to_euler(matrix)

        if yaw < -self.yaw_threshold:
            head_direction = "left"
        elif yaw > self.yaw_threshold:
            head_direction = "right"
        else:
            head_direction = "forward"

        # Faces detected via a dedicated face model are generally a
        # stronger signal than body-skeleton geometry.
        confidence = 0.85

        return {
            "head_yaw": round(float(yaw), 3),
            "head_pitch": round(float(pitch), 3),
            "head_direction": head_direction,
            "confidence": confidence,
            "refined_by": "mediapipe_face_mesh"
        }

     
    # MATH: ROTATION MATRIX -> EULER ANGLES (degrees)
     

    @staticmethod
    def matrix_to_euler(
        matrix
    ):

        rotation = matrix[:3, :3]

        sy = math.sqrt(
            rotation[0, 0] ** 2
            + rotation[1, 0] ** 2
        )

        singular = sy < 1e-6

        if not singular:
            pitch = math.atan2(rotation[2, 1], rotation[2, 2])
            yaw = math.atan2(-rotation[2, 0], sy)
            roll = math.atan2(rotation[1, 0], rotation[0, 0])
        else:
            pitch = math.atan2(-rotation[1, 2], rotation[1, 1])
            yaw = math.atan2(-rotation[2, 0], sy)
            roll = 0

        return (
            math.degrees(yaw),
            math.degrees(pitch),
            math.degrees(roll)
        )
