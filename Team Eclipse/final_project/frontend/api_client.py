import time
import requests

BASE_URL = "http://127.0.0.1:8000/api"

class ProctorAPIClient:
    @staticmethod
    def send_telemetry(session_id: str, student_id: str, vision_data: dict, audio_data: dict):
        payload = {
            "session_id": session_id,
            "student_id": student_id,
            "timestamp": time.time(),
            "vision_data": vision_data,
            "audio_data": audio_data
        }
        try:
            res = requests.post(f"{BASE_URL}/stream/telemetry", json=payload, timeout=3)
            return res.json()
        except Exception as e:
            return {"status": "error", "message": str(e)}

    @staticmethod
    def evaluate_incident(session_id: str, student_id: str, vision_data: dict, audio_data: dict):
        payload = {
            "session_id": session_id,
            "student_id": student_id,
            "telemetry": {
                "session_id": session_id,
                "student_id": student_id,
                "timestamp": time.time(),
                "vision_data": vision_data,
                "audio_data": audio_data
            }
        }
        try:
            res = requests.post(f"{BASE_URL}/incidents/evaluate", json=payload, timeout=30)
            return res.json()
        except Exception as e:
            return {"error": f"Evaluation request failed: {str(e)}"}
