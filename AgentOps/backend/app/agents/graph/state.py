from typing import Any, TypedDict, Annotated
import operator

class CoachState(TypedDict, total=False):
    """
    Shared state for the DSA Coach LangGraph workflow.
    """

    # --------------------------------------------------------
    # User request
    # --------------------------------------------------------

    message: str #user's actual request
    mode: str #requested interaction mode. eg. hint, explain, analyze, review

    # --------------------------------------------------------
    # Code information
    # --------------------------------------------------------

    language: str #programming language selected by the user.
    code: str #Contains the user's submitted code.

    # --------------------------------------------------------
    # Problem information
    # --------------------------------------------------------

    problem: dict[str, Any] | None #Contains information about the DSA problem.

    # --------------------------------------------------------
    # Conversation memory
    # --------------------------------------------------------

    conversation: Annotated[ 
        list[dict[str, Any]],
        operator.add,
    ] #conversation memory at the application level.


    # ========================================================
    # USER / SESSION INFORMATION
    # ========================================================

    user_id: str #identifies the user.
    thread_id: str #identifies a particular conversation/session.

    # --------------------------------------------------------
    # Agent routing
    # --------------------------------------------------------

    agent_type: str #tells the graph which agent should handle the request.

    resolved_query: str
    
    # --------------------------------------------------------
    # RAG
    # --------------------------------------------------------

    retrieved_documents: list[Any] #stores the documents retrieved by our RAG system.

    # --------------------------------------------------------
    # Final response
    # --------------------------------------------------------

    answer: str #contains the final generated response.

    # --------------------------------------------------------
    # Self-correction
    # --------------------------------------------------------

    evaluation: str #evaluation stores: good, bad

    retry_count: int #prevents infinite loops

    max_retries: int

    # --------------------------------------------------------
    # Testing / development
    # --------------------------------------------------------

    evaluation_override: str #only for testing
