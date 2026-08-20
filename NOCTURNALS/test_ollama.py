import requests
import json
import time


URL = "http://127.0.0.1:11434/api/chat"
MODEL = "qwen3:8b"


payload = {
    "model": MODEL,

    "messages": [
        {
            "role": "user",
            "content": (
                "Return ONLY this JSON and nothing else: "
                '{"action":"LABEL","reasoning":"test","review_required":false}'
            ),
        }
    ],

    "think": False,

    "stream": False,

    "options": {
        "temperature": 0,
        "num_predict": 100,
    },

    "keep_alive": "10m",
}


print("Testing Python -> Ollama...")
print(f"URL   : {URL}")
print(f"MODEL : {MODEL}")
print()


start = time.time()

try:

    response = requests.post(
        URL,
        json=payload,
        timeout=120,
    )

    elapsed = time.time() - start

    print(
        f"HTTP status: {response.status_code}"
    )

    print(
        f"Time taken : {elapsed:.2f} seconds"
    )

    response.raise_for_status()

    data = response.json()

    print()
    print("OLLAMA RESPONSE:")
    print(
        json.dumps(
            data,
            indent=2,
        )
    )

    print()
    print("SUCCESS!")

except Exception as exc:

    elapsed = time.time() - start

    print()
    print("FAILED!")
    print(
        f"Time before failure: {elapsed:.2f} seconds"
    )
    print(
        f"Error: {exc}"
    )