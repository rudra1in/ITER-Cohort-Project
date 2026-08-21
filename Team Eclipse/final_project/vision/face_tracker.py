import os
import urllib.request
import cv2
import numpy as np

# Safe import for Raspberry Pi GPIO pins
try:
    import RPi.GPIO as GPIO
    HAS_RPI = True
except (ImportError, RuntimeError, ModuleNotFoundError):
    GPIO = None
    HAS_RPI = False


class FaceTracker:
    def __init__(self, min_detection_confidence=0.5, min_tracking_confidence=0.5):
        """
        Initializes the face detector using OpenCV Haar Cascades with automated local fallback.
        """
        self.cascade_dir = os.path.dirname(os.path.abspath(__file__))
        self.xml_path = os.path.join(self.cascade_dir, "haarcascade_frontalface_default.xml")
        
        # Download XML cascade if not locally present
        if not os.path.exists(self.xml_path):
            url = "https://raw.githubusercontent.com/opencv/opencv/4.x/data/haarcascades/haarcascade_frontalface_default.xml"
            try:
                urllib.request.urlretrieve(url, self.xml_path)
            except Exception as e:
                print(f"Warning: Could not download cascade XML: {e}")

        self.face_cascade = cv2.CascadeClassifier(self.xml_path)
        if self.face_cascade.empty():
            backup_path = os.path.join(cv2.data.haarcascades, "haarcascade_frontalface_default.xml")
            self.face_cascade = cv2.CascadeClassifier(backup_path)

        if HAS_RPI and GPIO:
            try:
                GPIO.setmode(GPIO.BCM)
            except Exception:
                pass

    def process_frame(self, frame: np.ndarray) -> dict:
        """
        Processes a single BGR/RGB frame to track faces and annotate visual indicators.
        
        :param frame: Raw image array from camera feed
        :return: Structured telemetry dictionary containing face count and status
        """
        if frame is None or frame.size == 0:
            return {
                "face_count": 0,
                "status": "NO_FRAME",
                "pose": {"pitch": 0.0, "yaw": 0.0, "roll": 0.0},
                "raw_landmarks": None
            }

        # Convert frame safely to grayscale for Cascade processing
        if len(frame.shape) == 3 and frame.shape[2] == 3:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        else:
            gray = frame.copy()

        # CLAHE (Contrast Limited Adaptive Histogram Equalization) for low-light/backlit setup
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        gray = clahe.apply(gray)

        faces = []
        if not self.face_cascade.empty():
            # Reliable parameter configuration for webcam proctoring
            faces = self.face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(60, 60)
            )

        face_count = len(faces)

        # Draw visual indicators directly onto the frame
        for (x, y, w, h) in faces:
            box_color = (0, 255, 0) if face_count == 1 else (0, 0, 255)
            label = "Face Detected" if face_count == 1 else "Extra Face Detected"

            cv2.rectangle(frame, (int(x), int(y)), (int(x + w), int(y + h)), box_color, 2)
            cv2.putText(frame, label, (int(x), int(y) - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, box_color, 2)

        # Determine overall detection status
        status = "NORMAL"
        if face_count == 0:
            status = "NO_FACE_DETECTED"
        elif face_count > 1:
            status = "MULTIPLE_FACES_DETECTED"

        return {
            "face_count": face_count,
            "status": status,
            "pose": {"pitch": 0.0, "yaw": 0.0, "roll": 0.0},
            "raw_landmarks": None
        }


# -----------------------------------------------------------------------------
# Standalone Module Test Execution (`python vision/face_tracker.py`)
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    tracker = FaceTracker()
    cap = cv2.VideoCapture(0)

    print("Starting FaceTracker camera preview. Press 'q' to exit...")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        result = tracker.process_frame(frame)

        cv2.putText(frame, f"Status: {result['status']} | Count: {result['face_count']}", 
                    (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

        cv2.imshow("FaceTracker Test Window", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()