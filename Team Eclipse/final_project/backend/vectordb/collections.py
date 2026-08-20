from backend.vectordb.client import get_chroma_client
from backend.vectordb.embeddings import get_local_embedding_function

def init_collections():
    client = get_chroma_client()
    embedding_fn = get_local_embedding_function()

    exam_rules_col = client.get_or_create_collection(
        name="exam_rules",
        embedding_function=embedding_fn,
        metadata={"hnsw:space": "cosine"}
    )

    transcripts_col = client.get_or_create_collection(
        name="session_transcripts",
        embedding_function=embedding_fn,
        metadata={"hnsw:space": "cosine"}
    )

    if exam_rules_col.count() == 0:
        rules = [
            "Students must maintain direct gaze on the screen at all times during the assessment.",
            "Secondary voices, background noise, whispering, or external speaking are strictly prohibited.",
            "No electronic devices, smartphones, secondary monitors, or textbooks are allowed in the testing field of view.",
            "Leaving the webcam frame or obstructing the camera lens is classified as a severe violation."
        ]
        ids = [f"rule_{i+1}" for i in range(len(rules))]
        metadatas = [{"category": "policy", "severity": "high"} for _ in rules]

        exam_rules_col.add(documents=rules, ids=ids, metadatas=metadatas)

    return exam_rules_col, transcripts_col

if __name__ == "__main__":
    init_collections()
