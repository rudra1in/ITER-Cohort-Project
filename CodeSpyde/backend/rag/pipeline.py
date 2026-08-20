from retrieval.retriever import (
    DSAQuery,
    retrieve
)

from rag.context_builder import (
    build_context
)

from rag.prompts import (
    build_coach_prompt
)


def build_debug_query(
    problem: dict,
    code: str,
    execution_result: dict,
    syntax_result: dict
) -> str:

    return f"""
DSA Problem:
{problem.get("title", "")}

Topic:
{problem.get("topic", "")}

Pattern:
{problem.get("pattern", "")}

Difficulty:
{problem.get("difficulty", "")}

Student Code:
{code}

Static Analysis:
{syntax_result}

Execution Result:
{execution_result}
""".strip()


def run_coach_rag(
    problem: dict,
    code: str,
    execution_result: dict,
    syntax_result: dict,
    student_history: list[dict],
    recurring_errors: list[dict],
    request_type: str,
    hint_level: int
) -> dict:

    # -----------------------------------------------------
    # Build retrieval query
    # -----------------------------------------------------

    query_text = build_debug_query(
        problem=problem,
        code=code,
        execution_result=execution_result,
        syntax_result=syntax_result
    )

    # -----------------------------------------------------
    # Metadata-aware retrieval
    # -----------------------------------------------------

    query = DSAQuery(
        query=query_text,

        topic=problem.get(
            "topic"
        ),

        subtopic=problem.get(
            "subtopic"
        ),

        pattern=problem.get(
            "pattern"
        ),

        difficulty=problem.get(
            "difficulty"
        )
    )

    # -----------------------------------------------------
    # Part 3
    # -----------------------------------------------------

    results = retrieve(
        query
    )

    # -----------------------------------------------------
    # Build Top-K context
    # -----------------------------------------------------

    context_data = build_context(
        results
    )

    # -----------------------------------------------------
    # Build final prompt
    # -----------------------------------------------------

    prompt = build_coach_prompt(
        problem=problem,

        student_code=code,

        execution_result=execution_result,

        syntax_result=syntax_result,

        retrieved_context=context_data[
            "context"
        ],

        student_history=student_history,

        recurring_errors=recurring_errors,

        request_type=request_type,

        hint_level=hint_level
    )

    return {
        "query": query_text,

        "prompt": prompt,

        "retrieved_results": results,

        "context": context_data,
    }