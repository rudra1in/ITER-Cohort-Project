from src.agents.face_embedding_agent import (
    get_face_embedding,
)

from src.agents.face_verification_agent import (
    cosine_similarity,
)


image_path = "data/ids/test_img.jpg"

embedding_1 = get_face_embedding(
    image_path
)

embedding_2 = get_face_embedding(
    image_path
)

similarity = cosine_similarity(
    embedding_1,
    embedding_2,
)

print("Same-image similarity:")
print(similarity)