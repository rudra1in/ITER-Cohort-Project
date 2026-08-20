from app.rag.generator import generate_answer


# ============================================================
# ROADMAP AGENT
# ============================================================

def run_roadmap_agent(
    query: str,
    mode: str = "roadmap",
    language: str = "java",
    code: str = "",
    problem: dict | None = None,
    conversation: list | None = None,
    retrieved_documents: list | None = None,
):
    """
    DSA Roadmap Agent.

    Helps the user decide what DSA topics to study,
    in what order, and what to learn next.

    Uses the documents retrieved by the LangGraph
    RAG retrieval node.
    """

    instruction = """
You are the DSA Roadmap Agent.

Your job is to help the user plan and navigate
their DSA learning journey.

Use:
- logical topic progression
- prerequisite relationships
- DSA patterns
- beginner → intermediate → advanced progression
- practical problem-solving progression
- interview preparation relevance

When recommending what to learn next:
- consider what the user already knows
- identify prerequisite topics
- explain why the next topic is useful

When creating a roadmap:
- organize topics in a sensible order
- avoid unnecessary topics
- keep the roadmap practical
- include practice recommendations when useful

Use the retrieved DSA knowledge as the primary source.
"""

    enhanced_query = f"""
You are the DSA Roadmap Agent inside a multi-agent
DSA Coach.

Your instruction:

{instruction}

User question:
{query}

Interaction mode:
{mode}

Programming language:
{language}

Problem context:
{problem if problem else "No problem context provided."}

Previous conversation:
{conversation if conversation else "No previous conversation."}

Use the retrieved DSA knowledge as the primary source
for your answer.
"""

    documents = retrieved_documents or []

    return generate_answer(
        query=enhanced_query,
        documents=documents,
        
    )