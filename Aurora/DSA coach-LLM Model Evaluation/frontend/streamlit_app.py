import streamlit as st
import requests
from datetime import datetime


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="DSA Coach",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# COLORS
# ============================================================

BG = "#F3EAFF"
SIDEBAR_BG = "#E7DEFA"

PURPLE = "#4B357C"
DARK = "#29213A"

LIGHT_PURPLE = "#B0BAE6"
LIGHTER_PURPLE = "#C8C9F0"

WHITE = "#FFFFFF"
BORDER = "#D2C5EA"


# ============================================================
# SESSION STATE
# ============================================================

if "chats" not in st.session_state:
    st.session_state.chats = {
        "chat_1": {
            "name": "New Chat",
            "messages": []
        }
    }

if "current_chat" not in st.session_state:
    st.session_state.current_chat = "chat_1"


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_current_chat():

    return st.session_state.chats[
        st.session_state.current_chat
    ]


def new_chat():

    chat_id = f"chat_{datetime.now().timestamp()}"

    st.session_state.chats[chat_id] = {
        "name": "New Chat",
        "messages": []
    }

    st.session_state.current_chat = chat_id


def delete_chat(chat_id):

    # If only one chat exists,
    # clear it instead of deleting it completely.
    if len(st.session_state.chats) == 1:

        st.session_state.chats[chat_id] = {
            "name": "New Chat",
            "messages": []
        }

        st.session_state.current_chat = chat_id

        return

    # Delete chat
    del st.session_state.chats[chat_id]

    # If deleted chat was active,
    # switch to another chat.
    if st.session_state.current_chat == chat_id:

        remaining_chats = list(
            st.session_state.chats.keys()
        )

        st.session_state.current_chat = remaining_chats[0]


def rename_chat(chat_id, new_name):

    new_name = new_name.strip()

    if new_name:

        st.session_state.chats[
            chat_id
        ]["name"] = new_name


def auto_name_chat(chat_id, question):

    chat = st.session_state.chats[chat_id]

    # Only automatically name a brand-new chat.
    if chat["name"] != "New Chat":
        return

    clean_question = question.strip()

    if len(clean_question) > 35:

        clean_question = (
            clean_question[:35] + "..."
        )

    if clean_question:

        chat["name"] = clean_question


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    f"""
    <style>

    /* ========================================================
       GLOBAL
       ======================================================== */

    .stApp {{
        background-color: {BG} !important;
    }}

    html, body, [class*="css"] {{
        color: {DARK} !important;
    }}


    /* ========================================================
       SIDEBAR
       ======================================================== */

    [data-testid="stSidebar"] {{
        background-color: {SIDEBAR_BG} !important;
        border-right: 1px solid {BORDER} !important;
    }}

    [data-testid="stSidebar"] * {{
        color: {DARK} !important;
    }}


    /* ========================================================
       NEW CHAT BUTTON
       ======================================================== */

    [data-testid="stSidebar"] .stButton > button {{
        background-color: {LIGHT_PURPLE} !important;
        color: {DARK} !important;

        border: none !important;
        border-radius: 14px !important;

        min-height: 50px !important;

        font-size: 16px !important;
        font-weight: 600 !important;
    }}

    [data-testid="stSidebar"] .stButton > button:hover {{
        background-color: {LIGHTER_PURPLE} !important;
        color: {DARK} !important;
    }}


    /* ========================================================
       CONVERSATIONS TITLE
       ======================================================== */

    .conversation-title {{
        color: {PURPLE} !important;

        font-size: 20px !important;
        font-weight: 700 !important;

        margin-top: 28px !important;
        margin-bottom: 12px !important;
    }}


    /* ========================================================
       CHAT BUTTONS
       ======================================================== */

    .chat-button button {{
        background-color: transparent !important;
        color: {DARK} !important;

        border: none !important;
        border-radius: 12px !important;

        text-align: left !important;

        min-height: 44px !important;
    }}

    .chat-button button:hover {{
        background-color: {LIGHTER_PURPLE} !important;
        color: {DARK} !important;
    }}


    /* ========================================================
       THREE DOT MENU
       ======================================================== */

    [data-testid="stPopover"] button {{
        background-color: transparent !important;
        color: {DARK} !important;

        border: none !important;
    }}

    [data-testid="stPopover"] button:hover {{
        background-color: {LIGHTER_PURPLE} !important;
    }}


    /* ========================================================
       SELECT BOX
       ======================================================== */

    [data-testid="stSidebar"] div[data-baseweb="select"] {{
        background-color: {WHITE} !important;

        border-radius: 12px !important;

        border: 1px solid {BORDER} !important;
    }}

    [data-testid="stSidebar"]
    div[data-baseweb="select"] > div:first-child {{
        background-color: {WHITE} !important;

        border-radius: 12px !important;

        color: {DARK} !important;
    }}

    [data-testid="stSidebar"]
    div[data-baseweb="select"] * {{
        color: {DARK} !important;
    }}

    [data-testid="stSidebar"]
    div[data-baseweb="select"] svg {{
        fill: {DARK} !important;
    }}


    /* ========================================================
       SELECTBOX POPUP
       ======================================================== */

    div[data-baseweb="popover"] {{
        background-color: {WHITE} !important;
    }}

    div[data-baseweb="popover"] * {{
        color: {DARK} !important;
    }}

    div[data-baseweb="popover"]
    div[data-baseweb="menu"] {{
        background-color: {WHITE} !important;
    }}

    div[data-baseweb="popover"]
    div[data-baseweb="menu"] li {{
        background-color: {WHITE} !important;
        color: {DARK} !important;
    }}

    div[data-baseweb="popover"]
    div[data-baseweb="menu"] li:hover {{
        background-color: {LIGHTER_PURPLE} !important;
        color: {DARK} !important;
    }}


    /* ========================================================
       MAIN TITLE
       ======================================================== */

    .main-title {{
        color: {PURPLE} !important;

        text-align: center;

        font-size: 48px !important;
        font-weight: 800 !important;

        margin-top: 35px;
    }}

    .main-subtitle {{
        color: {PURPLE} !important;

        text-align: center;

        font-size: 20px !important;

        margin-top: 5px;
        margin-bottom: 30px;
    }}


    /* ========================================================
       CHAT MESSAGES
       ======================================================== */

    [data-testid="stChatMessage"] {{
        color: {DARK} !important;
    }}

    [data-testid="stChatMessage"] * {{
        color: {DARK} !important;
    }}


    /* ========================================================
       CHAT INPUT
       ======================================================== */

    [data-testid="stChatInput"] {{
        background-color: {WHITE} !important;

        border: 1px solid {BORDER} !important;

        border-radius: 16px !important;
    }}

    [data-testid="stChatInput"] textarea {{
        color: {DARK} !important;

        background-color: {WHITE} !important;
    }}

    [data-testid="stChatInput"] textarea::placeholder {{
        color: #756A88 !important;
    }}


    /* ========================================================
       DIVIDERS
       ======================================================== */

    hr {{
        border-color: {BORDER} !important;
    }}


    /* ========================================================
       RENAME INPUT
       ======================================================== */

    [data-testid="stPopover"] input {{
        color: {DARK} !important;

        background-color: {WHITE} !important;
    }}

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    # --------------------------------------------------------
    # NEW CHAT
    # --------------------------------------------------------

    if st.button(
        "🌸  New Chat",
        use_container_width=True,
        key="new_chat_button"
    ):

        new_chat()

        st.rerun()


    # --------------------------------------------------------
    # CONVERSATIONS
    # --------------------------------------------------------

    st.markdown(
        '<div class="conversation-title">'
        '💬 Conversations'
        '</div>',
        unsafe_allow_html=True
    )

    #model 
    model_name = st.selectbox(
    "Choose LLM",
    ["gemini", "qwen", "llama"],
    format_func=lambda x: {
            "gemini": "Gemini",
            "qwen": "Qwen",
            "llama": "Llama"
        }[x]
    )

    chat_ids = list(
        st.session_state.chats.keys()
    )

    # Newest conversations first
    chat_ids = list(reversed(chat_ids))


    for chat_id in chat_ids:

        chat = st.session_state.chats[chat_id]


        # Two columns:
        # conversation name + three dot menu

        col1, col2 = st.columns(
            [5, 1],
            gap="small"
        )


        # ----------------------------------------------------
        # CHAT NAME
        # ----------------------------------------------------

        with col1:

            if st.button(
                f"🌸  {chat['name']}",
                key=f"open_{chat_id}",
                use_container_width=True
            ):

                st.session_state.current_chat = chat_id

                st.rerun()


        # ----------------------------------------------------
        # THREE DOT MENU
        # ----------------------------------------------------

        with col2:

            with st.popover(
                "⋯",
                use_container_width=True
            ):

                # --------------------------------------------
                # RENAME
                # --------------------------------------------

                st.markdown(
                    "**✏️ Rename chat**"
                )

                new_name = st.text_input(
                    "Chat name",
                    value=chat["name"],
                    key=f"rename_input_{chat_id}",
                    label_visibility="collapsed"
                )

                if st.button(
                    "Save name",
                    key=f"save_name_{chat_id}",
                    use_container_width=True
                ):

                    rename_chat(
                        chat_id,
                        new_name
                    )

                    st.rerun()


                # --------------------------------------------
                # DELETE
                # --------------------------------------------

                if st.button(
                    "🗑️ Delete",
                    key=f"delete_{chat_id}",
                    use_container_width=True
                ):

                    delete_chat(chat_id)

                    st.rerun()


    # --------------------------------------------------------
    # SEARCH SETTINGS
    # --------------------------------------------------------

    st.markdown(
        "<br>",
        unsafe_allow_html=True
    )

    st.markdown(
        "**🔎 Search method**"
    )

    mode = st.selectbox(
        "Search method",
        ["hybrid", "semantic"],
        index=0,
        label_visibility="collapsed"
    )


    # --------------------------------------------------------
    # RETRIEVED CHUNKS
    # --------------------------------------------------------

    st.markdown(
        "**📚 Retrieved chunks**"
    )

    top_k = st.selectbox(
        "Retrieved chunks",
        [3, 4, 5],
        index=0,
        label_visibility="collapsed"
    )


    # --------------------------------------------------------
    # CLEAR CURRENT CONVERSATION
    # --------------------------------------------------------

    st.markdown(
        "<br><br>",
        unsafe_allow_html=True
    )

    current_chat = get_current_chat()


    if st.button(
        "🗑️  Clear Conversation",
        use_container_width=True,
        key="clear_conversation"
    ):

        current_chat["messages"] = []

        current_chat["name"] = "New Chat"

        st.rerun()


# ============================================================
# MAIN AREA
# ============================================================

current_chat = get_current_chat()


# ------------------------------------------------------------
# TITLE
# ------------------------------------------------------------

st.markdown(
    '<div class="main-title">DSA Coach 🌸</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="main-subtitle">'
    'Your friendly AI companion for Data Structures & Algorithms ✨'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# DISPLAY CURRENT CHAT
# ============================================================

for message in current_chat["messages"]:

    role = message["role"]
    content = message["content"]


    if role == "user":

        with st.chat_message(
            "user",
            avatar="🌸"
        ):

            st.markdown(content)


    else:

        with st.chat_message(
            "assistant",
            avatar="🤖"
        ):

            st.markdown(content)


# ============================================================
# CHAT INPUT
# ============================================================

question = st.chat_input(
    "Ask me anything about DSA..."
)


if question:

    question = question.strip()


    if not question:

        st.warning(
            "Please enter a question 💜"
        )

        st.stop()


    # ========================================================
    # SAVE USER MESSAGE
    # ========================================================

    current_chat["messages"].append(
        {
            "role": "user",
            "content": question
        }
    )


    # ========================================================
    # AUTOMATIC CHAT NAME
    # ========================================================

    auto_name_chat(
        st.session_state.current_chat,
        question
    )


    # ========================================================
    # SHOW USER MESSAGE
    # ========================================================

    with st.chat_message(
        "user",
        avatar="🌸"
    ):

        st.markdown(question)


    # ========================================================
    # PREVIOUS HISTORY
    # ========================================================

    previous_history = (
        current_chat["messages"][:-1]
    )


    # ========================================================
    # CALL FASTAPI
    # ========================================================

    with st.chat_message(
        "assistant",
        avatar="🤖"
    ):

        with st.spinner(
            "Evaluating Qwen, Gemini & Llama... ✨"
        ):

            try:

                response = requests.post(
                    "http://127.0.0.1:8000/ask",

                    json={
                        "question": question,
                        "mode": mode,
                        "top_k": top_k,
                        "history": previous_history
                    },

                    timeout=120
                )


                # ====================================================
                # SUCCESS
                # ====================================================

                if response.status_code == 200:

                    data = response.json()

                    evaluation = data.get(
                        "evaluation",
                        []
                    )


                    # =================================================
                    # CHECK EVALUATION
                    # =================================================

                    if not evaluation:

                        st.warning(
                            "No evaluation results received."
                        )

                    else:

                        # =============================================
                        # EVALUATION TABLE
                        # =============================================

                        st.markdown(
                            "### 📊 Model Evaluation"
                        )


                        table_data = []


                        for result in evaluation:

                            model = result.get(
                                "model",
                                "Unknown"
                            )

                            latency = result.get(
                                "latency",
                                0
                            )

                            answer = result.get(
                                "answer",
                                "No answer generated."
                            )


                            table_data.append(
                                {
                                    "Model": model.upper(),
                                    "Latency": (
                                        f"{latency:.2f}s"
                                    ),
                                    "Answer": answer
                                }
                            )


                        # Display table
                        st.table(
                            table_data
                        )


                        # =============================================
                        # DETAILED MODEL RESPONSES
                        # =============================================

                        st.markdown(
                            "### 🤖 Model Responses"
                        )


                        for result in evaluation:

                            model = result.get(
                                "model",
                                "Unknown"
                            )

                            latency = result.get(
                                "latency",
                                0
                            )

                            answer = result.get(
                                "answer",
                                "No answer generated."
                            )


                            with st.expander(
                                f"{model.upper()}  •  "
                                f"{latency:.2f}s"
                            ):

                                st.markdown(
                                    answer
                                )


                        # =============================================
                        # EVALUATION SUMMARY
                        # =============================================

                        st.markdown(
                            "### 📈 Evaluation Summary"
                        )


                        # Find fastest model

                        fastest = min(
                            evaluation,
                            key=lambda x: x.get(
                                "latency",
                                float("inf")
                            )
                        )


                        # Calculate average latency

                        latencies = [
                            result.get(
                                "latency",
                                0
                            )
                            for result in evaluation
                        ]


                        average_latency = (
                            sum(latencies)
                            / len(latencies)
                            if latencies
                            else 0
                        )


                        col1, col2 = st.columns(2)


                        with col1:

                            st.metric(
                                "⚡ Fastest Model",
                                fastest.get(
                                    "model",
                                    "Unknown"
                                ).upper()
                            )


                        with col2:

                            st.metric(
                                "⏱️ Average Latency",
                                f"{average_latency:.2f}s"
                            )


                        # =============================================
                        # SAVE RESULT TO CHAT HISTORY
                        # =============================================

                        summary = (
                            "### 📊 Model Evaluation\n\n"
                        )


                        for result in evaluation:

                            summary += (
                                f"**"
                                f"{result.get('model', 'Unknown').upper()}"
                                f"** — "
                                f"{result.get('latency', 0):.2f}s\n\n"
                                f"{result.get('answer', '')}\n\n"
                            )


                        current_chat["messages"].append(
                            {
                                "role": "assistant",
                                "content": summary
                            }
                        )


                # ====================================================
                # BACKEND ERROR
                # ====================================================

                else:

                    st.error(
                        "Something went wrong:\n\n"
                        f"{response.text}"
                    )


            # ========================================================
            # CONNECTION ERROR
            # ========================================================

            except requests.exceptions.ConnectionError:

                st.error(
                    "💜 I can't connect to the DSA Coach backend. "
                    "Please make sure FastAPI is running."
                )


            # ========================================================
            # TIMEOUT
            # ========================================================

            except requests.exceptions.Timeout:

                st.error(
                    "⏳ The request took too long. "
                    "Please try again."
                )


            # ========================================================
            # OTHER ERROR
            # ========================================================

            except Exception as e:

                st.error(
                    f"Unexpected error: {str(e)}"
                )