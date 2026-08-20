from config import FINAL_CONTEXT_LIMIT


def _clean_text(
    value
) -> str:

    if value is None:

        return ""

    return str(
        value
    ).strip()


def build_context(
    results: list[dict],
    max_chunks: int = FINAL_CONTEXT_LIMIT
) -> dict:

    selected = results[
        :max_chunks
    ]

    sections = []

    sources = []

    for result in selected:

        rank = result[
            "rank"
        ]

        title = _clean_text(
            result["title"]
        )

        content = _clean_text(
            result["content"]
        )

        chunk_type = _clean_text(
            result["chunk_type"]
        )

        topic = _clean_text(
            result["topic"]
        )

        pattern = _clean_text(
            result["pattern"]
        )

        difficulty = _clean_text(
            result["difficulty"]
        )

        complexity = []

        if result[
            "time_complexity"
        ]:

            complexity.append(
                "Time: "
                + str(
                    result[
                        "time_complexity"
                    ]
                )
            )

        if result[
            "space_complexity"
        ]:

            complexity.append(
                "Space: "
                + str(
                    result[
                        "space_complexity"
                    ]
                )
            )

        complexity_text = (
            " | ".join(complexity)
            if complexity
            else "Not specified"
        )

        section = f"""
SOURCE {rank}

Title: {title}
Chunk Type: {chunk_type}
Topic: {topic}
Pattern: {pattern}
Difficulty: {difficulty}

Complexity:
{complexity_text}

Knowledge:
{content}
""".strip()

        sections.append(
            section
        )

        sources.append(
            {
                "rank": rank,
                "chunk_id":
                    result["chunk_id"],
                "document_id":
                    result["document_id"],
                "title": title,
                "chunk_type":
                    chunk_type,
                "topic": topic,
                "pattern": pattern,
                "source_reference":
                    result[
                        "source_reference"
                    ],
                "retrieval_score":
                    result[
                        "final_score"
                    ]
            }
        )

    context = (
        "\n\n"
        + "\n\n-------------------------\n\n"
        .join(sections)
    )

    return {
        "context": context.strip(),
        "sources": sources,
        "count": len(selected)
    }