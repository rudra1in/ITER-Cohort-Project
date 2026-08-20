from app.agents.graph.state import CoachState

from app.agents.coach_agent import run_coach_agent
from app.agents.code_agent import run_code_agent
from app.agents.hint_agent import run_hint_agent
from app.agents.interview_agent import run_interview_agent
from app.agents.mcq_agent import run_mcq_agent
from app.agents.roadmap_agent import run_roadmap_agent

from app.rag.retriever import similarity_search

def normalize_answer(answer) -> str:
    """
    Convert Gemini/LangChain response content into a plain string.
    """

    if answer is None:
        return ""

    # Already a normal string
    if isinstance(answer, str):
        return answer

    # Gemini/LangChain may return a list of content blocks
    if isinstance(answer, list):
        parts = []

        for item in answer:
            if isinstance(item, str):
                parts.append(item)

            elif isinstance(item, dict):
                text = item.get("text")

                if text:
                    parts.append(str(text))

            else:
                # Handle objects that may expose `.text`
                text = getattr(item, "text", None)

                if text:
                    parts.append(str(text))

        return "\n".join(parts).strip()

    # Fallback
    return str(answer).strip()

# ============================================================
# CONVERSATION QUERY RESOLUTION
# ============================================================

def resolve_conversation_query(state: CoachState) -> str:
    """
    Resolve follow-up questions using the existing conversation.

    Example:

        Previous:
            User: Explain binary search
            Assistant: Binary Search is...

        Current:
            User: What is its time complexity?

        Resolved query:
            What is the time complexity of Binary Search?

    This is intentionally deterministic for now.
    The retrieved conversation is passed directly to the
    retrieval system so the current question can be understood
    in context.
    """

    message = state.get("message", "").strip()

    if not message:
        return ""

    conversation = state.get(
        "conversation",
        [],
    )

    if not conversation:
        return message

    # --------------------------------------------------------
    # Get recent conversation
    # --------------------------------------------------------

    recent_conversation = conversation[-6:]

    conversation_lines = []

    for item in recent_conversation:

        role = item.get(
            "role",
            "",
        )

        content = item.get(
            "content",
            "",
        )

        if content:

            conversation_lines.append(
                f"{role}: {content}"
            )

    if not conversation_lines:
        return message

    conversation_context = "\n".join(
        conversation_lines
    )

    # --------------------------------------------------------
    # For follow-up questions, keep the current question
    # together with the previous conversation.
    #
    # This allows the retriever/agent to understand words
    # such as:
    #
    #   it
    #   its
    #   this
    #   that
    #   the above approach
    #   this algorithm
    # --------------------------------------------------------

    return f"""
Current user question:
{message}

Recent conversation:
{conversation_context}

Use the recent conversation to identify what the current
question refers to.

The current question should be interpreted in the context
of the previous conversation.
""".strip()

# ============================================================
# MEMORY NODE
# ============================================================

def memory_node(state: CoachState) -> CoachState:
    """
    Add the current user message to conversation memory.

    CoachState.conversation uses operator.add, so this
    message is appended to the existing conversation history.
    """

    message = state.get("message", "")

    if not message:
        return {}

    return {
        "conversation": [
            {
                "role": "user",
                "content": message,
            }
        ]
    }


# ============================================================
# ROUTER NODE
# ============================================================

def router_node(state: CoachState) -> CoachState:
    """
    Decide which specialized agent should handle the request.

    The selected agent is stored in agent_type.
    """

    message = state.get("message", "").lower().strip()
    mode = state.get("mode", "").lower().strip()

    # ========================================================
    # KEYWORDS
    # ========================================================

    code_keywords = [
        "my code",
        "my solution",
        "why does my code",
        "debug",
        "debugging",
        "bug",
        "error",
        "wrong answer",
        "runtime error",
        "compile error",
        "time complexity of my code",
        "space complexity of my code",
    ]

    hint_keywords = [
        "give me a hint",
        "give hint",
        "hint",
        "don't give me the answer",
        "do not give me the answer",
        "without giving the answer",
        "don't tell me the answer",
        "do not tell me the answer",
        "without the answer",
        "help me think",
    ]

    interview_keywords = [
        "interview question",
        "interview questions",
        "mock interview",
        "interview prep",
        "interview preparation",
        "ask me an interview question",
        "technical interview",
    ]

    mcq_keywords = [
        "mcq",
        "multiple choice",
        "multiple choice question",
        "quiz me",
        "quiz",
        "practice questions",
    ]

    roadmap_keywords = [
        "roadmap",
        "learning path",
        "what should i learn",
        "what should i study",
        "study plan",
        "learning plan",
        "dsa roadmap",
    ]

    # ========================================================
    # 1. STRONG MESSAGE INTENT
    # ========================================================

    if any(keyword in message for keyword in hint_keywords):
        agent_type = "hint"

    elif any(keyword in message for keyword in code_keywords):
        agent_type = "code"

    elif any(keyword in message for keyword in interview_keywords):
        agent_type = "interview"

    elif any(keyword in message for keyword in mcq_keywords):
        agent_type = "mcq"

    elif any(keyword in message for keyword in roadmap_keywords):
        agent_type = "roadmap"

    # ========================================================
    # 2. EXPLICIT UI MODE
    # ========================================================
    else:

        if mode == "hint":
            agent_type = "hint"

        elif mode in ["review", "analyze"]:
            agent_type = "code"

        elif mode in ["interview", "interview_prep"]:
            agent_type = "interview"

        elif mode in ["mcq", "quiz"]:
            agent_type = "mcq"

        elif mode in ["roadmap", "learning_path"]:
            agent_type = "roadmap"

        else:
            # Default mode = Coach
            agent_type = "coach"

    # ========================================================
    # DEBUG LOG
    # ========================================================

    print(
        f"[ROUTER] message={message!r} "
        f"mode={mode!r} "
        f"-> agent_type={agent_type!r}"
    )

    return {
        "agent_type": agent_type,
    }


# ============================================================
# RAG RETRIEVAL NODE
# ============================================================

def retrieve_node(state: CoachState) -> CoachState:
    """
    Retrieve relevant DSA knowledge from PostgreSQL + pgvector.

    Retrieval uses:
    1. Current user message
    2. Recent conversation history
    3. Problem context, if available

    This allows follow-up questions such as:
        "What is its time complexity?"

    to be understood using the previous conversation.
    """

    message = state.get("message", "")

    problem = state.get("problem")

    conversation = state.get(
        "conversation",
        [],
    )

    # --------------------------------------------------------
    # Resolve current question using conversation
    # --------------------------------------------------------

    resolved_query = resolve_conversation_query(
        state
    )

    # --------------------------------------------------------
    # Build retrieval query
    # --------------------------------------------------------

    retrieval_query = f"""
Resolved user query:
{resolved_query}

Current user question:
{message}
""".strip()

    # --------------------------------------------------------
    # Add structured problem information
    # --------------------------------------------------------

    if problem:

        title = problem.get(
            "title",
            "",
        )

        topic = problem.get(
            "topic",
            "",
        )

        pattern = problem.get(
            "pattern",
            "",
        )

        retrieval_query += f"""

Problem context:
Title: {title}
Topic: {topic}
Pattern: {pattern}
"""

    # --------------------------------------------------------
    # Retrieval hints
    # --------------------------------------------------------

    agent_type = state.get(
        "agent_type",
        "",
    ).lower()

    if agent_type == "code":

        retrieval_query += """

    Retrieval priority:
    - Find the exact problem or algorithm being discussed.
    - Prefer problem, solution, approach, key idea, and complexity sections.
    - Programming language is secondary metadata, not the main search topic.
    """

    elif agent_type == "coach":

        retrieval_query += """

    Retrieval priority:
    - Prefer conceptual explanation, key idea, algorithm steps,
    implementation details, and complexity sections.
    - Resolve references such as "it", "its", "this algorithm",
    and "the above approach" using conversation context.
    """

    # --------------------------------------------------------
    # Build conversation context
    # --------------------------------------------------------

    conversation_context = ""

    if conversation:

        recent_conversation = conversation[-6:]

        conversation_lines = []

        for item in recent_conversation:

            role = item.get(
                "role",
                "",
            )

            content = item.get(
                "content",
                "",
            )

            if content:

                conversation_lines.append(
                    f"{role}: {content}"
                )

        conversation_context = "\n".join(
            conversation_lines
        )
    

    # --------------------------------------------------------
    # PostgreSQL + pgvector retrieval
    # --------------------------------------------------------

    documents = similarity_search(
        query=retrieval_query,
        top_k=5,
    )

    return {
        "resolved_query": resolved_query,
        "retrieved_documents": documents,
    }


# ============================================================
# COACH NODE
# ============================================================

def coach_node(state: CoachState) -> CoachState:
    """
    Execute the Coach Agent.

    The resolved conversational query is supplied to the agent
    so follow-up questions retain their context.
    """
    query = state.get(
        "resolved_query",
        "",
    )

    if not query:
        query = state.get(
            "message",
            "",
        )

    result = run_coach_agent(
        query=query,
        mode=state.get("mode", "explain"),
        language=state.get("language", "java"),
        code=state.get("code", ""),
        problem=state.get("problem"),
        conversation=state.get("conversation", []),
        retrieved_documents=state.get(
            "retrieved_documents",
            [],
        ),
    )

    raw_answer = (
        result.get("answer","")
        if isinstance(result, dict)
        else result
    )

    answer = normalize_answer(raw_answer)

    return {
        "agent_type": "coach",
        "answer": answer,
    }


# ============================================================
# CODE NODE
# ============================================================

def code_node(state: CoachState) -> CoachState:
    """
    Execute the Code Analysis Agent.

    IMPORTANT:
    This node only generates an answer.

    It does NOT update conversation memory.
    """
    query = state.get(
        "resolved_query",
        "",
    )

    if not query:
        query = state.get(
            "message",
            "",
        )

    result = run_code_agent(
        query=query,
        mode=state.get("mode", "review"),
        language=state.get("language", "java"),
        code=state.get("code", ""),
        problem=state.get("problem"),
        conversation=state.get("conversation", []),
        retrieved_documents=state.get(
            "retrieved_documents",
            [],
        ),
    )

    raw_answer = (
        result["answer"]
        if isinstance(result, dict)
        else result
    )

    answer = normalize_answer(raw_answer)

    return {
        "agent_type": "code",
        "answer": answer,
    }


# ============================================================
# HINT NODE
# ============================================================

def hint_node(state: CoachState) -> CoachState:
    """
    Execute the Hint Agent.

    IMPORTANT:
    This node only generates an answer.

    It does NOT update conversation memory.
    """

    query = state.get(
        "resolved_query",
        "",
    )

    if not query:
        query = state.get(
            "message",
            "",
        )

    result = run_hint_agent(
        query=query,
        mode="hint",
        language=state.get("language", "java"),
        code=state.get("code", ""),
        problem=state.get("problem"),
        conversation=state.get("conversation", []),
        retrieved_documents=state.get(
            "retrieved_documents",
            [],
        ),
    )

    raw_answer = (
        result["answer"]
        if isinstance(result, dict)
        else result
    )

    answer = normalize_answer(raw_answer)

    return {
        "agent_type": "hint",
        "answer": answer,
    }

# ============================================================
# INTERVIEW NODE
# ============================================================

def interview_node(state: CoachState) -> CoachState:
    """
    Execute the Interview Preparation Agent.
    """
    query = state.get(
        "resolved_query",
        "",
    )

    if not query:
        query = state.get(
            "message",
            "",
        )

    result = run_interview_agent(
        query=query,
        mode=state.get("mode", "interview"),
        language=state.get("language", "java"),
        code=state.get("code", ""),
        problem=state.get("problem"),
        conversation=state.get("conversation", []),
        retrieved_documents=state.get(
            "retrieved_documents",
            [],
        ),
    )

    raw_answer = (
        result["answer"]
        if isinstance(result, dict)
        else result
    )

    answer = normalize_answer(raw_answer)

    return {
        "agent_type": "interview",
        "answer": answer,
    }


# ============================================================
# MCQ NODE
# ============================================================

def mcq_node(state: CoachState) -> CoachState:
    """
    Execute the MCQ Agent.
    """
    query = state.get(
        "resolved_query",
        "",
    )

    if not query:
        query = state.get(
            "message",
            "",
        )

    result = run_mcq_agent(
        query=query,
        mode=state.get("mode", "mcq"),
        language=state.get("language", "java"),
        code=state.get("code", ""),
        problem=state.get("problem"),
        conversation=state.get("conversation", []),
        retrieved_documents=state.get(
            "retrieved_documents",
            [],
        ),
    )

    raw_answer = (
        result["answer"]
        if isinstance(result, dict)
        else result
    )

    answer = normalize_answer(raw_answer)

    return {
        "agent_type": "mcq",
        "answer": answer,
    }


# ============================================================
# ROADMAP NODE
# ============================================================

def roadmap_node(state: CoachState) -> CoachState:
    """
    Execute the Roadmap Agent.
    """
    query = state.get(
        "resolved_query",
        "",
    )

    if not query:
        query = state.get(
            "message",
            "",
        )

    result = run_roadmap_agent(
        query=query,
        mode=state.get("mode", "roadmap"),
        language=state.get("language", "java"),
        code=state.get("code", ""),
        problem=state.get("problem"),
        conversation=state.get("conversation", []),
        retrieved_documents=state.get(
            "retrieved_documents",
            [],
        ),
    )

    raw_answer = (
        result["answer"]
        if isinstance(result, dict)
        else result
    )

    answer = normalize_answer(raw_answer)

    return {
        "agent_type": "roadmap",
        "answer": answer,
    }

# ============================================================
# EVALUATION NODE
# ============================================================

def evaluate_node(state: CoachState) -> CoachState:
    """
    Evaluate the generated response.

    Current version:
        Deterministic development evaluator.

    Future version:
        Gemini-based evaluator.

    The graph interface remains the same:

        evaluation = "good"
        evaluation = "bad"

    This allows Gemini to be introduced later without
    changing the LangGraph routing logic.
    """

    # --------------------------------------------------------
    # Current retry count
    # --------------------------------------------------------

    retry_count = state.get(
        "retry_count",
        0,
    )

    # --------------------------------------------------------
    # Testing override
    # --------------------------------------------------------

    override = state.get(
        "evaluation_override",
        "",
    )

    if override == "good":

        return {
            "evaluation": "good",
        }

    if override == "bad":

        return {
            "evaluation": "bad",
            "retry_count": retry_count + 1,
        }

    # --------------------------------------------------------
    # Get generated answer
    # --------------------------------------------------------

    answer = normalize_answer(
        state.get("answer", "")
    )

    # --------------------------------------------------------
    # Empty response = BAD
    # --------------------------------------------------------

    if not answer:

        return {
            "evaluation": "bad",
            "retry_count": retry_count + 1,
        }

    # --------------------------------------------------------
    # Response is acceptable
    # --------------------------------------------------------

    return {
        "evaluation": "good",
    }


# ============================================================
# CONVERSATION MEMORY UPDATE
# ============================================================

def conversation_node(state: CoachState) -> CoachState:
    """
    Save the final user + assistant exchange into conversation
    memory.

    This node is executed ONLY after the response has been
    accepted or after maximum retries have been reached.

    Failed intermediate responses are NOT stored.
    """

    answer = state.get(
        "answer",
        "",
    )

    if not answer:
        return {}

    return {
        "conversation": [
            {
                "role": "assistant",
                "content": answer,
            }
        ]
    }