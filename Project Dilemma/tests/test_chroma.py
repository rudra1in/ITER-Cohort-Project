from src.agents.face_embedding_agent import (
    get_face_embedding,
)

from src.vectorstore.chroma import (
    search_identity,
    store_identity,
)


embedding = get_face_embedding(
    "data/ids/test_img.jpg"
)


store_identity(
    identity_id="ashim_test",
    face_embedding=embedding,
    metadata={
        "name": "ASHIM ABINASH MISHRA",
        "type": "student_id",
    },
)


result = search_identity(
    embedding,
)


print("\nChroma IDs:")
print(result["ids"])

print("\nMetadata:")
print(result["metadatas"])

print("\nDistances:")
print(result["distances"])