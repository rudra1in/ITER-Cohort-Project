from typing import List, Dict, Any, Set

from langchain_core.documents import Document
from sqlalchemy import text

from app.database.database import SessionLocal
from app.rag.embeddings import embed_query


# ============================================================
# TEXT NORMALIZATION
# ============================================================

def normalize_text(value: str) -> str:
    """
    Normalize text so problem names can be matched reliably.

    Examples:

        "3Sum Closest"       -> "3sum closest"
        "3sum_closest"       -> "3sum closest"
        "Problem 16: 3Sum"   -> "problem 16 3sum"
        "Meeting Rooms II"   -> "meeting rooms ii"
    """

    if not value:
        return ""

    return (
        value.lower()
        .replace("-", " ")
        .replace("_", " ")
        .replace(":", " ")
        .replace(",", " ")
        .strip()
    )


# ============================================================
# PROBLEM NAME MATCHING
# ============================================================

def remove_problem_prefix(value: str) -> str:
    """
    Remove prefixes such as:

        Problem 16
        Problem 253

    from a title.

    Example:

        "problem 16 3sum closest"
        ->
        "3sum closest"
    """

    normalized = normalize_text(value)

    if normalized.startswith("problem "):

        parts = normalized.split(" ", 2)

        if len(parts) == 3:
            return parts[2]

    return normalized


def problem_name_matches(
    query: str,
    title: str,
    problem_id: str,
) -> bool:
    """
    Determine whether the user explicitly mentioned
    the candidate problem.

    This is intentionally stronger than semantic similarity.

    Example:

        Query:
        "Explain 3Sum Closest and its two pointer approach."

        Candidate:
        Problem 16: 3Sum Closest

        -> True

    But:

        Query:
        "Explain 3Sum Closest..."

        Candidate:
        Problem 15: 3Sum

        -> False
    """

    query_normalized = normalize_text(query)

    title_normalized = normalize_text(title)
    problem_id_normalized = normalize_text(problem_id)

    # Remove "problem 16" / "problem 253" from title.
    title_without_prefix = remove_problem_prefix(title)

    # --------------------------------------------------------
    # Exact title match
    # --------------------------------------------------------

    if (
        title_normalized
        and title_normalized in query_normalized
    ):
        return True

    # --------------------------------------------------------
    # Title without "Problem N"
    # --------------------------------------------------------

    if (
        title_without_prefix
        and title_without_prefix in query_normalized
    ):
        return True

    # --------------------------------------------------------
    # Problem ID match
    #
    # Example:
    #
    # 3sum_closest -> 3sum closest
    # --------------------------------------------------------

    if (
        problem_id_normalized
        and problem_id_normalized in query_normalized
    ):
        return True

    return False


# ============================================================
# EXPLICIT PROBLEM DETECTION
# ============================================================

def extract_explicit_problem_candidates(
    query: str,
) -> Set[str]:
    """
    Detect well-known multi-word DSA problem names from the query.

    This helps prevent related problems from outranking the
    explicitly requested problem.

    Example:

        "Explain 3Sum Closest and its two pointer approach."

    returns:

        {"3sum closest"}

    """

    query_normalized = normalize_text(query)

    known_problem_names = [
        "3sum closest",
        "3sum smaller",
        "meeting rooms ii",
        "majority element ii",
        "contains duplicate ii",
        "contains duplicate iii",
        "intersection of two arrays ii",
        "kth largest element in an array",
        "kth smallest element in a sorted matrix",
        "minimum number of arrows to burst balloons",
        "find all duplicates in an array",
        "minimum moves to equal array elements ii",
        "sort colors",
        "group anagrams",
        "merge intervals",
        "non overlapping intervals",
        "queue reconstruction by height",
        "russian doll envelopes",
        "the skyline problem",
        "find median from data stream",
        "best meeting point",
        "reconstruct itinerary",
        "relative ranks",
        "largest divisible subset",
        "rearrange string k distance apart",
        "sort transformed array",
    ]

    matches = set()

    for problem_name in known_problem_names:

        if problem_name in query_normalized:
            matches.add(problem_name)

    return matches


# ============================================================
# CANONICAL PROBLEM ID
# ============================================================

def canonical_problem_id(
    title: str,
    problem_id: str,
) -> str:
    """
    Produce a normalized representation of a problem.

    Example:

        title = "Problem 16: 3Sum Closest"
        problem_id = "3sum_closest"

        -> "3sum closest"
    """

    normalized_id = normalize_text(problem_id)

    if normalized_id:
        return normalized_id

    return remove_problem_prefix(title)


# ============================================================
# RELATED PROBLEM PENALTY
# ============================================================

def related_problem_penalty(
    query: str,
    candidate_problem_id: str,
    candidate_title: str,
) -> float:
    """
    Penalize a candidate when the query explicitly names
    another, different problem.

    This is particularly important for problems such as:

        3Sum
        3Sum Closest
        3Sum Smaller

    or:

        Contains Duplicate
        Contains Duplicate II
        Contains Duplicate III

    Semantic embeddings naturally consider these problems
    very similar. This penalty protects the explicitly
    requested problem.
    """

    query_normalized = normalize_text(query)

    candidate_id = normalize_text(candidate_problem_id)

    penalty = 0.0

    # --------------------------------------------------------
    # 3Sum family
    # --------------------------------------------------------

    if "3sum closest" in query_normalized:

        if candidate_id == "3sum":
            penalty += 0.35

        elif candidate_id == "3sum smaller":
            penalty += 0.30

    elif "3sum smaller" in query_normalized:

        if candidate_id == "3sum":
            penalty += 0.35

        elif candidate_id == "3sum closest":
            penalty += 0.30

    # --------------------------------------------------------
    # Meeting Rooms family
    # --------------------------------------------------------

    if "meeting rooms ii" in query_normalized:

        if candidate_id == "meeting rooms":
            penalty += 0.35

    # --------------------------------------------------------
    # Majority Element family
    # --------------------------------------------------------

    if "majority element ii" in query_normalized:

        if candidate_id == "majority element":
            penalty += 0.35

    # --------------------------------------------------------
    # Contains Duplicate family
    # --------------------------------------------------------

    if "contains duplicate iii" in query_normalized:

        if candidate_id == "contains duplicate":
            penalty += 0.35

        elif candidate_id == "contains duplicate ii":
            penalty += 0.30

    elif "contains duplicate ii" in query_normalized:

        if candidate_id == "contains duplicate":
            penalty += 0.35

        elif candidate_id == "contains duplicate iii":
            penalty += 0.30

    # --------------------------------------------------------
    # Intersection of Two Arrays family
    # --------------------------------------------------------

    if "intersection of two arrays ii" in query_normalized:

        if candidate_id == "intersection of two arrays":
            penalty += 0.35

    return penalty


# ============================================================
# SECTION QUALITY
# ============================================================

def section_score(section: str) -> float:
    """
    Return a reranking adjustment based on section quality.

    Lower score = better ranking because the final candidate
    score is sorted ascending.

    We prefer explanatory sections over generic metadata sections.
    """

    section = normalize_text(section)

    # --------------------------------------------------------
    # Highest-value sections
    # --------------------------------------------------------

    if section == "optimized approach":
        return -0.14

    if section == "key idea":
        return -0.12

    if section == "interview explanation":
        return -0.11

    if section == "algorithm":
        return -0.09

    # --------------------------------------------------------
    # Useful sections
    # --------------------------------------------------------

    if section in {
        "problem",
        "problem description",
    }:
        return -0.05

    if section == "hints":
        return -0.03

    if section == "common mistakes":
        return -0.02

    if section == "edge cases":
        return -0.01

    if section == "complexity analysis":
        return 0.00

    # --------------------------------------------------------
    # Lower-value sections
    # --------------------------------------------------------

    if section == "introduction":
        return 0.06

    if section == "pattern":
        return 0.05

    # --------------------------------------------------------
    # Default
    # --------------------------------------------------------

    return 0.00

# ============================================================
# GENERAL DSA CONCEPT ALIASES
# ============================================================

def get_concept_aliases() -> Dict[str, List[str]]:
    """
    Map common user terminology to equivalent DSA concepts.

    This makes conceptual questions work across the whole
    knowledge base instead of hardcoding one data structure.

    Example:

        "what is hashmap"
        "explain hash map"
        "what is a hash table"

    are all treated as the same general concept.
    """

    return {
        "linked list": [
            "linked list",
            "linkedlist",
            "singly linked list",
            "doubly linked list",
            "circular linked list",
        ],

        "hash map": [
            "hash map",
            "hashmap",
            "hash table",
            "hashtable",
            "map",
            "dictionary",
        ],

        "array": [
            "array",
            "arrays",
        ],

        "string": [
            "string",
            "strings",
        ],

        "stack": [
            "stack",
            "stacks",
        ],

        "queue": [
            "queue",
            "queues",
        ],

        "heap": [
            "heap",
            "heaps",
            "min heap",
            "max heap",
        ],

        "priority queue": [
            "priority queue",
            "priority queues",
        ],

        "tree": [
            "tree",
            "trees",
        ],

        "binary tree": [
            "binary tree",
            "binary trees",
        ],

        "binary search tree": [
            "binary search tree",
            "binary search trees",
            "bst",
        ],

        "graph": [
            "graph",
            "graphs",
        ],

        "binary search": [
            "binary search",
        ],

        "recursion": [
            "recursion",
            "recursive",
        ],

        "dynamic programming": [
            "dynamic programming",
            "dp",
        ],

        "greedy": [
            "greedy",
            "greedy algorithm",
        ],

        "backtracking": [
            "backtracking",
        ],

        "sliding window": [
            "sliding window",
        ],

        "two pointer": [
            "two pointer",
            "two pointers",
            "two pointer technique",
        ],
    }

# ============================================================
# CONCEPT DETECTION
# ============================================================

def detect_query_concepts(query: str) -> Set[str]:
    """
    Detect general DSA concepts explicitly mentioned by the user.

    Example:

        "What is a linked list?"

        -> {"linked list"}

        "Explain hashmap and its operations"

        -> {"hash map"}
    """

    query_normalized = normalize_text(query)

    aliases = get_concept_aliases()

    detected = set()

    for canonical_name, variations in aliases.items():

        for variation in variations:
            if variation in query_normalized:
                detected.add(canonical_name)
                break

    return detected

# ============================================================
# CONCEPT MATCH SCORE
# ============================================================

def concept_match_score(
    query: str,
    title: str,
    topic: str,
    problem_id: str,
    section: str,
    content: str,
) -> float:
    """
    Strongly rank chunks belonging to a concept explicitly
    mentioned by the user.

    This is especially important for conceptual questions like:

        "What is linked list?"
        "What is hashmap?"
        "Explain stack"
        "What is a binary tree?"

    Lower score = better.
    """

    detected_concepts = detect_query_concepts(query)

    if not detected_concepts:
         return 0.0

    title_normalized = normalize_text(title)
    topic_normalized = normalize_text(topic)
    problem_normalized = normalize_text(problem_id)
    section_normalized = normalize_text(section)
    content_normalized = normalize_text(content)

    aliases = get_concept_aliases()

    score = 0.0

    for concept in detected_concepts:

        variations = aliases.get(concept, [])

        direct_title_match = any(
            variation in title_normalized
            for variation in variations
        )

        direct_topic_match = any(
            variation in topic_normalized
            for variation in variations
        )

        direct_problem_match = any(
            variation in problem_normalized
            for variation in variations
        )

        direct_content_match = any(
            variation in content_normalized
            for variation in variations
        )

        # ----------------------------------------------------
        # Strongest: concept in title
        # ----------------------------------------------------

        if direct_title_match:
            score -= 0.25

        # ----------------------------------------------------
        # Strong: concept in topic
        # ----------------------------------------------------

        if direct_topic_match:
            score -= 0.22

        # ----------------------------------------------------
        # Strong: concept in problem ID
        # ----------------------------------------------------

        if direct_problem_match:
            score -= 0.20

        # ----------------------------------------------------
        # Weaker: concept only in content
        # ----------------------------------------------------
        elif direct_content_match:
            score -= 0.08

        # ----------------------------------------------------
        # Prefer explanatory sections for concept questions
        # ----------------------------------------------------

        if section_normalized in {
            "introduction",
            "definition",
            "overview",
            "problem",
            "problem description",
            "key idea",
            "interview explanation",
        }:
            score -= 0.15
    return score

# ============================================================
# QUERY INTENT / CONCEPT MATCHING
# ============================================================

def query_concept_score(
    query: str,
    title: str,
    problem_id: str,
    section: str,
    content: str,
) -> float:
    """
    Boost candidates that directly match the main concept
    asked about in the query.

    Lower final score = better candidate.
    """

    query_normalized = normalize_text(query)

    title_normalized = normalize_text(title)
    problem_normalized = normalize_text(problem_id)
    section_normalized = normalize_text(section)
    content_normalized = normalize_text(content)

    score = 0.0

    # --------------------------------------------------------
    # IMPORTANT DSA CONCEPTS
    # --------------------------------------------------------

    concepts = [
        "binary search",
        "linked list",
        "array",
        "string",
        "stack",
        "queue",
        "hash map",
        "hashmap",
        "heap",
        "priority queue",
        "two pointer",
        "two pointers",
        "sliding window",
        "recursion",
        "dynamic programming",
        "greedy",
        "backtracking",
        "graph",
        "tree",
        "binary tree",
        "binary search tree",
    ]

    for concept in concepts:

        if concept not in query_normalized:
            continue

        # Strongest: concept appears in title
        if concept in title_normalized:
            score -= 0.20

        # Strong: concept appears in problem ID
        elif concept in problem_normalized:
            score -= 0.18

        # Good: concept appears in content
        elif concept in content_normalized:
            score -= 0.08

    # --------------------------------------------------------
    # COMPLEXITY QUESTIONS
    # --------------------------------------------------------

    complexity_terms = [
        "time complexity",
        "space complexity",
        "complexity",
        "big o",
        "time",
        "space",
    ]

    complexity_query = any(
        term in query_normalized
        for term in complexity_terms
    )

    if complexity_query:

        if (
            "complexity analysis" in section_normalized
        ):
            score -= 0.18

        elif (
            "complexity" in section_normalized
        ):
            score -= 0.15

        # If the content actually discusses complexity,
        # prefer it over unrelated chunks.
        if (
            "time complexity" in content_normalized
        ):
            score -= 0.08

        if (
            "space complexity" in content_normalized
        ):
            score -= 0.05

    # --------------------------------------------------------
    # DEFINITION / WHAT-IS QUESTIONS
    # --------------------------------------------------------

    definition_query = (
        query_normalized.startswith("what is")
        or query_normalized.startswith("what are")
        or query_normalized.startswith("what's")
        or "define " in query_normalized
        or "definition" in query_normalized
        or "meaning of" in query_normalized
        or "explain " in query_normalized
    )

    if definition_query:

        if section_normalized in {
            "introduction",
            "definition",
            "overview",
            "problem",
            "problem description",
            "key idea",
            "interview explanation",
        }:
            score -= 0.15

        # A definition normally contains explanatory language.
        definition_terms = [
            "is a",
            "is an",
            "data structure",
            "consists of",
            "used to",
            "allows",
            "stores",
        ]

        definition_matches = sum(
            1
            for term in definition_terms
            if term in content_normalized
        )

        if definition_matches:
            score -= min(
                0.10,
                0.025 * definition_matches
            )

    return score

# ============================================================
# CODE INTENT SCORE
# ============================================================

def query_code_intent_score(
    query: str,
    title: str,
    problem_id: str,
    section: str,
    content: str,
) -> float:
    """
    Detect whether the user is asking for code/implementation
    and rerank candidates accordingly.

    Example:

        "Give me Java code for binary search"

    should prefer implementation-oriented chunks for
    the binary-search problem rather than unrelated Java
    problems such as Graph Representation in Java.

    Lower score = better candidate.
    """

    query_normalized = normalize_text(query)

    #title_normalized = normalize_text(title)
    #problem_normalized = normalize_text(problem_id)
    section_normalized = normalize_text(section)
    content_normalized = content.lower()

    score = 0.0

    # --------------------------------------------------------
    # Detect code-related intent
    # --------------------------------------------------------

    code_terms = [
        "code",
        "java code",
        "write code",
        "give code",
        "provide code",
        "implementation",
        "implement",
        "coding",
        "solution",
        "program",
        "programming",
    ]

    is_code_query = any(
        term in query_normalized
        for term in code_terms
    )

    if not is_code_query:
        return score

    # --------------------------------------------------------
    # Implementation-related sections
    # --------------------------------------------------------

    if "implementation" in section_normalized:
        score -= 0.18

    elif "code" in section_normalized:
        score -= 0.18

    elif "java solution" in section_normalized:
        score -= 0.18

    elif "solution" in section_normalized:
        score -= 0.14

    elif "optimized approach" in section_normalized:
        score -= 0.08

    elif "algorithm" in section_normalized:
        score -= 0.06

    elif "key idea" in section_normalized:
        score -= 0.03

    # --------------------------------------------------------
    # Java-specific intent
    # --------------------------------------------------------

    if "java" in query_normalized:

        if "public class" in content_normalized:
            score -= 0.04

        if "public static" in content_normalized:
            score -= 0.03

        if "int[]" in content_normalized:
            score -= 0.03

        # Only give a small boost for Java in the section.
        if "java" in section_normalized:
            score -= 0.05

    # --------------------------------------------------------
    # Prefer actual implementation/code content
    # --------------------------------------------------------

    implementation_terms = [
        "public class",
        "public static",
        "int[]",
        "while",
        "for",
        "return",
        "int mid",
        "int low",
        "int high",
        "implementation",
        "code",
    ]

    implementation_matches = sum(
        1
        for term in implementation_terms
        if term in content_normalized
    )

    if implementation_matches > 0:

        score -= min(
            0.10,
            0.02 * implementation_matches
        )

    # ========================================================
    # 5. BINARY SEARCH CODE INTENT
    # ========================================================

    # If the query explicitly asks for binary-search code,
    # favor binary-search implementation content.

    if "binary search" in query_normalized:

        binary_search_terms = [
            "binary search",
            "int low",
            "int high",
            "int mid",
            "mid =",
            "low =",
            "high =",
        ]

        binary_matches = sum(
            1
            for term in binary_search_terms
            if term in content_normalized
        )

        if binary_matches > 0:
            score -= min(
                0.14,
                0.025 * binary_matches
            )
    return score



# ============================================================
# CONCEPT ALIAS SCORE
# ============================================================

def concept_alias_score(
    query: str,
    title: str,
    problem_id: str,
    content: str,
) -> float:
    """
    Handle common conceptual relationships where the user's
    query may describe an algorithm rather than the exact
    problem title.

    Example:

        Query:
            "binary search"

        Candidate:
            "Search X in Sorted Array"

    This is a strong conceptual match even though
    "binary search" may not appear in the title itself.
    """

    query_normalized = normalize_text(query)

    title_normalized = normalize_text(title)

    problem_normalized = normalize_text(problem_id)
    content_normalized = normalize_text(content)

    score = 0.0

    # ========================================================
    # BINARY SEARCH
    # ========================================================

    if "binary search" in query_normalized:

        # Direct binary-search mention
        if "binary search" in title_normalized:
            score -= 0.18

        elif "binary search" in problem_normalized:
            score -= 0.16

        elif "binary search" in content_normalized:
            score -= 0.12

        # "Search X in Sorted Array" is a canonical
        # binary-search problem in this knowledge base.
        if "search x in sorted array" in title_normalized:
            score -= 0.25

        if "search x in sorted array" in problem_normalized:
            score -= 0.25

    # ========================================================
    # TWO POINTER
    # ========================================================

    if (
        "two pointer" in query_normalized
        or "two pointers" in query_normalized
    ):

        if "two pointer" in title_normalized:
            score -= 0.15

        elif "two pointer" in content_normalized:
            score -= 0.10

    # ========================================================
    # SLIDING WINDOW
    # ========================================================

    if "sliding window" in query_normalized:

        if "sliding window" in title_normalized:
            score -= 0.15

        elif "sliding window" in content_normalized:
            score -= 0.10

    return score

# ============================================================
# SIMILARITY SEARCH
# ============================================================

def similarity_search(
    query: str,
    top_k: int = 5,
) -> List[Document]:
    """
    Retrieve relevant DSA knowledge chunks from PostgreSQL
    using pgvector similarity search followed by deterministic
    metadata-aware reranking.

    Retrieval pipeline:

    1. Validate query.
    2. Generate query embedding.
    3. Retrieve a larger semantic candidate set.
    4. Detect explicit problem names.
    5. Strongly boost exact problem matches.
    6. Boost useful explanation sections.
    7. Penalize related-but-different problems.
    8. Apply keyword/pattern matching.
    9. Sort by final reranking score.
    10. Return top_k LangChain Documents.
    """

    if not query or not query.strip():
        return []

    # ========================================================
    # 1. EMBED QUERY
    # ========================================================

    query_embedding = embed_query(query)

    # ========================================================
    # 2. RETRIEVE LARGER CANDIDATE SET
    # ========================================================

    # We retrieve more than top_k because semantic similarity
    # may place a related problem above the exact problem.
    candidate_k = max(top_k * 10, 50)

    db = SessionLocal()

    try:

        sql = text(
            """
            SELECT
                id,
                problem_id,
                title,
                topic,
                difficulty,
                pattern,
                section,
                content,
                source,
                embedding <=> CAST(:query_embedding AS vector)
                    AS distance
            FROM knowledge_chunks
            ORDER BY embedding <=> CAST(:query_embedding AS vector)
            LIMIT :candidate_k
            """
        )

        result = db.execute(
            sql,
            {
                "query_embedding": str(query_embedding),
                "candidate_k": candidate_k,
            },
        )

        rows = result.fetchall()

        # ====================================================
        # 2B. EXACT / LEXICAL PROBLEM CANDIDATES
        # ====================================================
        #
        # pgvector finds semantically similar problems, but
        # semantic similarity can sometimes rank a related
        # problem above the exact problem requested by the user.
        #
        # This additional query searches the database directly
        # for a problem whose title or problem_id appears in the
        # user's query.
        #
        # This is general and does NOT require hardcoding problem
        # names such as Two Sum, 3Sum, etc.
        # ====================================================

        lexical_sql = text(
            """
            SELECT DISTINCT ON (problem_id)
                id,
                problem_id,
                title,
                topic,
                difficulty,
                pattern,
                section,
                content,
                source,
                0.0 AS distance
            FROM knowledge_chunks
            WHERE
                LOWER(:query) LIKE '%' || LOWER(title) || '%'
                OR
                LOWER(:query) LIKE '%' ||
                LOWER(REPLACE(problem_id, '_', ' ')) || '%'
            ORDER BY problem_id, id
            """
        )

        lexical_result = db.execute(
            lexical_sql,
            {
                "query": query,
            },
        )

        lexical_rows = lexical_result.fetchall()

        # ====================================================
        # MERGE LEXICAL RESULTS WITH SEMANTIC RESULTS
        # ====================================================

        existing_ids = {
            row.id
            for row in rows
        }

        for lexical_row in lexical_rows:

            if lexical_row.id not in existing_ids:

                rows.append(lexical_row)

                existing_ids.add(lexical_row.id)

        # ====================================================
        # 3. QUERY PREPARATION
        # ====================================================

        query_normalized = normalize_text(query)
        query_words = set(query_normalized.split())

        explicit_problem_names = (
            extract_explicit_problem_candidates(query)
        )

        detected_concepts = detect_query_concepts(query)

        # Is this primarily a conceptual question?
        definition_query = (
            query_normalized.startswith("what is")
            or query_normalized.startswith("what are")
            or query_normalized.startswith("what's")
            or "define " in query_normalized
            or "definition" in query_normalized
            or "meaning of" in query_normalized
        )

        candidates: List[Dict[str, Any]] = []

        # ====================================================
        # 4. RERANK
        # ====================================================

        for row in rows:

            title = normalize_text(row.title)
            problem_id = normalize_text(row.problem_id)
            topic = normalize_text(row.topic)
            pattern = normalize_text(row.pattern)
            section = normalize_text(row.section)
            content = normalize_text(row.content)

            original_distance = float(row.distance)

            # Start with vector similarity distance.
            #
            # Lower distance = better.
            score = original_distance

            # ==================================================
            # A. EXACT PROBLEM MATCH
            # ==================================================

            exact_problem_match = problem_name_matches(
                query=query,
                title=row.title,
                problem_id=row.problem_id,
            )

            if exact_problem_match:

                # VERY strong boost.
                #
                # This is the most important rule.
                score -= 0.30

            # ==================================================
            # B. EXPLICIT MULTI-WORD PROBLEM MATCH
            # ==================================================

            candidate_problem_name = canonical_problem_id(
                row.title,
                row.problem_id,
            )

            for explicit_name in explicit_problem_names:

                if explicit_name == candidate_problem_name:

                    # Additional protection for explicitly
                    # requested problem.
                    score -= 0.15

            # ==================================================
            # C. GENERAL CONCEPT MATCH
            # ==================================================

            if detected_concepts:

                score += concept_match_score(
                    query=query,
                    title=row.title,
                    topic=row.topic,
                    problem_id=row.problem_id,
                    section=row.section,
                    content=row.content,
                )

            # ==================================================
            # C. TITLE WORD OVERLAP
            # ==================================================

            title_words = set(title.split())

            title_overlap = query_words.intersection(
                title_words
            )

            if title_overlap:

                score -= min(
                    0.10,
                    0.03 * len(title_overlap)
                )

            # ==================================================
            # D. PROBLEM ID OVERLAP
            # ==================================================

            if (
                problem_id
                and problem_id in query_normalized
            ):

                score -= 0.15

            # ==================================================
            # F. TOPIC MATCH
            # ==================================================

            if detected_concepts:

                aliases = get_concept_aliases()

                for concept in detected_concepts:

                    variations = aliases.get(
                        concept,
                        [],
                    )

                    if any(
                        variation in topic
                        for variation in variations
                    ):

                        score -= 0.12

            # ==================================================
            # E. PATTERN MATCH
            # ==================================================

            pattern_words = set(
                pattern
                .replace("/", " ")
                .replace("+", " ")
                .replace("|", " ")
                .split()
            )

            pattern_overlap = query_words.intersection(
                pattern_words
            )

            if pattern_overlap:

                score -= min(
                    0.06,
                    0.02 * len(pattern_overlap)
                )

            # ==================================================
            # F. SECTION QUALITY
            # ==================================================

            score += section_score(section)

            # ==================================================
            # F2. CONCEPT / QUERY INTENT MATCH
            # ==================================================

            score += query_concept_score(
                query=query,
                title=row.title,
                problem_id=row.problem_id,
                section=row.section,
                content=row.content,
            )

            # =================================================
            # H. CODE INTENT MATCH
            # =================================================

            score += query_code_intent_score(
                query=query,
                title=row.title,
                problem_id=row.problem_id,
                section=row.section,
                content=row.content,
            )

            # =================================================
            # I. CONCEPT ALIAS MATCH
            # =================================================

            score += concept_alias_score(
                query=query,
                title=row.title,
                problem_id=row.problem_id,
                content=row.content,
            )

            # ==================================================
            # G. RELATED PROBLEM PENALTY
            # ==================================================

            score += related_problem_penalty(
                query=query,
                candidate_problem_id=row.problem_id,
                candidate_title=row.title,
            )

            # ==================================================
            # M. DEFINITION-SPECIFIC BOOST
            # ==================================================

            if definition_query and detected_concepts:

                # Prefer introduction / definition / overview.
                if section in {
                    "introduction",
                    "definition",
                    "overview",
                }:

                    score -= 0.20

                # Problem-description sections are also useful.
                elif section in {
                    "problem",
                    "problem description",
                }:

                    score -= 0.08

                # Prefer chunks that actually explain the concept.
                definition_terms = [
                    "is a",
                    "is an",
                    "data structure",
                    "consists of",
                    "stores",
                    "used to",
                    "allows",
                ]

                definition_matches = sum(
                    1
                    for term in definition_terms
                    if term in content
                )

                if definition_matches:

                    score -= min(
                        0.10,
                        0.02 * definition_matches
                    )


            # ==================================================
            # H. IMPORTANT CONTENT KEYWORDS
            # ==================================================

            important_keywords = [
                "two pointer",
                "two pointers",
                "target",
                "closest",
                "minimum difference",
                "sorted",
                "sorting",
                "min heap",
                "heap",
                "sliding window",
                "binary search",
                "hash map",
                "dynamic programming",
                "greedy",
            ]

            for keyword in important_keywords:

                if (
                    keyword in query_normalized
                    and keyword in content
                ):

                    score -= 0.015

            # ==================================================
            # I. QUERY WORD MATCH IN CONTENT
            # ==================================================

            content_words = set(content.split())

            content_overlap = query_words.intersection(
                content_words
            )

            if content_overlap:

                score -= min(
                    0.05,
                    0.005 * len(content_overlap)
                )

            # ==================================================
            # J. STORE CANDIDATE
            # ==================================================

            candidates.append(
                {
                    "row": row,
                    "score": score,
                    "distance": original_distance,
                    "exact_problem_match": exact_problem_match,
                }
            )

        # ========================================================
        # 5. SORT CANDIDATES
        # ========================================================

        # Exact problem matches are given priority first.
        #
        # This is deliberately deterministic. We don't want a
        # semantically similar problem such as "3Sum" to appear
        # above "3Sum Smaller" simply because its embedding
        # happened to be slightly closer.

        candidates.sort(
            key=lambda item: (
                not item["exact_problem_match"],
                item["score"],
            )
        )

        # ========================================================
        # 6. BUILD LANGCHAIN DOCUMENTS
        # ========================================================

        documents: List[Document] = []

        for candidate in candidates[:top_k]:

            row = candidate["row"]

            document = Document(
                page_content=row.content,

                metadata={
                    "id": row.id,
                    "problem_id": row.problem_id,
                    "title": row.title,
                    "topic": row.topic,
                    "difficulty": row.difficulty,
                    "pattern": row.pattern,
                    "section": row.section,
                    "source": row.source,

                    # Original vector distance.
                    "distance": candidate["distance"],

                    # Final reranking score.
                    "rerank_score": candidate["score"],

                    # Useful for debugging.
                    "exact_problem_match": (
                        candidate["exact_problem_match"]
                    ),
                },
            )

            documents.append(document)

        return documents

    finally:

        db.close()