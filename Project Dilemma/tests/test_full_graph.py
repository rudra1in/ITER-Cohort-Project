from src.graph import workflow


result = workflow.invoke(
    {
        "id_image_path":
            "data/ids/test_img.jpg",

        "video_path":
            "data/videos/verification_video.mp4",

        "errors": [],
    }
)


print(
    "\n========== ERRORS =========="
)

print(
    result.get(
        "errors",
        []
    )
)


print(
    "\n========== ID DATA =========="
)

print(
    result.get(
        "identity_data"
    )
)


print(
    "\n========== FRAME COUNT =========="
)

print(
    len(
        result.get(
            "frame_paths",
            []
        )
    )
)


print(
    "\n========== VIDEO DATA =========="
)

print(
    result.get(
        "video_identity_data"
    )
)


print(
    "\n========== ID FACE EMBEDDING =========="
)

print(
    len(
        result.get(
            "id_face_embedding",
            []
        )
    )
)


print(
    "\n========== VIDEO FACE EMBEDDINGS =========="
)

print(
    len(
        result.get(
            "video_face_embeddings",
            []
        )
    )
)


print(
    "\n========== FACE SIMILARITY =========="
)

print(
    result.get(
        "face_similarity"
    )
)


print(
    "\n========== VERIFICATION =========="
)

print(
    result.get(
        "verification_result"
    )
)


print(
    "\n========== REASON =========="
)

print(
    result.get(
        "verification_reason"
    )
)


print(
    "\n========== CHROMA MATCH =========="
)

print(
    result.get(
        "chroma_match_id"
    )
)


print(
    "\n========== LEDGER =========="
)

print(
    result.get(
        "ledger_entry"
    )
)