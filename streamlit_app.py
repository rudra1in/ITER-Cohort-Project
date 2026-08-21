import json
import os
from pathlib import Path

import streamlit as st


st.set_page_config(
    page_title="CodeCurry — AI DSA Coach",
    page_icon="🥕",
    layout="wide",
    initial_sidebar_state="expanded",
)

BASE_DIR = Path(__file__).resolve().parent
QUESTION_FILE = BASE_DIR / "data" / "txt" / "dsa_questions.json"
PROGRESS_FILE = BASE_DIR / "progress.json"
UPLOAD_DIR = BASE_DIR / "data" / "uploads"


# ============================================================
# STYLE
# ============================================================

st.markdown(
    """
<style>
[data-testid="stAppViewContainer"] {
    background:
        radial-gradient(circle at 10% 0%, rgba(255,166,0,.10), transparent 28%),
        radial-gradient(circle at 90% 10%, rgba(113,89,255,.10), transparent 30%),
        #080a10;
}

[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 1550px;
    padding-top: 2.5rem;
    padding-left: 3rem;
    padding-right: 3rem;
}

.hero {
    padding: 48px;
    border: 1px solid rgba(255,255,255,.08);
    border-radius: 28px;
    background: linear-gradient(
        135deg,
        rgba(255,166,0,.10),
        rgba(91,77,255,.10)
    );
    margin-bottom: 24px;
}

.hero-title {
    font-size: 56px;
    line-height: 1.0;
    font-weight: 800;
    letter-spacing: -2px;
}

.gradient {
    background: linear-gradient(90deg,#ffb84d,#ff6b6b,#8c7cff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.small-muted {
    color: #9da3b4;
}

.card {
    padding: 24px;
    border-radius: 22px;
    border: 1px solid rgba(255,255,255,.08);
    background: rgba(255,255,255,.035);
}

.badge {
    display: inline-block;
    padding: 7px 12px;
    border-radius: 999px;
    background: rgba(255,166,0,.12);
    color: #ffc766;
    font-size: 13px;
    font-weight: 700;
}

.big-score {
    font-size: 62px;
    font-weight: 800;
    line-height: 1;
}

div.stButton > button {
    border-radius: 14px;
    font-weight: 700;
    min-height: 54px;
    font-size: 17px;
    padding: 10px 20px;
}

div[data-testid="stMetric"] {
    background: rgba(255,255,255,.035);
    padding: 24px;
    min-height: 135px;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,.06);
}

div[data-testid="stMetricLabel"] {
    font-size: 17px !important;
}

div[data-testid="stMetricValue"] {
    font-size: 32px !important;
}

section[data-testid="stSidebar"] {
    background: #0d1017;
    min-width: 320px !important;
    width: 320px !important;
}

section[data-testid="stSidebar"] > div {
    width: 320px !important;
    padding: 2rem 1.5rem;
}

section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] span {
    font-size: 17px !important;
}

section[data-testid="stSidebar"] button {
    min-height: 58px !important;
    font-size: 17px !important;
    border-radius: 12px !important;
}

h1 {
    font-size: 40px !important;
}

h2 {
    font-size: 32px !important;
}

h3 {
    font-size: 26px !important;
}

p {
    font-size: 17px;
}

input, textarea {
    font-size: 17px !important;
}

div[data-baseweb="select"] {
    font-size: 17px !important;
}

.streamlit-expanderHeader {
    font-size: 18px !important;
    padding: 15px !important;
}

@media (max-width: 900px) {
    .block-container {
        padding-left: 1.5rem;
        padding-right: 1.5rem;
    }

    h1 {
        font-size: 34px !important;
    }

    h2 {
        font-size: 28px !important;
    }
}
</style>
""",
    unsafe_allow_html=True,
)


# ============================================================
# BACKEND IMPORT
# ============================================================

try:
    from agents.graph import agent

    BACKEND_AVAILABLE = True
    BACKEND_ERROR = ""
except Exception as exc:
    BACKEND_AVAILABLE = False
    BACKEND_ERROR = str(exc)


# ============================================================
# DATA
# ============================================================

@st.cache_data
def load_questions():
    try:
        with open(QUESTION_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []


PROBLEMS = load_questions()


def read_progress():
    if not PROGRESS_FILE.exists():
        return {
            "score_history": [],
            "avg_score": 0,
            "solved_ids": [],
            "submissions": 0,
        }

    try:
        with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        scores = []
        for value in data.get("score_history", []):
            try:
                scores.append(max(0, min(10, int(float(value)))))
            except Exception:
                pass

        solved = data.get("solved_ids", [])
        if not isinstance(solved, list):
            solved = []

        return {
            "score_history": scores,
            "avg_score": (
                sum(scores) / len(scores) if scores else 0
            ),
            "solved_ids": solved,
            "submissions": len(scores),
        }
    except Exception:
        return {
            "score_history": [],
            "avg_score": 0,
            "solved_ids": [],
            "submissions": 0,
        }


# ============================================================
# SESSION
# ============================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "selected_problem" not in st.session_state:
    st.session_state.selected_problem = None

if "last_result" not in st.session_state:
    st.session_state.last_result = None

if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = []


# ============================================================
# LOGIN
# ============================================================

def login_page():
    st.markdown(
        """
        <div class="hero">
            <div class="badge">⚡ AI-POWERED DSA</div>
            <div class="hero-title">
                Hey there 👋<br>
                ready to <span class="gradient">cook</span> some code?
            </div>
            <p class="small-muted">
                Practice smarter. Understand your mistakes.
                Become interview-ready one problem at a time.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    left, center, right = st.columns([1, 1.5, 1])

    with center:
        login, signup = st.tabs(
            ["🔐 Login", "✨ Create account"]
        )

        with login:
            email = st.text_input(
                "Email",
                placeholder="you@example.com",
            )
            password = st.text_input(
                "Password",
                type="password",
            )

            if st.button(
                "Enter CodeCurry 🚀",
                type="primary",
                use_container_width=True,
            ):
                if email and password:
                    st.session_state.logged_in = True
                    st.session_state.username = email.split("@")[0]
                    st.rerun()
                else:
                    st.warning("Please enter your email and password.")

        with signup:
            name = st.text_input("Your name")
            email = st.text_input(
                "Email",
                key="signup_email",
            )
            password = st.text_input(
                "Password",
                type="password",
                key="signup_password",
            )

            if st.button(
                "Start my DSA journey ✨",
                type="primary",
                use_container_width=True,
            ):
                if name and email and password:
                    st.session_state.logged_in = True
                    st.session_state.username = name
                    st.rerun()
                else:
                    st.warning("Fill all fields to continue.")


# ============================================================
# SIDEBAR
# ============================================================

def sidebar():
    progress = read_progress()

    with st.sidebar:
        st.markdown("## 🥕 CodeCurry")
        st.caption(
            f"Coach mode • {st.session_state.username}"
        )

        st.divider()

        items = [
            ("🏠 Home", "Home"),
            ("🧠 DSA Arena", "Problems"),
            ("💬 AI Coach", "Coach"),
            ("📈 My Progress", "Progress"),
        ]

        for label, page in items:
            if st.button(
                label,
                use_container_width=True,
                type=(
                    "primary"
                    if st.session_state.page == page
                    else "secondary"
                ),
            ):
                st.session_state.page = page
                st.rerun()

        st.divider()

        st.metric(
            "🔥 Current average",
            f"{progress['avg_score']:.1f}/10",
        )

        if st.button(
            "🚪 Logout",
            use_container_width=True,
        ):
            st.session_state.logged_in = False
            st.rerun()


# ============================================================
# HOME
# ============================================================

def home_page():
    progress = read_progress()

    solved = len(progress["solved_ids"])
    total = len(PROBLEMS)
    avg = progress["avg_score"]
    submissions = progress["submissions"]

    st.markdown(
        f"""
        <div class="hero">
            <div class="badge">🥕 CODECURRY COACH</div>
            <div class="hero-title">
                Hey {st.session_state.username} 👋<br>
                let's <span class="gradient">level up</span> your DSA.
            </div>
            <p class="small-muted">
                Not another coding platform.
                A coach that explains how you think, not just whether you passed.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    a, b, c, d = st.columns(4)

    a.metric("🔥 Solved", f"{solved}/{total}")
    b.metric("⭐ Average", f"{avg:.1f}/10")
    c.metric("🎯 Submissions", submissions)

    level = (
        "🌱 Rookie"
        if avg < 4
        else "🔥 Builder"
        if avg < 7
        else "🏆 DSA Pro"
    )
    d.metric("Level", level)

    st.divider()

    st.subheader("🎮 Today's challenge")

    if PROBLEMS:
        solved_ids = set(progress["solved_ids"])

        challenge = next(
            (
                p
                for p in PROBLEMS
                if p.get("id") not in solved_ids
            ),
            PROBLEMS[0],
        )

        with st.container(border=True):
            x, y = st.columns([5, 1])

            with x:
                st.markdown(
                    f"### {challenge['problem']}"
                )
                st.caption(
                    f"{challenge['difficulty']} • {challenge['topic']}"
                )
                st.write(challenge["description"])

            with y:
                if st.button(
                    "Start →",
                    type="primary",
                    use_container_width=True,
                ):
                    st.session_state.selected_problem = challenge
                    st.session_state.last_result = None
                    st.session_state.page = "Problem"
                    st.rerun()

    st.divider()

    st.subheader("🗺️ Your DSA roadmap")

    roadmap = [
        ("01", "Arrays & Hashing", "Two Sum → Group Anagrams"),
        ("02", "Two Pointers", "Palindrome → Container"),
        ("03", "Stacks & Queues", "Parentheses → Monotonic Stack"),
        ("04", "Trees & Graphs", "Islands → Course Schedule"),
        ("05", "Dynamic Programming", "Coin Change → LIS"),
    ]

    cols = st.columns(5)

    for col, (number, title, description) in zip(
        cols,
        roadmap,
    ):
        with col:
            st.markdown(
                f"""
                <div class="card">
                    <div class="badge">{number}</div>
                    <h4>{title}</h4>
                    <p class="small-muted">{description}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.divider()

    st.subheader("📚 Bring your own material")

    uploaded = st.file_uploader(
        "Upload your DSA notes, PDF or DOCX",
        type=["pdf", "txt", "docx"],
    )

    if uploaded:
        UPLOAD_DIR.mkdir(
            parents=True,
            exist_ok=True,
        )

        destination = UPLOAD_DIR / uploaded.name

        with open(destination, "wb") as f:
            f.write(uploaded.getbuffer())

        st.success(
            f"📚 {uploaded.name} added to your study workspace."
        )


# ============================================================
# PROBLEMS
# ============================================================

def problems_page():
    st.title("🧠 DSA Arena")
    st.caption(
        "20 curated problems. Build confidence one pattern at a time."
    )

    difficulty = st.selectbox(
        "Difficulty",
        ["All", "Simple", "Medium"],
    )

    filtered = [
        p
        for p in PROBLEMS
        if difficulty == "All"
        or p["difficulty"] == difficulty
    ]

    progress = read_progress()
    solved_ids = set(progress["solved_ids"])

    for p in filtered:
        solved = p["id"] in solved_ids

        with st.container(border=True):
            left, mid, right = st.columns([6, 2, 1])

            with left:
                st.markdown(
                    f"""
                    ### {'✅' if solved else '○'} {p['problem']}
                    """
                )
                st.caption(p["topic"])

            with mid:
                st.write(p["difficulty"])

            with right:
                if st.button(
                    "Solve",
                    key=f"solve_{p['id']}",
                    type="primary",
                ):
                    st.session_state.selected_problem = p
                    st.session_state.last_result = None
                    st.session_state.page = "Problem"
                    st.rerun()


# ============================================================
# PROBLEM WORKSPACE
# ============================================================

def problem_page():
    p = st.session_state.selected_problem

    if not p:
        st.session_state.page = "Problems"
        st.rerun()

    if st.button("← Back to Arena"):
        st.session_state.page = "Problems"
        st.rerun()

    st.markdown(
        f"""
        <div class="hero">
            <div class="badge">
                {p['difficulty']} • {p['topic']}
            </div>
            <div class="hero-title" style="font-size:42px">
                {p['problem']}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    tab1, tab2, tab3 = st.tabs(
        ["📖 Problem", "🧪 Examples", "💡 Concepts"]
    )

    with tab1:
        st.write(p["description"])

    with tab2:
        for example in p.get("examples", []):
            st.code(example)

    with tab3:
        for concept in p.get(
            "expected_concepts",
            [],
        ):
            st.write(f"• {concept}")

    st.divider()

    st.subheader("🧩 01 — Explain your thinking")

    approach = st.text_area(
        "Approach",
        height=140,
        placeholder=(
            "Before coding, tell your coach:\n"
            "• What data structure will you use?\n"
            "• What is your algorithm?\n"
            "• What are the time and space complexities?"
        ),
    )

    st.subheader("💻 02 — Cook the solution")

    language = st.selectbox(
        "Language",
        ["Java", "Python", "C++", "C"],
    )

    code = st.text_area(
        "Code",
        height=430,
        placeholder=(
            f"// Write your {language} solution here..."
            if language != "Python"
            else "# Write your Python solution here..."
        ),
    )

    if st.button(
        "🚀 Submit to CodeCurry",
        type="primary",
        use_container_width=True,
    ):
        if not approach.strip():
            st.warning(
                "🧩 Tell me your approach first."
            )
            return

        if not code.strip():
            st.warning(
                "💻 Write some code first."
            )
            return

        if not BACKEND_AVAILABLE:
            st.error(
                "The backend could not be imported."
            )
            st.code(BACKEND_ERROR)
            return

        initial_state = {
            "problem": p["description"],
            "approach": approach,
            "code": code,
            "language": language,
            "retrieved_knowledge": [],
            "score_history": [],
            "score": 0,
            "avg_score": 0,
            "done": False,
        }

        with st.spinner(
            "🧠 Your AI coach is thinking..."
        ):
            try:
                result = agent.invoke(
                    initial_state
                )

                st.session_state.last_result = result

                progress = read_progress()

                solved_ids = set(
                    progress["solved_ids"]
                )
                solved_ids.add(p["id"])

                from agents.memory import save_progress

                save_progress(
                    result.get(
                        "score_history",
                        [],
                    ),
                    result.get(
                        "avg_score",
                        0,
                    ),
                    list(solved_ids),
                )

                st.balloons()

                st.success(
                    "🎉 Evaluation complete!"
                )

            except Exception as exc:
                st.error(
                    "Evaluation failed."
                )
                st.exception(exc)

    result = st.session_state.last_result

    if not result:
        return

    st.divider()

    score = max(
        0,
        min(
            10,
            int(
                result.get(
                    "score",
                    0,
                )
            ),
        ),
    )

    st.markdown(
        f"""
        <div class="card">
            <div class="small-muted">
                YOUR CODECURRY SCORE
            </div>
            <div class="big-score">
                {score}<span style="font-size:24px">/10</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.progress(score / 10)

    st.subheader("📊 Skill breakdown")

    scorecard = result.get(
        "scorecard",
        {},
    )

    c1, c2, c3, c4 = st.columns(4)

    cards = [
        (
            c1,
            "Correctness",
            scorecard.get("Correctness", 0),
            4,
        ),
        (
            c2,
            "Efficiency",
            scorecard.get("Efficiency", 0),
            3,
        ),
        (
            c3,
            "Readability",
            scorecard.get("Readability", 0),
            2,
        ),
        (
            c4,
            "Approach",
            scorecard.get("Approach", 0),
            1,
        ),
    ]

    for col, name, value, maximum in cards:
        with col:
            st.metric(
                name,
                f"{value}/{maximum}",
            )
            st.progress(
                value / maximum
                if maximum
                else 0
            )

    st.divider()

    st.subheader("🧑‍🏫 Your personal review")

    review_tabs = st.tabs(
        [
            "🎉 Summary",
            "🔍 Analysis",
            "⚡ Complexity",
            "✅ Evaluation",
            "💡 Hint",
            "🚀 Improve",
        ]
    )

    review_values = [
        result.get("intro", ""),
        result.get("analysis", ""),
        result.get("complexity", ""),
        result.get("evaluation", ""),
        result.get("hint", ""),
        result.get("feedback", ""),
    ]

    for tab, value in zip(
        review_tabs,
        review_values,
    ):
        with tab:
            st.write(value)

    st.success(
        result.get(
            "encouragement",
            "🚀 Keep going!",
        )
    )

    if st.button(
        "🔥 Try again",
        use_container_width=True,
    ):
        st.session_state.last_result = None
        st.rerun()


# ============================================================
# AI COACH
# ============================================================

def coach_page():
    st.title("💬 AI Coach")
    st.caption(
        "Don't copy solutions. Learn how to think."
    )

    problem_names = [
        "General DSA"
    ] + [
        p["problem"]
        for p in PROBLEMS
    ]

    selected = st.selectbox(
        "Problem context",
        problem_names,
    )

    question = st.text_area(
        "Ask your coach",
        height=130,
        placeholder=(
            "Why does two pointer work here?\n"
            "Give me a hint but not the answer..."
        ),
    )

    if st.button(
        "Ask Coach 🧠",
        type="primary",
    ):
        if not question.strip():
            st.warning(
                "Ask something first."
            )
            return

        try:
            from ollama import chat

            context = ""

            if selected != "General DSA":
                p = next(
                    x
                    for x in PROBLEMS
                    if x["problem"] == selected
                )
                context = p["description"]

            prompt = f"""
You are CodeCurry, a friendly DSA coach.

Problem:
{context}

Student question:
{question}

Give a beginner-friendly explanation.
Prefer hints, intuition and reasoning.
Do not dump a complete solution unless explicitly requested.
"""

            with st.spinner(
                "Coach is thinking..."
            ):
                response = chat(
                    model=os.getenv(
                        "OLLAMA_MODEL",
                        "llama3.2",
                    ),
                    messages=[
                        {
                            "role": "user",
                            "content": prompt,
                        }
                    ],
                )

            answer = response[
                "message"
            ]["content"]

            st.session_state.chat_messages.append(
                {
                    "q": question,
                    "a": answer,
                }
            )

        except Exception as exc:
            st.error(
                "Ollama is not available."
            )
            st.info(
                "Make sure Ollama is installed, "
                "running and the selected model is pulled."
            )
            st.exception(exc)

    for message in reversed(
        st.session_state.chat_messages
    ):
        with st.chat_message("user"):
            st.write(message["q"])

        with st.chat_message("assistant"):
            st.write(message["a"])


# ============================================================
# PROGRESS
# ============================================================

def progress_page():
    st.title("📈 My Progress")
    st.caption(
        "Your improvement matters more than one bad submission."
    )

    progress = read_progress()

    scores = progress["score_history"]
    avg = progress["avg_score"]

    a, b, c = st.columns(3)

    a.metric(
        "Problems solved",
        len(progress["solved_ids"]),
    )

    b.metric(
        "Average score",
        f"{avg:.1f}/10",
    )

    c.metric(
        "Submissions",
        progress["submissions"],
    )

    st.divider()

    if scores:
        st.subheader("📊 Your score journey")

        st.line_chart(
            {
                "CodeCurry Score": scores
            }
        )

        best = max(scores)
        latest = scores[-1]

        x, y = st.columns(2)

        x.metric(
            "🔥 Best score",
            f"{best}/10",
        )

        y.metric(
            "🎯 Latest score",
            f"{latest}/10",
        )
    else:
        st.info(
            "Solve your first problem to unlock your progress graph."
        )

    st.divider()

    st.subheader("🏆 Your current level")

    if avg < 4:
        st.info(
            "🌱 Rookie — focus on correctness and patterns."
        )
    elif avg < 7:
        st.warning(
            "🔥 Builder — now optimize your solutions."
        )
    else:
        st.success(
            "🏆 DSA Pro — you're becoming interview-ready!"
        )


# ============================================================
# APP
# ============================================================

if not st.session_state.logged_in:
    login_page()
else:
    sidebar()

    if st.session_state.page == "Home":
        home_page()

    elif st.session_state.page == "Problems":
        problems_page()

    elif st.session_state.page == "Problem":
        problem_page()

    elif st.session_state.page == "Coach":
        coach_page()

    elif st.session_state.page == "Progress":
        progress_page()