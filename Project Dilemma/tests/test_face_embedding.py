from src.agents.face_embedding_agent import (
    face_embedding_agent,
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


result = face_embedding_agent(state)

print("\nErrors:")
print(result.get("errors"))

print(
    "\nID embedding dimension:",
    len(
        result.get(
            "id_face_embedding",
            []
        )
    ),
)

video_embeddings = result.get(
    "video_face_embeddings",
    []
)

print(
    "Number of video embeddings:",
    len(video_embeddings),
)

if video_embeddings:
    print(
        "Video embedding dimension:",
        len(video_embeddings[0]),
    )