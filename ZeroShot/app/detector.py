from ultralytics import YOLO


class YOLODetector:

    def __init__(
        self,
        model_name="yolo11n.pt",
        confidence=0.35
    ):

        self.confidence = confidence

        print(
            f"Loading YOLO model: "
            f"{model_name}"
        )

        self.model = YOLO(
            model_name
        )

     
    # DETECT
     

    def detect(
        self,
        image_path
    ):

        results = self.model.predict(
            source=image_path,
            conf=self.confidence,
            verbose=False
        )

        detections = []

        if not results:

            return detections

        result = results[0]

        if result.boxes is None:

            return detections

        names = result.names

        for box in result.boxes:

            xyxy = (
                box.xyxy[0]
                .cpu()
                .numpy()
                .tolist()
            )

            confidence = float(
                box.conf[0]
                .cpu()
                .item()
            )

            class_id = int(
                box.cls[0]
                .cpu()
                .item()
            )

            class_name = names[
                class_id
            ]

            detections.append(
                {
                    "class_id": class_id,

                    "class_name":
                        class_name,

                    "confidence":
                        confidence,

                    "x1":
                        float(xyxy[0]),

                    "y1":
                        float(xyxy[1]),

                    "x2":
                        float(xyxy[2]),

                    "y2":
                        float(xyxy[3])
                }
            )

        return detections