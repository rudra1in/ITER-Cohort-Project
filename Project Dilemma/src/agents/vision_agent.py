import base64
import json
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq

from src.state import VerificationState


load_dotenv()

client = Groq()


def encode_image(image_path: str) -> str:
    """Convert an image file to base64."""

    with open(image_path, "rb") as image_file:
        return base64.b64encode(
            image_file.read()
        ).decode("utf-8")


def extract_json(text: str) -> dict:
    """
    Extract the first complete JSON object from
    the model response.
    """

    if "</think>" in text:
        text = text.split("</think>", 1)[1]

    text = text.replace("```json", "")
    text = text.replace("```", "")
    text = text.strip()

    start = text.find("{")

    if start == -1:
        raise ValueError(
            "No JSON object found in model response."
        )

    decoder = json.JSONDecoder()

    try:
        data, _ = decoder.raw_decode(
            text[start:]
        )
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"Could not parse JSON from model response: {exc}"
        ) from exc

    if not isinstance(data, dict):
        raise ValueError(
            "Model response is not a JSON object."
        )

    return data


def analyze_image(
    image_path: str,
    prompt: str,
) -> dict:
    """
    Send one image to the Groq vision model.
    """

    image_data = encode_image(
        str(Path(image_path))
    )

    response = client.chat.completions.create(
        model="qwen/qwen3.6-27b",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt,
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": (
                                "data:image/jpeg;base64,"
                                f"{image_data}"
                            )
                        },
                    },
                ],
            }
        ],
        temperature=0,
    )

    text = response.choices[0].message.content

    return extract_json(text)


def vision_agent(
    state: VerificationState,
) -> VerificationState:

    id_image_path = state.get(
        "id_image_path"
    )

    frame_paths = state.get(
        "frame_paths",
        []
    )

    errors = list(
        state.get("errors", [])
    )

    # --------------------------------------------------
    # ID IMAGE
    # --------------------------------------------------

    if id_image_path:

        id_prompt = """
You are an identity verification vision agent.

Analyze this ID image.

Return ONLY one JSON object:

{
    "document_type": "type of ID",
    "name": "name",
    "date_of_birth": "date of birth",
    "id_number": "ID number",
    "identity_features": [
        "feature 1",
        "feature 2"
    ]
}

Use null when information is not visible.
Do not invent information.
Do not include reasoning.
Do not include markdown.
"""

        try:

            identity_data = analyze_image(
                image_path=id_image_path,
                prompt=id_prompt,
            )

            state = {
                **state,
                "identity_data": identity_data,
            }

        except Exception as exc:

            errors.append(
                f"ID vision analysis failed: {exc}"
            )

    # --------------------------------------------------
    # VIDEO FRAME
    # --------------------------------------------------

    if frame_paths:

        video_prompt = """
You are an identity verification vision agent.

Analyze the provided image and identify the
PRIMARY person being verified.

Return ONLY one JSON object:

{
    "person_description": "short description",
    "visible_face": true,
    "number_of_people": 1,
    "identity_features": [
        "feature 1",
        "feature 2",
        "feature 3"
    ]
}

Only describe visibly observable information.
Do not invent information.
Do not include reasoning.
Do not include markdown.
"""

        selected_frame = frame_paths[0]

        try:

            video_identity_data = analyze_image(
                image_path=selected_frame,
                prompt=video_prompt,
            )

            state = {
                **state,
                "video_identity_data": (
                    video_identity_data
                ),
            }

        except Exception as exc:

            errors.append(
                f"Video vision analysis failed: {exc}"
            )

    state["errors"] = errors

    return state