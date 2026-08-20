from collections import defaultdict

from sqlalchemy import text

from app.database.database import engine


def analyze_duplicates():
    print("\n" + "=" * 70)
    print("DSA KNOWLEDGE BASE DUPLICATE ANALYSIS")
    print("=" * 70)

    with engine.connect() as connection:

        # ---------------------------------------------------------
        # 1. Total number of stored chunks
        # ---------------------------------------------------------

        result = connection.execute(
            text("""
                SELECT COUNT(*)
                FROM knowledge_chunks;
            """)
        )

        total_chunks = result.scalar()

        print(f"\nTotal stored chunks: {total_chunks}")

        # ---------------------------------------------------------
        # 2. Number of unique problems
        # ---------------------------------------------------------

        result = connection.execute(
            text("""
                SELECT COUNT(DISTINCT problem_id)
                FROM knowledge_chunks;
            """)
        )

        unique_problems = result.scalar()

        print(f"Unique problems: {unique_problems}")

        # ---------------------------------------------------------
        # 3. Problems occurring more than once
        # ---------------------------------------------------------

        result = connection.execute(
            text("""
                SELECT
                    problem_id,
                    title,
                    COUNT(*) AS chunk_count
                FROM knowledge_chunks
                GROUP BY problem_id, title
                HAVING COUNT(*) > 1
                ORDER BY chunk_count DESC, problem_id;
            """)
        )

        duplicate_problems = result.fetchall()

        print(
            f"Problems with multiple chunks: "
            f"{len(duplicate_problems)}"
        )

        # ---------------------------------------------------------
        # 4. Show duplicate problem distribution
        # ---------------------------------------------------------

        print("\n" + "-" * 70)
        print("PROBLEMS WITH MULTIPLE CHUNKS")
        print("-" * 70)

        for row in duplicate_problems[:30]:

            problem_id = row[0]
            title = row[1]
            count = row[2]

            print(
                f"\n{problem_id}"
                f"\n  Title: {title}"
                f"\n  Chunks: {count}"
            )

        if len(duplicate_problems) > 30:
            print(
                f"\n... and "
                f"{len(duplicate_problems) - 30} more."
            )

        # ---------------------------------------------------------
        # 5. Problems appearing under multiple topics
        # ---------------------------------------------------------

        result = connection.execute(
            text("""
                SELECT
                    problem_id,
                    title,
                    COUNT(DISTINCT topic) AS topic_count,
                    STRING_AGG(
                        DISTINCT topic,
                        ', '
                        ORDER BY topic
                    ) AS topics
                FROM knowledge_chunks
                GROUP BY problem_id, title
                HAVING COUNT(DISTINCT topic) > 1
                ORDER BY topic_count DESC, problem_id;
            """)
        )

        multi_topic_problems = result.fetchall()

        print("\n" + "-" * 70)
        print("PROBLEMS APPEARING UNDER MULTIPLE TOPICS")
        print("-" * 70)

        print(
            f"\nFound {len(multi_topic_problems)} "
            f"problems appearing under multiple topics."
        )

        for row in multi_topic_problems[:50]:

            problem_id = row[0]
            title = row[1]
            topic_count = row[2]
            topics = row[3]

            print(
                f"\n{problem_id}"
                f"\n  Title: {title}"
                f"\n  Topic count: {topic_count}"
                f"\n  Topics: {topics}"
            )

        if len(multi_topic_problems) > 50:
            print(
                f"\n... and "
                f"{len(multi_topic_problems) - 50} more."
            )

        # ---------------------------------------------------------
        # 6. Same problem + same section occurring multiple times
        # ---------------------------------------------------------

        result = connection.execute(
            text("""
                SELECT
                    problem_id,
                    section,
                    COUNT(*) AS duplicate_count
                FROM knowledge_chunks
                GROUP BY problem_id, section
                HAVING COUNT(*) > 1
                ORDER BY duplicate_count DESC;
            """)
        )

        duplicate_sections = result.fetchall()

        print("\n" + "-" * 70)
        print("DUPLICATE PROBLEM + SECTION COMBINATIONS")
        print("-" * 70)

        print(
            f"\nFound {len(duplicate_sections)} "
            f"problem/section combinations appearing more than once."
        )

        for row in duplicate_sections[:50]:

            problem_id = row[0]
            section = row[1]
            count = row[2]

            print(
                f"\nProblem: {problem_id}"
                f"\nSection: {section}"
                f"\nCount: {count}"
            )

        if len(duplicate_sections) > 50:
            print(
                f"\n... and "
                f"{len(duplicate_sections) - 50} more."
            )

        # ---------------------------------------------------------
        # 7. Exact duplicate content
        # ---------------------------------------------------------

        result = connection.execute(
            text("""
                SELECT
                    COUNT(*) AS duplicate_groups
                FROM (
                    SELECT
                        content
                    FROM knowledge_chunks
                    GROUP BY content
                    HAVING COUNT(*) > 1
                ) AS duplicates;
            """)
        )

        exact_duplicate_groups = result.scalar()

        print("\n" + "-" * 70)
        print("EXACT DUPLICATE CONTENT")
        print("-" * 70)

        print(
            f"\nExact duplicate content groups: "
            f"{exact_duplicate_groups}"
        )

        # ---------------------------------------------------------
        # 8. Exact duplicate content + examples
        # ---------------------------------------------------------

        result = connection.execute(
            text("""
                SELECT
                    content,
                    COUNT(*) AS occurrence_count
                FROM knowledge_chunks
                GROUP BY content
                HAVING COUNT(*) > 1
                ORDER BY occurrence_count DESC;
            """)
        )

        exact_duplicates = result.fetchall()

        for index, row in enumerate(exact_duplicates[:20], start=1):

            content = row[0]
            count = row[1]

            preview = content.replace("\n", " ").strip()

            if len(preview) > 200:
                preview = preview[:200] + "..."

            print(
                f"\n[{index}] Occurrences: {count}"
                f"\n    {preview}"
            )

        # ---------------------------------------------------------
        # 9. Topic distribution
        # ---------------------------------------------------------

        result = connection.execute(
            text("""
                SELECT
                    topic,
                    COUNT(*) AS chunk_count,
                    COUNT(DISTINCT problem_id) AS problem_count
                FROM knowledge_chunks
                GROUP BY topic
                ORDER BY chunk_count DESC;
            """)
        )

        topic_distribution = result.fetchall()

        print("\n" + "-" * 70)
        print("TOPIC DISTRIBUTION")
        print("-" * 70)

        for row in topic_distribution:

            topic = row[0]
            chunk_count = row[1]
            problem_count = row[2]

            print(
                f"\n{topic}"
                f"\n  Chunks: {chunk_count}"
                f"\n  Problems: {problem_count}"
            )

        # ---------------------------------------------------------
        # 10. Summary
        # ---------------------------------------------------------

        print("\n" + "=" * 70)
        print("SUMMARY")
        print("=" * 70)

        print(f"\nTotal chunks:              {total_chunks}")
        print(f"Unique problems:           {unique_problems}")
        print(
            f"Problems with >1 chunk:   "
            f"{len(duplicate_problems)}"
        )
        print(
            f"Multi-topic problems:      "
            f"{len(multi_topic_problems)}"
        )
        print(
            f"Duplicate sections:        "
            f"{len(duplicate_sections)}"
        )
        print(
            f"Exact duplicate groups:    "
            f"{exact_duplicate_groups}"
        )

        print("\nAnalysis complete.")


if __name__ == "__main__":
    try:
        analyze_duplicates()

    except Exception as e:

        print("\nERROR")
        print("=" * 70)
        print(e)
        print("=" * 70)
        raise