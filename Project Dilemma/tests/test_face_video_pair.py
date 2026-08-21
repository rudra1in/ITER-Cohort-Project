from src.agents.face_embedding_agent import (
    get_face_embedding,
)

from src.agents.face_verification_agent import (
    cosine_similarity,
)


frame_1 = get_face_embedding(
    "data/frames/frame_0000.jpg"
)

frame_2 = get_face_embedding(
    "data/frames/frame_0080.jpg"
)

similarity = cosine_similarity(
    frame_1,
    frame_2,
)

print("Video-frame similarity:")
print(similarity)