from typing import Optional

from retrieval.hybrid_search import (
    hybrid_search
)

from retrieval.reranker import (
    rerank
)

from config import (
    HYBRID_SEARCH_LIMIT,
    RERANK_LIMIT
)


class DSAQuery:

    def __init__(
        self,
        query: str,
        topic: Optional[str] = None,
        subtopic: Optional[str] = None,
        pattern: Optional[str] = None,
        difficulty: Optional[str] = None,
        chunk_type: Optional[str] = None
    ):

        self.query = query

        self.topic = topic
        self.subtopic = subtopic
        self.pattern = pattern
        self.difficulty = difficulty
        self.chunk_type = chunk_type


def retrieve(
    query: DSAQuery
) -> list[dict]:

    # -----------------------------------------------------
    # Stage 1:
    # Hybrid candidate retrieval
    # -----------------------------------------------------

    candidates = hybrid_search(
        query=query.query,

        topic=query.topic,

        subtopic=query.subtopic,

        pattern=query.pattern,

        difficulty=query.difficulty,

        chunk_type=query.chunk_type,

        limit=HYBRID_SEARCH_LIMIT
    )

    if not candidates:

        return []

    # -----------------------------------------------------
    # Stage 2:
    # Cross-encoder reranking
    # -----------------------------------------------------

    final_results = rerank(
        candidates=candidates,
        query=query.query,
        limit=RERANK_LIMIT
    )

    # -----------------------------------------------------
    # Normalize output
    # -----------------------------------------------------

    results = []

    for rank, item in enumerate(
        final_results,
        start=1
    ):

        chunk = item[
            "chunk"
        ]

        results.append(
            {
                "rank": rank,

                "chunk_id": str(
                    chunk["id"]
                ),

                "document_id": str(
                    chunk["document_id"]
                ),

                "chunk_type":
                    chunk["chunk_type"],

                "title":
                    chunk["title"],

                "content":
                    chunk["content"],

                "topic":
                    chunk["topic"],

                "subtopic":
                    chunk["subtopic"],

                "pattern":
                    chunk["pattern"],

                "difficulty":
                    chunk["difficulty"],

                "code":
                    chunk["code"],

                "language":
                    chunk["language"],

                "time_complexity":
                    chunk[
                        "time_complexity"
                    ],

                "space_complexity":
                    chunk[
                        "space_complexity"
                    ],

                "source_reference":
                    chunk[
                        "source_reference"
                    ],

                "hybrid_score":
                    item[
                        "rrf_score"
                    ],

                "rerank_score":
                    item[
                        "rerank_score"
                    ],

                "final_score":
                    item[
                        "final_score"
                    ]
            }
        )

    return results