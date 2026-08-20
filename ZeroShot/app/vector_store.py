import json
from pathlib import Path
import faiss
import numpy as np


class FAISSVectorStore:

    def __init__(
        self,
        directory,
        dimension
    ):

        self.directory = Path(
            directory
        )

        self.directory.mkdir(
            parents=True,
            exist_ok=True
        )

        self.index_path = (
            self.directory
            / "events.faiss"
        )

        self.metadata_path = (
            self.directory
            / "events.json"
        )

        self.dimension = dimension

        self.metadata = []

        self.index = (
            self.load_or_create()
        )

    # LOAD / CREATE

    def load_or_create(
        self
    ):

        if (
            self.index_path.exists()
            and self.metadata_path.exists()
        ):

            index = faiss.read_index(
                str(self.index_path)
            )

            with open(
                self.metadata_path,
                "r",
                encoding="utf-8"
            ) as file:

                self.metadata = json.load(
                    file
                )

            return index

        return faiss.IndexFlatIP(
            self.dimension
        )
    
    # ADDing

    def add(
        self,
        vectors,
        metadata
    ):

        vectors = np.asarray(
            vectors,
            dtype="float32"
        )

        if vectors.ndim == 1:

            vectors = vectors.reshape(
                1,
                -1
            )

        if vectors.shape[1] != (
            self.dimension
        ):

            raise ValueError(
                "Vector dimension mismatch"
            )

        faiss.normalize_L2(
            vectors
        )

        self.index.add(
            vectors
        )

        self.metadata.extend(
            metadata
        )

        self.save()

    # REMOVE 
    

    def remove_by_test(
        self,
        test_id
    ):

        keep_indices = [

            i for i, item in enumerate( self.metadata )
            if item.get(
                "test_id"
            ) != test_id

        ]
        if len(keep_indices) == len( self.metadata):
            return

        if keep_indices:

            vectors = np.vstack(
                [
                    self.index.reconstruct(i)
                    for i in keep_indices
                ]
            ).astype("float32")

        else:

            vectors = np.zeros(
                (0, self.dimension),
                dtype="float32"
            )

        new_metadata = [
            self.metadata[i]
            for i in keep_indices
        ]

        new_index = faiss.IndexFlatIP(
            self.dimension
        )

        if len(vectors) > 0:

            new_index.add(
                vectors
            )

        self.index = new_index

        self.metadata = new_metadata

        self.save()

    # SEARCH

    def search(
        self,
        query_vector,
        top_k=8
    ):

        if self.index.ntotal == 0:

            return []

        query_vector = np.asarray(
            query_vector,
            dtype="float32"
        )

        if query_vector.ndim == 1:

            query_vector = (
                query_vector.reshape(
                    1,
                    -1
                )
            )

        faiss.normalize_L2(
            query_vector
        )

        k = min(
            top_k,
            self.index.ntotal
        )

        scores, indices = (
            self.index.search(
                query_vector,
                k
            )
        )

        results = []

        for score, index in zip(
            scores[0],
            indices[0]
        ):

            if index < 0:

                continue

            item = dict(
                self.metadata[index]
            )

            item[
                "vector_score"
            ] = float(score)

            results.append(
                item
            )

        return results

    # SAVE

    def save(
        self
    ):

        faiss.write_index(
            self.index,
            str(self.index_path)
        )

        with open(
            self.metadata_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                self.metadata,
                file,
                indent=2,
                ensure_ascii=False
            )

    # COUNT

    def count(
        self
    ):

        return self.index.ntotal