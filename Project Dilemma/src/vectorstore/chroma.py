import chromadb


client = chromadb.PersistentClient(
    path="data/chroma"
)

collection = client.get_or_create_collection(
    name="identity_faces"
)


def store_identity(
    identity_id: str,
    face_embedding: list[float],
    metadata: dict,
) -> None:
    """Store an ID face embedding in ChromaDB."""

    collection.upsert(
        ids=[identity_id],
        embeddings=[face_embedding],
        metadatas=[metadata],
    )


def search_identity(
    face_embedding: list[float],
    n_results: int = 1,
) -> dict:
    """Find the closest stored ID face embedding."""

    return collection.query(
        query_embeddings=[face_embedding],
        n_results=n_results,
    )


def clear_collection() -> None:
    """Delete the current collection."""

    global collection

    client.delete_collection(
        name="identity_faces"
    )

    collection = client.get_or_create_collection(
        name="identity_faces"
    )