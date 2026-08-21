import streamlit as st
import datetime
import time
from frontend.config import API_BASE_URL
from frontend.api_client import DSAClient
from frontend.styles import inject_custom_styles
from frontend.components.sidebar import render_sidebar
from frontend.components.header import render_header
from frontend.components.problem_view import render_problem_view
from frontend.components.editor import render_code_editor
from frontend.components.bottom_panel import render_bottom_panel

# Set page config
st.set_page_config(
    page_title="CodeMentor - Premium AI DSA Coach",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inject custom stylesheet & keyboard hook scripts
inject_custom_styles()

# Initialize Client
client = DSAClient()

# Initialize Session State
if "history" not in st.session_state:
    st.session_state.history = []
if "execution_result" not in st.session_state:
    st.session_state.execution_result = {}
if "coach_result" not in st.session_state:
    st.session_state.coach_result = {}
if "ast_status" not in st.session_state:
    st.session_state.ast_status = {}
if "hint_level" not in st.session_state:
    st.session_state.hint_level = 1
if "trigger_run" not in st.session_state:
    st.session_state.trigger_run = False
if "trigger_submit" not in st.session_state:
    st.session_state.trigger_submit = False
if "is_running" not in st.session_state:
    st.session_state.is_running = False

# Cached Backend Health Check (30 seconds TTL to keep UI responsive)
@st.cache_data(ttl=30)
def check_backend_health_cached():
    return client.check_health()

# Cached Problem List Retrieval (10 mins TTL)
@st.cache_data(ttl=600)
def get_problems_cached():
    return client.get_problems()

is_healthy = check_backend_health_cached()
if not is_healthy:
    st.markdown(f"""
    <div style="background-color: rgba(239, 68, 68, 0.05); border: 1px solid rgba(239, 68, 68, 0.2); border-radius: 6px; padding: 0.75rem 1rem; margin-bottom: 1rem;">
        <span style="color: var(--danger); font-weight: 700;">⚠️ API Connectivity Warning:</span> 
        <span style="color: var(--text-muted); font-size: 0.9rem;">FastAPI Backend is unreachable at <code>{API_BASE_URL}</code>. 
        Please start the backend server via command line. Falling back to local static problem set for preview mode.</span>
    </div>
    """, unsafe_allow_html=True)

# Fetch problems
problems_resp = get_problems_cached()
if "error" in problems_resp or not problems_resp.get("problems"):
    # Fallback problem set
    problems = [
        {
            "id": "two-sum",
            "title": "Two Sum",
            "description": "Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.",
            "topic": "Arrays",
            "difficulty": "Easy",
            "pattern": "Hash Map",
            "constraints": "Each input has exactly one solution. You may not use the same element twice.",
            "examples": [
                {
                    "input": "nums = [2,7,11,15], target = 9",
                    "output": "[0,1]",
                    "explanation": "Because nums[0] + nums[1] == 9, we return [0, 1]."
                }
            ],
            "test_cases": [
                {"input": [[2, 7, 11, 15], 9], "expected_output": [0, 1]},
                {"input": [[3, 2, 4], 6], "expected_output": [1, 2]}
            ],
            "complexity": "Time Complexity: O(N)\nSpace Complexity: O(N)"
        },
        {
            "id": "reverse-array",
            "title": "Reverse Array",
            "description": "Given an array `arr`, return the array with its elements reversed.",
            "topic": "Arrays",
            "difficulty": "Easy",
            "pattern": "Two Pointers",
            "constraints": "Array size is between 1 and 10^5.",
            "examples": [
                {
                    "input": "arr = [1,2,3,4]",
                    "output": "[4,3,2,1]"
                }
            ],
            "test_cases": [
                {"input": [[1, 2, 3, 4]], "expected_output": [4, 3, 2, 1]}
            ],
            "complexity": "Time Complexity: O(N)\nSpace Complexity: O(1)"
        }
    ]
else:
    problems = problems_resp.get("problems", [])

# Render sidebar & get active problem
with st.sidebar:
    active_problem = render_sidebar(problems)

# If no problem is selected (e.g. empty lists), stop
if not active_problem:
    st.info("No problems available.")
    st.stop()

# Helper Callbacks
prob_id = active_problem.get("id")
code_key = f"code_{prob_id}"

def run_ai_loading_sequence():
    """Renders sequential animated loading messages to explain RAG + execution steps."""
    placeholder = st.empty()
    steps = [
        "🔍 Analyzing your code...",
        "📖 Retrieving relevant DSA knowledge from RAG...",
        "⚡ Checking the execution context & test cases...",
        "🤖 Preparing your hint..."
    ]
    for step in steps:
        placeholder.markdown(f"""
        <div style="background-color: var(--bg-overlay); border: 1px solid var(--border); border-left: 3px solid var(--accent); border-radius: 4px; padding: 0.75rem 1rem; font-family: var(--font-mono); font-size: 0.85rem; color: var(--accent); margin-bottom: 0.5rem; display:flex; align-items:center; gap:0.5rem;">
            <div class="shimmer" style="width:10px; height:10px; background-color:var(--accent); border-radius:50%;"></div>
            <span>{step}</span>
        </div>
        """, unsafe_allow_html=True)
        time.sleep(0.3)
    placeholder.empty()

def trigger_coach_feedback():
    """Trigger payload submission to uvicorn API coach."""
    st.session_state.is_running = True
    student_code = st.session_state.get(code_key, "")
    
    # Run interactive loaded process steps
    run_ai_loading_sequence()
    
    # Fetch RAG AI Coach advice
    coach_resp = client.get_coach_feedback(
        problem_id=prob_id,
        code=student_code,
        hint_level=st.session_state.hint_level
    )
    st.session_state.coach_result = coach_resp
    st.session_state.is_running = False
    
    # Toast notification
    st.toast("AI Coach mentoring analysis complete.", icon="💡")
    st.rerun()

def handle_hint_level_change(new_level: int):
    st.session_state.hint_level = new_level
    student_code = st.session_state.get(code_key, "")
    
    run_ai_loading_sequence()
    
    coach_resp = client.get_coach_feedback(
        problem_id=prob_id,
        code=student_code,
        hint_level=new_level
    )
    st.session_state.coach_result = coach_resp
    st.rerun()

def apply_code_suggestion(new_code: str):
    """Apply correction suggestion from AI into the code editor."""
    st.session_state[code_key] = new_code
    st.toast("Applied AI suggestion to code workspace.", icon="✨")
    st.rerun()

# -------------------------------------------------------------
# MAIN APP WORKSPACE
# -------------------------------------------------------------

# Render Problem Header
render_header(active_problem)

# If in running state, show subtle progress banner top of workspace
if st.session_state.is_running:
    st.markdown('<div style="background-color:rgba(59,130,246,0.06); border: 1px solid var(--border); padding:0.5rem; border-radius:4px; font-family:var(--font-mono); font-size:0.8rem; text-align:center; color:var(--accent);">⚡ Processing solution...</div>', unsafe_allow_html=True)

# Split Workspace into 2 main columns for Desktop
col_left, col_right = st.columns([5, 6])

with col_left:
    st.markdown('<div class="dev-panel" style="min-height:560px;">', unsafe_allow_html=True)
    st.markdown('<div class="dev-panel-header">📖 Problem Description</div>', unsafe_allow_html=True)
    render_problem_view(active_problem)
    st.markdown('</div>', unsafe_allow_html=True)

with col_right:
    st.markdown('<div class="dev-panel" style="min-height:560px;">', unsafe_allow_html=True)
    # Editor handles state internally, returns code & AST status
    code, is_syntax_valid, ast_details = render_code_editor(active_problem)
    st.session_state.ast_status = ast_details
    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------------------------------------
# TRIGGER LOGIC FOR BUTTON ACTIONS
# -------------------------------------------------------------
if st.session_state.trigger_run:
    st.session_state.trigger_run = False
    
    if not is_syntax_valid:
        st.toast("Syntax error detected. Fix AST check before running.", icon="⚠️")
    else:
        st.session_state.is_running = True
        with st.spinner("Executing solution on test cases..."):
            exec_resp = client.execute_code(
                code=code,
                test_cases=active_problem.get("test_cases", [])
            )
            st.session_state.execution_result = exec_resp
            
            # Log attempt to session history
            timestamp = datetime.datetime.now().strftime("%H:%M:%S")
            st.session_state.history.append({
                "problem_id": prob_id,
                "timestamp": timestamp,
                "status": exec_resp.get("status", "unknown"),
                "runtime_ms": exec_resp.get("runtime_ms", 0) or 0,
                "hint_level": st.session_state.hint_level
            })
            
            # Save solved status in session
            if exec_resp.get("status") == "accepted":
                st.session_state[f"solved_{prob_id}"] = True
                st.toast("Correct Solution! All tests passed.", icon="🎉")
            else:
                st.toast("Test execution finished. Cases failed.", icon="❌")
                
        st.session_state.is_running = False
        st.rerun()

if st.session_state.trigger_submit:
    st.session_state.trigger_submit = False
    
    st.session_state.is_running = True
    with st.spinner("Submitting solution & retrieving AI analysis..."):
        # Execute tests
        exec_resp = client.execute_code(
            code=code,
            test_cases=active_problem.get("test_cases", [])
        )
        st.session_state.execution_result = exec_resp
        
        # Get AI Coach feedback
        coach_resp = client.get_coach_feedback(
            problem_id=prob_id,
            code=code,
            hint_level=st.session_state.hint_level
        )
        st.session_state.coach_result = coach_resp
        
        # Log attempt to history
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        status = exec_resp.get("status", "unknown")
        st.session_state.history.append({
            "problem_id": prob_id,
            "timestamp": timestamp,
            "status": status,
            "runtime_ms": exec_resp.get("runtime_ms", 0) or 0,
            "hint_level": st.session_state.hint_level
        })
        
        if status == "accepted":
            st.session_state[f"solved_{prob_id}"] = True
            st.toast("Submission Accepted! All tests passed.", icon="🎉")
        else:
            st.toast("Submission recorded. Feedback generated.", icon="💡")
            
    st.session_state.is_running = False
    st.rerun()

# -------------------------------------------------------------
# BOTTOM PANEL AREA (Test Results / AI Coach / Diagnostics)
# -------------------------------------------------------------
st.write("")
st.markdown('<div class="dev-panel">', unsafe_allow_html=True)
st.markdown('<div class="dev-panel-header">📊 Output Console & AI Coach Guidance</div>', unsafe_allow_html=True)

render_bottom_panel(
    execution_result=st.session_state.execution_result,
    coach_result=st.session_state.coach_result,
    ast_status=st.session_state.ast_status,
    history=st.session_state.history,
    problem=active_problem,
    student_code=st.session_state.get(code_key, ""),
    on_hint_level_change=handle_hint_level_change,
    on_trigger_coach_feedback=trigger_coach_feedback,
    on_apply_code_suggestion=apply_code_suggestion,
    is_backend_available=is_healthy
)

st.markdown('</div>', unsafe_allow_html=True)
