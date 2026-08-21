import hashlib
import re
from pathlib import Path
import cv2
import imagehash
from PIL import Image


class ImageUtils:

    
    # VALIDATE
    

    @staticmethod
    def validate_image(
        image_path,
        min_width=320,
        min_height=240
    ):

        path = Path(
            image_path
        )

        if not path.exists():

            return False, (
                "File does not exist"
            )

        try:

            with Image.open(path) as image:

                width, height = (
                    image.size
                )

                if width < min_width:

                    return False, (
                        f"Image width "
                        f"{width} is too small"
                    )

                if height < min_height:

                    return False, (
                        f"Image height "
                        f"{height} is too small"
                    )

                image.verify()

            return True, "OK"

        except Exception as error:

            return False, str(error)

    
    # SHA256
    

    @staticmethod
    def sha256(
        image_path
    ):

        sha = hashlib.sha256()

        with open(
            image_path,
            "rb"
        ) as file:

            while True:

                chunk = file.read(
                    1024 * 1024
                )

                if not chunk:

                    break

                sha.update(
                    chunk
                )

        return sha.hexdigest()

    
    # PERCEPTUAL HASH
    

    @staticmethod
    def phash(
        image_path
    ):

        with Image.open(
            image_path
        ) as image:

            return str(
                imagehash.phash(
                    image
                )
            )

    
    # PHASH DISTANCE
    

    @staticmethod
    def phash_distance(
        phash_a,
        phash_b
    ):

        hash_a = imagehash.hex_to_hash(
            phash_a
        )

        hash_b = imagehash.hex_to_hash(
            phash_b
        )

        return hash_a - hash_b

    
    # IMAGE METADATA
    

    @staticmethod
    def metadata(
        image_path
    ):

        path = Path(
            image_path
        )

        with Image.open(
            path
        ) as image:

            width, height = (
                image.size
            )

        return {
            "width": width,
            "height": height,
            "file_size": path.stat().st_size
        }

    
    # TIMESTAMP EXTRACTION
    

    @staticmethod
    def extract_timestamp(
        filename
    ):

        patterns = [

            r"(?<!\d)(\d{2})[_-](\d{2})[_-](\d{2})(?!\d)",

            # 10:41:22
            r"(\d{2}):(\d{2}):(\d{2})",

            # 104122
            r"(?<!\d)(\d{2})(\d{2})(\d{2})(?!\d)"

        ]

        for pattern in patterns:

            match = re.search(
                pattern,
                filename
            )

            if match:

                hour = match.group(1)
                minute = match.group(2)
                second = match.group(3)

                return (
                    f"{hour}:"
                    f"{minute}:"
                    f"{second}"
                )

        return None

    
    # CHANGE SCORE
    

    @staticmethod
    def change_score(
        previous_path,
        current_path
    ):

        previous = cv2.imread(
            str(previous_path)
        )

        current = cv2.imread(
            str(current_path)
        )

        if (
            previous is None
            or current is None
        ):

            return 1.0

        # Resize both images so the comparison is cheap and consistent.

        previous = cv2.resize(
            previous,
            (320, 240)
        )

        current = cv2.resize(
            current,
            (320, 240)
        )

        previous_gray = cv2.cvtColor(
            previous,
            cv2.COLOR_BGR2GRAY
        )

        current_gray = cv2.cvtColor(
            current,
            cv2.COLOR_BGR2GRAY
        )

        difference = cv2.absdiff(
            previous_gray,
            current_gray
        )

        score = (
            difference.mean()
            / 255.0
        )

        return float(
            score
        )