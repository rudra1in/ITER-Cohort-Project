import uuid
import shutil
from pathlib import Path
from app.config import (
    SUPPORTED_EXTENSIONS,
    PROCESSED_DIR,
    PHASH_THRESHOLD,
    CHANGE_THRESHOLD,
    MIN_IMAGE_WIDTH,
    MIN_IMAGE_HEIGHT
)

from app.image_utils import ImageUtils


class IngestionService:

    def __init__(
        self,
        database,
        detector
    ):

        self.database = database

        self.detector = detector

     
    # INGEST TEST
     

    def ingest_test(
        self,
        test_id,
        source_directory
    ):

        source = Path(
            source_directory
        )

        if not source.exists():

            raise ValueError(
                f"Directory does not exist: "
                f"{source}"
            )

        self.database.create_test(
            test_id
        )

        image_files = (
            self.discover_images(
                source
            )
        )

        results = {

            "test_id":
                test_id,

            "discovered":
                len(image_files),

            "processed":
                0,

            "invalid":
                0,

            "exact_duplicates":
                0,

            "near_duplicates":
                0,

            "change_points":
                0,

            "detections":
                0,

            "errors":
                []
        }

        # Used for duplicate detection.

        known_hashes = {}

        known_phashes = []

        # Used for temporal change detection.

        previous_by_candidate = {}

        for image_path in image_files:

            try:

                result = (
                    self.process_image(
                        test_id=test_id,
                        image_path=image_path,
                        known_hashes=known_hashes,
                        known_phashes=known_phashes,
                        previous_by_candidate=(
                            previous_by_candidate
                        )
                    )
                )

                results[
                    "processed"
                ] += 1

                if result[
                    "is_exact_duplicate"
                ]:

                    results[
                        "exact_duplicates"
                    ] += 1

                if result[
                    "is_near_duplicate"
                ]:

                    results[
                        "near_duplicates"
                    ] += 1

                if result[
                    "is_change_point"
                ]:

                    results[
                        "change_points"
                    ] += 1

                results[
                    "detections"
                ] += result[
                    "detection_count"
                ]

            except ValueError as error:

                results[
                    "invalid"
                ] += 1

                results[
                    "errors"
                ].append(
                    {
                        "file":
                            str(image_path),

                        "error":
                            str(error)
                    }
                )

            except Exception as error:

                results[
                    "errors"
                ].append(
                    {
                        "file":
                            str(image_path),

                        "error":
                            str(error)
                    }
                )

        return results

     
    # DISCOVER
     

    def discover_images(
        self,
        root
    ):

        images = []

        for path in root.rglob("*"):

            if not path.is_file():

                continue

            if (
                path.suffix.lower()
                not in SUPPORTED_EXTENSIONS
            ):

                continue

            images.append(
                path
            )

        images.sort()

        return images

     
    # PROCESS IMAGE
     

    def process_image(
        self,
        test_id,
        image_path,
        known_hashes,
        known_phashes,
        previous_by_candidate
    ):

        image_path = Path(
            image_path
        )

         
        # VALIDATION
         

        valid, reason = (
            ImageUtils.validate_image(
                image_path,
                MIN_IMAGE_WIDTH,
                MIN_IMAGE_HEIGHT
            )
        )

        if not valid:

            raise ValueError(
                reason
            )

         
        # CANDIDATE
         

        candidate_id = (
            image_path.parent.name
        )

         
        # METADATA
         

        metadata = (
            ImageUtils.metadata(
                image_path
            )
        )

        timestamp = (
            ImageUtils.extract_timestamp(
                image_path.name
            )
        )

         
        # HASH
         

        sha256 = (
            ImageUtils.sha256(
                image_path
            )
        )

        phash = (
            ImageUtils.phash(
                image_path
            )
        )

         
        # EXACT DUPLICATE
         

        is_exact_duplicate = (
            sha256 in known_hashes
        )

        duplicate_of = (
            known_hashes.get(
                sha256
            )
        )

        if not is_exact_duplicate:

            known_hashes[
                sha256
            ] = str(
                image_path
            )

         
        # NEAR DUPLICATE
         

        is_near_duplicate = False

        near_duplicate_of = None

        for old_phash, old_path in (
            known_phashes
        ):

            distance = (
                ImageUtils.phash_distance(
                    phash,
                    old_phash
                )
            )

            if (
                distance
                <= PHASH_THRESHOLD
            ):

                is_near_duplicate = True

                near_duplicate_of = (
                    old_path
                )

                break

        if not is_near_duplicate:

            known_phashes.append(
                (
                    phash,
                    str(image_path)
                )
            )

         
        # CHANGE DETECTION
         

        previous_path = (
            previous_by_candidate.get(
                candidate_id
            )
        )

        if previous_path:

            change_score = (
                ImageUtils.change_score(
                    previous_path,
                    image_path
                )
            )

        else:

            change_score = 1.0

        is_change_point = (
            change_score
            >= CHANGE_THRESHOLD
        )

        previous_by_candidate[
            candidate_id
        ] = image_path

         
        # COPY IMAGE
         

        output_directory = (
            Path(PROCESSED_DIR)
            / test_id
            / candidate_id
        )

        output_directory.mkdir(
            parents=True,
            exist_ok=True
        )

        destination = (
            output_directory
            / image_path.name
        )

        if not destination.exists():

            shutil.copy2(
                image_path,
                destination
            )

         
        # FRAME ID
         

        frame_id = (
            f"FRAME_"
            f"{uuid.uuid4().hex[:12]}"
        )

         
        # YOLO
         

        # For Part 1 we run YOLO on:
        #
        # 1. first frame
        # 2. change points
        # 3. frames that are not near duplicates
        #
        # This is deliberately conservative.

        should_run_yolo = (

            not is_exact_duplicate

            and (

                is_change_point

                or not is_near_duplicate

            )
        )

        detections = []

        if should_run_yolo:

            detections = (
                self.detector.detect(
                    str(destination)
                )
            )

         
        # SAVE FRAME
         

        frame = {

            "frame_id":
                frame_id,

            "test_id":
                test_id,

            "candidate_id":
                candidate_id,

            "filename":
                image_path.name,

            "image_path":
                destination.as_posix(),

            "timestamp":
                timestamp,

            "sha256":
                sha256,

            "phash":
                phash,

            "width":
                metadata["width"],

            "height":
                metadata["height"],

            "file_size":
                metadata["file_size"],

            "is_exact_duplicate":
                is_exact_duplicate,

            "duplicate_of":
                duplicate_of,

            "is_near_duplicate":
                is_near_duplicate,

            "near_duplicate_of":
                near_duplicate_of,

            "is_change_point":
                is_change_point,

            "change_score":
                change_score,

            "yolo_processed":
                should_run_yolo
        }

        self.database.insert_frame(
            frame
        )

         
        # SAVE DETECTIONS
         

        for detection in detections:

            self.database.insert_detection(
                frame_id,
                detection
            )

        return {

            "frame_id":
                frame_id,

            "is_exact_duplicate":
                is_exact_duplicate,

            "is_near_duplicate":
                is_near_duplicate,

            "is_change_point":
                is_change_point,

            "change_score":
                change_score,

            "detection_count":
                len(detections)
        }