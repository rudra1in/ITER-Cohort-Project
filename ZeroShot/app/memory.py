class ConversationMemory:

    def __init__(
        self,
        database,
        limit=8
    ):

        self.database = database

        self.limit = limit

    # CREATE SESSION

    def create_session(
        self,
        session_id,
        test_id
    ):

        self.database.create_chat_session(
            session_id,
            test_id
        )
     
    # SAVE USER
    
    def save_user_message(
        self,
        session_id,
        content
    ):

        self.database.save_message(
            session_id,
            "user",
            content
        )
    
    # SAVE ASSISTANT

    def save_assistant_message(
        self,
        session_id,
        content
    ):

        self.database.save_message(
            session_id,
            "assistant",
            content
        )
     
    # GET

    def get_history(
        self,
        session_id
    ):

        return self.database.get_messages(
            session_id,
            self.limit
        )
     
    # FORMAT
     
    def format_history(
        self,
        session_id
    ):

        messages = (
            self.get_history(
                session_id
            )
        )

        if not messages:

            return "No previous conversation."

        lines = []

        for message in messages:

            role = (
                message["role"]
                .upper()
            )

            content = (
                message["content"]
            )

            lines.append(
                f"{role}: {content}"
            )

        return "\n".join(
            lines
        )