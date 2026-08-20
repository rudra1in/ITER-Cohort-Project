import os
import cv2
import numpy as np
from ultralytics import YOLO
from ultralytics import YOLO

class ObjectDetector:
    PROHIBITED_CLASSES = {0: "Person", 63: "Cell Phone", 67: "Cell Phone/Laptop", 73: "Book"}

    def __init__(self, model_path: str = "models/yolov8n.pt", confidence_threshold: float = 0.4):
        self.model = YOLO(model_path)
        self.conf = confidence_threshold

    def detect_prohibited_objects(self, frame: np.ndarray) -> dict:
        results = self.model.predict(frame, conf=self.conf, verbose=False)[0]
        detected_items = []
        violations = []
        person_count = 0

        for box in results.boxes:
            cls_id = int(box.cls[0])
            confidence = float(box.conf[0])
            label = self.model.names[cls_id]

            if cls_id == 0:
                person_count += 1

            if cls_id in self.PROHIBITED_CLASSES or label in ["cell phone", "book", "laptop"]:
                detected_items.append({
                    "class_id": cls_id,
                    "label": label,
                    "confidence": round(confidence, 2),
                    "bbox": [int(x) for x in box.xyxy[0].tolist()]
                })
                if cls_id != 0:
                    violations.append(label)

        if person_count > 1:
            violations.append("Multiple Persons Detected")

        return {
            "has_violation": len(violations) > 0,
            "violations": list(set(violations)),
            "person_count": person_count,
            "detected_objects": detected_items
        }
    class ObjectDetector:
     def __init__(self):
        try:
            self.model = YOLO("yolov8n.pt")
        except Exception:
            self.model = None

    def detect_objects(self, frame):
        if not self.model:
            return []
        results = self.model(frame, verbose=False)
        return results
