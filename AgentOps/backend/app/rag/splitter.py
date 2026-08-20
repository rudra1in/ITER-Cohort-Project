import re
from typing import List

from langchain_core.documents import Document


SECTION_PATTERN = re.compile(
    r"^##\s+(.+?)\s*$",
    re.MULTILINE,
)


def normalize_section_name(section_name: str) -> str:
    """
    Convert a Markdown section title into a metadata-friendly name.

    Example:
        Optimized Approach
        -> optimized_approach
    """

    section_name = section_name.strip().lower()

    section_name = re.sub(
        r"[^a-z0-9]+",
        "_",
        section_name,
    )

    return section_name.strip("_")


def split_markdown_sections(
    document: Document,
) -> List[Document]:
    """
    Split a DSA problem into self-contained semantic chunks.

    Every chunk includes:
        - Problem title
        - Problem ID
        - Difficulty
        - Pattern
        - Section name
        - Section content

    This prevents generic sections from losing their
    problem context during embedding.
    """

    content = document.page_content.strip()

    if not content:
        return []

    matches = list(
        SECTION_PATTERN.finditer(content)
    )

    metadata = document.metadata

    problem_id = metadata.get(
        "problem_id",
        "unknown",
    )

    title = metadata.get(
        "title",
        "Unknown Problem",
    )

    difficulty = metadata.get(
        "difficulty",
        "unknown",
    )

    pattern = metadata.get(
        "pattern",
        "unknown",
    )

    topic = metadata.get(
        "topic",
        "unknown",
    )

    chunks: List[Document] = []

    # --------------------------------------------------
    # Handle content before first ## section
    # --------------------------------------------------

    introduction = content[
        :matches[0].start()
    ].strip() if matches else content

    # Do not create useless chunks containing only
    # the "# Problem Name" heading.
    #
    # We only keep introduction content if it has
    # meaningful information.
    if introduction:

        introduction_without_heading = re.sub(
            r"^#\s+.+?\n*",
            "",
            introduction,
            count=1,
            flags=re.MULTILINE,
        ).strip()

        if introduction_without_heading:

            chunk_text = f"""Problem: {title}
Problem ID: {problem_id}
Difficulty: {difficulty}
Topic: {topic}
Pattern: {pattern}

Section: Introduction

{introduction_without_heading}
"""

            chunks.append(
                Document(
                    page_content=chunk_text.strip(),
                    metadata={
                        **metadata,
                        "section": "introduction",
                        "section_title": "Introduction",
                        "chunk_index": 0,
                    },
                )
            )

    # --------------------------------------------------
    # Extract ## sections
    # --------------------------------------------------

    for index, match in enumerate(matches):

        section_title = match.group(1).strip()

        section_start = match.end()

        if index + 1 < len(matches):

            section_end = matches[
                index + 1
            ].start()

        else:

            section_end = len(content)

        section_content = content[
            section_start:section_end
        ].strip()

        if not section_content:
            continue

        normalized_section = (
            normalize_section_name(
                section_title
            )
        )

        # --------------------------------------------------
        # Remove redundant horizontal separators
        # --------------------------------------------------

        section_content = re.sub(
            r"^\s*---\s*$",
            "",
            section_content,
            flags=re.MULTILINE,
        ).strip()

        # --------------------------------------------------
        # Build self-contained chunk
        # --------------------------------------------------

        chunk_text = f"""Problem: {title}
Problem ID: {problem_id}
Difficulty: {difficulty}
Topic: {topic}
Pattern: {pattern}

Section: {section_title}

{section_content}
"""

        chunk_metadata = {
            **metadata,
            "section": normalized_section,
            "section_title": section_title,
            "chunk_index": index + 1,
        }

        chunks.append(
            Document(
                page_content=chunk_text.strip(),
                metadata=chunk_metadata,
            )
        )

    return chunks


def split_documents(
    documents: List[Document],
) -> List[Document]:
    """
    Split all DSA documents into self-contained
    semantic chunks.
    """

    all_chunks: List[Document] = []

    for document in documents:

        chunks = split_markdown_sections(
            document
        )

        all_chunks.extend(chunks)

    print(
        f"Created {len(all_chunks)} semantic chunks."
    )

    return all_chunks