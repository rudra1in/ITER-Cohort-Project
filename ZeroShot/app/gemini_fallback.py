"""
Gemini escalation for ambiguous frames.
This is a FAILSAFE, not a primary path

Ambiguity criteria (tune via constructor args):
  - pose_confidence below `confidence_threshold`, OR
  - head_direction == "unknown"

"""

import os
import json
import base64
import requests


GEMINI_API_URL = (
    "https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
)

ESCALATION_PROMPT = (
    "You are assisting a post-test behavioral review system. Look at "
    "this single photo of a person during a test. Answer strictly as "
    "JSON with no other text, no markdown fences:\n"
    "{\n"
    '  "head_direction": "forward" | "left" | "right" | "unknown",\n'
    '  "phone_visible": true | false,\n'
    '  "confidence": <number between 0 and 1>\n'
    "}"
)


class GeminiEscalation:

    def __init__(
        self,
        api_key=None,
        model="gemini-2.0-flash",
        confidence_threshold=0.4,
        timeout=15
    ):

        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        self.model = model
        self.confidence_threshold = confidence_threshold
        self.timeout = timeout

        self.enabled = bool(self.api_key)

     
    # AMBIGUITY CHECK
     

    def is_ambiguous(
        self,
        observation
    ):

        pose_confidence = observation.get(
            "pose_confidence",
            observation.get("pose", {}).get("pose_confidence", 1.0)
        )

        head_direction = observation.get(
            "head_direction",
            observation.get("pose", {}).get("head_direction")
        )

        if pose_confidence is None:
            pose_confidence = 1.0

        if pose_confidence < self.confidence_threshold:
            return True

        if head_direction == "unknown":
            return True

        return False

     
    # ESCALATE
     

    def escalate(
        self,
        image_path
    ):
        """
        Returns None if disabled, on any error, or on an unparseable
        response - callers should treat None as "keep the existing
        local observation, don't override anything".

        Otherwise returns:
            {"head_direction": ..., "phone_visible": ..., "confidence": ...}
        """

        if not self.enabled:
            return None

        try:
            with open(image_path, "rb") as file:
                image_b64 = base64.b64encode(file.read()).decode("utf-8")

            url = GEMINI_API_URL.format(model=self.model)

            payload = {
                "contents": [{
                    "parts": [
                        {"text": ESCALATION_PROMPT},
                        {
                            "inline_data": {
                                "mime_type": "image/jpeg",
                                "data": image_b64
                            }
                        }
                    ]
                }],
                "generationConfig": {
                    "temperature": 0
                }
            }

            response = requests.post(
                url,
                params={"key": self.api_key},
                json=payload,
                timeout=self.timeout
            )

            response.raise_for_status()

            data = response.json()

            text = (
                data["candidates"][0]["content"]["parts"][0]["text"]
            )

            return self.parse_response(text)

        except Exception:
            return None

     
    # PARSE
     

    @staticmethod
    def parse_response(
        text
    ):

        try:
            cleaned = text.strip()

            if cleaned.startswith("```"):
                cleaned = cleaned.strip("`")
                if cleaned.lower().startswith("json"):
                    cleaned = cleaned[4:]

            parsed = json.loads(cleaned.strip())

            head_direction = parsed.get("head_direction")

            if head_direction not in ("forward", "left", "right", "unknown"):
                return None

            return {
                "head_direction": head_direction,
                "phone_visible": bool(parsed.get("phone_visible", False)),
                "confidence": float(parsed.get("confidence", 0.6)),
                "escalated_by": "gemini"
            }

        except Exception:
            return None
