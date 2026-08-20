from typing import List

from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings


MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


def create_embedding_model() -> HuggingFaceEmbeddings:
    """
    Create the local embedding model used by the DSA RAG system.
    """

    return HuggingFaceEmbeddings(
        model_name=MODEL_NAME,
        model_kwargs={
            "device": "cpu",
        },
        encode_kwargs={
            "normalize_embeddings": True,
        },
    )


def embed_documents(
    documents: List[Document],
) -> List[List[float]]:
    """
    Convert document chunks into embedding vectors.
    """

    embedding_model = create_embedding_model()

    texts = [
        document.page_content
        for document in documents
    ]

    embeddings = embedding_model.embed_documents(texts)

    return embeddings


def embed_query(
    query: str,
) -> List[float]:
    """
    Convert a user query into an embedding vector.
    """

    embedding_model = create_embedding_model()

    return embedding_model.embed_query(query)