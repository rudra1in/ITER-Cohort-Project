from app.rag.generator import generate_answer


# ============================================================
# INTERVIEW AGENT
# ============================================================

def run_interview_agent(
    query: str,
    mode: str = "interview",
    language: str = "java",
    code: str = "",
    problem: dict | None = None,
    conversation: list | None = None,
    retrieved_documents: list | None = None,
):
    """
    DSA Interview Agent.

    Handles technical interview preparation,
    mock interview questions, and follow-up questions.

    Uses the documents retrieved by the LangGraph
    RAG retrieval node.
    """

    instruction = """
You are the DSA Interview Agent.

Your job is to help the user prepare for technical
DSA interviews.

Use:
- realistic interview-style questions
- simple and clear explanations
- step-by-step reasoning
- hints when appropriate
- follow-up questions when appropriate
- time complexity
- space complexity
- interview-oriented thinking

If the user asks for a mock interview:
- behave like an interviewer
- ask one question at a time
- do not immediately reveal the complete solution

If the user asks for an interview question:
- provide a realistic placement/interview-level question

Do not unnecessarily provide the complete solution unless
the user specifically asks for it.

Use the retrieved DSA knowledge as the primary source.
"""

    enhanced_query = f"""
You are the DSA Interview Agent inside a multi-agent
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
        
    )