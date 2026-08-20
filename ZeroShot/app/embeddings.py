from sentence_transformers import SentenceTransformer

import numpy as np


class EmbeddingService:

    def __init__(
        self,
        model_name
    ):

        print(
            f"Loading embedding model: "
            f"{model_name}"
        )

        self.model = (
            SentenceTransformer(
                model_name
            )
        )

     
    # SINGLE
     

    def encode(
        self,
        text
    ):

        vector = self.model.encode(
            [text],
            normalize_embeddings=True
        )

        return np.asarray(
            vector,
            dtype="float32"
        )

     
    # BATCH
     

    def encode_batch(
        self,
        texts
    ):

        vectors = self.model.encode(
            texts,
            normalize_embeddings=True
        )

        return np.asarray(
            vectors,
            dtype="float32"
        )