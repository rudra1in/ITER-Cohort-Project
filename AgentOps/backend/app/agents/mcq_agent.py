from app.rag.generator import generate_answer


# ============================================================
# MCQ AGENT
# ============================================================

def run_mcq_agent(
    query: str,
    mode: str = "mcq",
    language: str = "java",
    code: str = "",
    problem: dict | None = None,
    conversation: list | None = None,
    retrieved_documents: list | None = None,
):
    """
    DSA MCQ Agent.

    Handles DSA multiple-choice questions,
    answers, and explanations.

    Uses the documents retrieved by the LangGraph
    RAG retrieval node.
    """

    instruction = """
You are the DSA MCQ Agent.

Your job is to help the user practice DSA
multiple-choice questions.

Use:
- accurate DSA concepts
- realistic placement-level questions
- four options when generating an MCQ
- clear explanations
- reasoning behind the correct answer
- explanations of incorrect options when useful
- time complexity when relevant
- space complexity when relevant

Do not create ambiguous questions.

If the user asks for an MCQ:
- provide a clear question
- provide four options
- allow the user to answer before revealing the answer
  when appropriate

If the user asks for the answer:
- clearly identify the correct option
- explain why it is correct

Use the retrieved DSA knowledge as the primary source.
"""

    enhanced_query = f"""
You are the DSA MCQ Agent inside a multi-agent
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