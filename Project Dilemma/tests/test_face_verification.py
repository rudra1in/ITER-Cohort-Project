from src.agents.face_embedding_agent import (
    face_embedding_agent,
)

from src.agents.face_verification_agent import (
    face_verification_agent,
)


state = {
    "id_image_path": "data/ids/test_img.jpg",

    "frame_paths": [
        "data/frames/frame_0000.jpg",
        "data/frames/frame_0010.jpg",
        "data/frames/frame_0020.jpg",
        "data/frames/frame_0030.jpg",
        "data/frames/frame_0040.jpg",
        "data/frames/frame_0050.jpg",
        "data/frames/frame_0060.jpg",
        "data/frames/frame_0070.jpg",
        "data/frames/frame_0080.jpg",
    ],

    "errors": [],
}


state = face_embedding_agent(state)

# Store the ID embedding in Chroma.
from src.vectorstore.chroma import store_identity

store_identity(
    identity_id="ashim_test",
    face_embedding=state["id_face_embedding"],
    metadata={
        "name": "ASHIM ABINASH MISHRA",
        "type": "student_id",
    },
)


result = face_verification_agent(state)


print("\nErrors:")
print(result.get("errors"))

print(
    "\nNumber of video faces:",
    len(
        result.get(
            "video_face_embeddings",
            []
        )
    ),
)

print(
    "\nFace similarities:"
)

for index, similarity in enumerate(
    result.get(
        "face_similarities",
        []
    ),
    start=1,
):

    print(
        f"Frame {index}: "
        f"{similarity:.4f}"
    )

print(
    "\nMean similarity:",
    result.get("face_similarity"),
)

print(
    "Chroma match:",
    result.get("chroma_match_id"),
)

print(
    "Chroma distance:",
    result.get("chroma_distance"),
)

print(
    "\nVerification:",
    result.get("verification_result"),
)

print(
    "Reason:",
    result.get("verification_reason"),
)