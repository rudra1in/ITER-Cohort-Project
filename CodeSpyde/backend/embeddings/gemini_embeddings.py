from google import genai
from google.genai import types

from config import (
    GEMINI_API_KEY,
    GEMINI_EMBEDDING_MODEL,
    EMBEDDING_DIMENSION,
)


if not GEMINI_API_KEY:
    raise RuntimeError(
        "GEMINI_API_KEY is not configured."
    )


if not GEMINI_EMBEDDING_MODEL:
    raise RuntimeError(
        "GEMINI_EMBEDDING_MODEL is not configured."
    )


client = genai.Client(
    api_key=GEMINI_API_KEY
)


def create_embedding(
    text: str
) -> list[float]:
    """
    Generate one embedding for a DSA chunk.
    """

    if not text or not text.strip():

        raise ValueError(
            "Cannot embed empty text."
        )

    response = client.models.embed_content(
        model=GEMINI_EMBEDDING_MODEL,
        contents=text,
        config=types.EmbedContentConfig(
            output_dimensionality=EMBEDDING_DIMENSION
        )
    )

    if not response.embeddings:

        raise RuntimeError(
            "Embedding API returned no embeddings."
        )

    values = response.embeddings[0].values

    if len(values) != EMBEDDING_DIMENSION:

        raise RuntimeError(
            "Embedding dimension mismatch: "
            f"expected {EMBEDDING_DIMENSION}, "
            f"received {len(values)}"
        )

    return list(values)


def create_embeddings(
    texts: list[str]
) -> list[list[float]]:
    """
    Generate embeddings for multiple chunks.

    This function intentionally processes each item
    explicitly so failures can be identified easily.
    """

    embeddings = []

    for index, text in enumerate(texts):

        try:

            embedding = create_embedding(
                text
            )

            embeddings.append(
                embedding
            )

        except Exception as error:

            raise RuntimeError(
                f"Embedding failed for "
                f"item {index}: {error}"
            ) from error

    return embeddings