from app.rag.generator import generate_answer


def run_hint_agent(
    query: str,
    mode: str = "hint",
    language: str = "java",
    code: str = "",
    problem: dict | None = None,
    conversation: list | None = None,
    retrieved_documents: list | None = None,
):
    """
    Hint Agent.

    Uses retrieved DSA knowledge to provide a hint
    without revealing the complete solution.
    """

    instruction = """
    You are the Hint Agent inside a multi-agent DSA Coach.

    The user wants guidance, NOT the solution.

    Rules:

    - Give only a hint.
    - Do NOT provide complete code.
    - Do NOT provide the complete algorithm.
    - Do NOT list all implementation steps.
    - Do NOT directly solve the problem.
    - Identify one important observation, pattern, or direction.
    - Ask a guiding question when useful.
    - If the user provides code, point out what they should investigate next.
    - Keep the response concise.
    """

    enhanced_query = f"""
You are the Hint Agent inside a multi-agent DSA Coach.

Your instruction:

{instruction}

User question:
{query}

Programming language:
{language}

Problem context:
{problem if problem else "No problem context provided."}

User code:
{code if code else "No code provided."}

Previous conversation:
{conversation if conversation else "No previous conversation."}

Use the retrieved DSA knowledge as the primary source
for your answer.
"""

    documents = retrieved_documents or []

    return generate_answer(
        query=enhanced_query,
        documents=documents,
        language=language,
    )