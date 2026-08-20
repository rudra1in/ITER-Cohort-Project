from dataclasses import dataclass
from typing import Optional


@dataclass
class DSAChunk:
    chunk_type: str
    title: str
    content: str

    topic: Optional[str]
    subtopic: Optional[str]
    pattern: Optional[str]
    difficulty: Optional[str]

    code: Optional[str]
    language: Optional[str]

    time_complexity: Optional[str]
    space_complexity: Optional[str]

    source_reference: Optional[str]

    chunk_index: int = 0


def _value(
    document: dict,
    key: str
):

    value = document.get(key)

    if value is None:
        return None

    value = str(value).strip()

    return value or None


def _create_chunk(
    document: dict,
    chunk_type: str,
    title: str,
    content: str,
    index: int
) -> DSAChunk:

    return DSAChunk(
        chunk_type=chunk_type,
        title=title,
        content=content.strip(),

        topic=_value(
            document,
            "topic"
        ),

        subtopic=_value(
            document,
            "subtopic"
        ),

        pattern=_value(
            document,
            "pattern"
        ),

        difficulty=_value(
            document,
            "difficulty"
        ),

        code=_value(
            document,
            "code"
        ),

        language=_value(
            document,
            "language"
        ),

        time_complexity=_value(
            document,
            "time_complexity"
        ),

        space_complexity=_value(
            document,
            "space_complexity"
        ),

        source_reference=_value(
            document,
            "source"
        ) or _value(
            document,
            "_source_file"
        ),

        chunk_index=index
    )


def create_dsa_chunks(
    document: dict
) -> list[DSAChunk]:

    title = _value(
        document,
        "title"
    ) or "Untitled DSA Document"

    chunks = []

    # -----------------------------------------------------
    # Problem
    # -----------------------------------------------------

    problem = (
        document.get("problem")
        or document.get("description")
    )

    if problem:

        chunks.append(
            _create_chunk(
                document,
                "problem",
                title,
                str(problem),
                len(chunks)
            )
        )


    # -----------------------------------------------------
    # Intuition
    # -----------------------------------------------------

    intuition = document.get(
        "intuition"
    )

    if intuition:

        chunks.append(
            _create_chunk(
                document,
                "intuition",
                f"{title} - Intuition",
                str(intuition),
                len(chunks)
            )
        )


    # -----------------------------------------------------
    # Approach
    # -----------------------------------------------------

    approach = document.get(
        "approach"
    )

    if approach:

        chunks.append(
            _create_chunk(
                document,
                "approach",
                f"{title} - Approach",
                str(approach),
                len(chunks)
            )
        )


    # -----------------------------------------------------
    # Algorithm
    # -----------------------------------------------------

    algorithm = document.get(
        "algorithm"
    )

    if algorithm:

        chunks.append(
            _create_chunk(
                document,
                "algorithm",
                f"{title} - Algorithm",
                str(algorithm),
                len(chunks)
            )
        )


    # -----------------------------------------------------
    # Examples
    # -----------------------------------------------------

    examples = document.get(
        "examples"
    )

    if examples:

        if isinstance(
            examples,
            list
        ):

            example_text = "\n\n".join(
                str(example)
                for example in examples
            )

        else:

            example_text = str(
                examples
            )

        chunks.append(
            _create_chunk(
                document,
                "example",
                f"{title} - Examples",
                example_text,
                len(chunks)
            )
        )


    # -----------------------------------------------------
    # Common mistakes
    # -----------------------------------------------------

    mistakes = document.get(
        "mistakes"
    )

    if mistakes:

        if isinstance(
            mistakes,
            list
        ):

            mistake_text = "\n".join(
                f"- {item}"
                for item in mistakes
            )

        else:

            mistake_text = str(
                mistakes
            )

        chunks.append(
            _create_chunk(
                document,
                "mistakes",
                f"{title} - Common Mistakes",
                mistake_text,
                len(chunks)
            )
        )


    # -----------------------------------------------------
    # Complexity
    # -----------------------------------------------------

    complexity_parts = []

    if document.get(
        "time_complexity"
    ):

        complexity_parts.append(
            "Time Complexity: "
            + str(
                document[
                    "time_complexity"
                ]
            )
        )

    if document.get(
        "space_complexity"
    ):

        complexity_parts.append(
            "Space Complexity: "
            + str(
                document[
                    "space_complexity"
                ]
            )
        )

    if complexity_parts:

        chunks.append(
            _create_chunk(
                document,
                "complexity",
                f"{title} - Complexity",
                "\n".join(
                    complexity_parts
                ),
                len(chunks)
            )
        )


    # -----------------------------------------------------
    # Solution
    # -----------------------------------------------------

    solution = document.get(
        "solution"
    )

    code = document.get(
        "code"
    )

    solution_parts = []

    if solution:
        solution_parts.append(
            str(solution)
        )

    if code:
        solution_parts.append(
            "\nCode:\n"
            + str(code)
        )

    if solution_parts:

        chunks.append(
            _create_chunk(
                document,
                "solution",
                f"{title} - Solution",
                "\n".join(
                    solution_parts
                ),
                len(chunks)
            )
        )


    # -----------------------------------------------------
    # Fallback
    # -----------------------------------------------------

    if not chunks:

        content = document.get(
            "content"
        )

        if content:

            chunks.append(
                _create_chunk(
                    document,
                    "general",
                    title,
                    str(content),
                    0
                )
            )


    return chunks