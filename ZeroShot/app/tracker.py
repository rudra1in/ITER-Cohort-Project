from ultralytics import YOLO


class PersonTracker:

    def __init__(
        self,
        model_name="yolo11n.pt",
        confidence=0.35
    ):

        self.model = YOLO(
            model_name
        )

        self.confidence = confidence

    # TRACK IMAGE SEQUENCE
    
    def track(
        self,
        image_paths
    ):

        results = self.model.track(
            source=image_paths,
            conf=self.confidence,
            tracker="bytetrack.yaml",
            persist=True,
            stream=True,
            verbose=False
        )

        observations = []

        for frame_index, result in enumerate(
            results
        ):

            frame_observations = []

            if (
                result.boxes is None
            ):

                observations.append(
                    frame_observations
                )

                continue

            names = result.names

            boxes = result.boxes

            for index, box in enumerate(
                boxes
            ):

                class_id = int(
                    box.cls
                    .cpu()
                    .item()
                )

                class_name = names[
                    class_id
                ]

                if class_name != "person":

                    continue

                confidence = float(
                    box.conf
                    .cpu()
                    .item()
                )

                coordinates = (
                    box.xyxy
                    .cpu()
                    .numpy()
                    .tolist()
                )[0]

                track_id = None

                if boxes.id is not None:
                    try:
                        track_tensor = boxes.id[index]
                        if track_tensor is not None:
                            track_id = int(track_tensor.cpu().item())
                    except Exception:
                        track_id = None

                frame_observations.append(
                    {

                        "track_id":
                            track_id,

                        "class_id":
                            class_id,

                        "class_name":
                            class_name,

                        "confidence":
                            confidence,

                        "x1":
                            float(
                                coordinates[0]
                            ),

                        "y1":
                            float(
                                coordinates[1]
                            ),

                        "x2":
                            float(
                                coordinates[2]
                            ),

                        "y2":
                            float(
                                coordinates[3]
                            )
                    }
                )

            observations.append(
                frame_observations
            )

        return observations