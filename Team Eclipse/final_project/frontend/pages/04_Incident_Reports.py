import os
import json
import pandas as pd
import streamlit as st

# -----------------------------------------------------------------------------
# PAGE CONFIGURATION
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Incident Reports & Scoreboard",
    page_icon="📊",
    layout="wide"
)

# -----------------------------------------------------------------------------
# STYLING INJECTION
# -----------------------------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    .stApp {
        background: #0B0F19;
        color: #F1F5F9;
    }
    /* Metric Box Styling */
    div[data-testid="stMetric"] {
        background-color: #1E293B !important;
        border: 1px solid #334155 !important;
        border-radius: 12px !important;
        padding: 20px !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3) !important;
    }
    div[data-testid="stMetricLabel"] {
        font-size: 0.85rem !important;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #94A3B8 !important;
        font-weight: 600 !important;
    }
    div[data-testid="stMetricValue"] {
        color: #38BDF8 !important;
        font-size: 1.8rem !important;
        font-weight: 700 !important;
    }
    .app-card {
        background-color: #1E293B;
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 24px;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# DATA PERSISTENCE & HISTORY MANAGEMENT ENGINE
# -----------------------------------------------------------------------------
HISTORY_FILE = os.path.join(os.getcwd(), "all_assessment_sessions.json")
LATEST_FILE = os.path.join(os.getcwd(), "latest_assessment.json")

def load_all_history() -> list:
    """Reads all saved historical sessions from disk."""
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r") as f:
                return json.load(f)
        except Exception:
            return []
    return []

def save_history(history_list: list):
    """Saves updated sessions history list to disk."""
    with open(HISTORY_FILE, "w") as f:
        json.dump(history_list, f, indent=4)

def sync_latest_session_to_history():
    """Checks if a latest_assessment.json exists and merges it into history."""
    if not os.path.exists(LATEST_FILE):
        return
    try:
        with open(LATEST_FILE, "r") as f:
            latest_session = json.load(f)
        history = load_all_history()
        s_id = latest_session.get("session_id", "UNKNOWN_SESS")
        
        existing_idx = next((i for i, item in enumerate(history) if item.get("session_id") == s_id), None)
        if existing_idx is not None:
            history[existing_idx] = latest_session
        else:
            history.append(latest_session)
        save_history(history)
    except Exception as e:
        st.error(f"Error syncing latest session to history: {e}")

sync_latest_session_to_history()
all_sessions = load_all_history()

# -----------------------------------------------------------------------------
# HEADER SECTION
# -----------------------------------------------------------------------------
st.title("📋 Exam Incident Reports & Session History")
st.caption("Automated Multi-Agent Evaluation & Cumulative Session Database")
st.divider()

# Absolute Penalty Weight Map
PENALTY_WEIGHTS = {
    "NO_FACE_DETECTED": 15.0,
    "MULTIPLE_FACES_DETECTED": 30.0,
    "GAZE_AWAY": 5.0,
    "HIGH_NOISE_DETECTED": 10.0,
    "TAB_SWITCH": 25.0
}

if not all_sessions:
    st.info("No assessment history recorded yet. Complete an exam in '02 Assessment Session' first.")
    st.stop()

# -----------------------------------------------------------------------------
# SIDEBAR SESSION SWITCHER
# -----------------------------------------------------------------------------
with st.sidebar:
    st.markdown("### 📜 Session Records Archive")
    session_options = [f"{s.get('session_id', 'SESS')} - {s.get('student_id', 'STU')}" for s in all_sessions]
    selected_option = st.selectbox("Select Historical Session", options=session_options, index=len(session_options) - 1)
    
    selected_index = session_options.index(selected_option)
    selected_session = all_sessions[selected_index]

# Extract selected session properties
session_id = selected_session.get("session_id", "N/A")
student_id = selected_session.get("student_id", "N/A")
logs = selected_session.get("events", [])

# -----------------------------------------------------------------------------
# ABSOLUTE SCORE CALCULATION FOR SELECTED SESSION
# -----------------------------------------------------------------------------
BASE_SCORE = 100.0
total_deductions = sum(PENALTY_WEIGHTS.get(log.get("type") or log.get("status"), 5.0) for log in logs)
absolute_score = max(0.0, BASE_SCORE - total_deductions)
total_flags = len(logs)

if absolute_score >= 75.0:
    verdict, verdict_color = "PASS", "#4ADE80"
elif absolute_score >= 50.0:
    verdict, verdict_color = "NEEDS REVIEW", "#FACC15"
else:
    verdict, verdict_color = "FAIL", "#F87171"

# -----------------------------------------------------------------------------
# METRICS DISPLAY BANNER
# -----------------------------------------------------------------------------
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.metric(label="Candidate ID", value=student_id)
with m2:
    st.metric(
        label="Absolute Credibility", 
        value=f"{absolute_score:.1f}%", 
        delta=f"-{total_deductions:.1f}% Cumulative" if total_deductions > 0 else "100%",
        delta_color="inverse"
    )
with m3:
    st.metric(label="Final Verdict", value=verdict)
with m4:
    st.metric(
        label="Total Session Flags", 
        value=f"{total_flags} Flags", 
        delta="HIGH RISK" if total_flags >= 5 else "NORMAL",
        delta_color="inverse"
    )

st.divider()

# -----------------------------------------------------------------------------
# DETAILED AUDIT LOG & BREAKDOWN FOR SELECTED SESSION
# -----------------------------------------------------------------------------
col_logs, col_summary = st.columns([2, 1])

with col_logs:
    st.subheader(f"📜 Session Telemetry Log History ({session_id})")
    if logs:
        st.dataframe(pd.DataFrame(logs), use_container_width=True)
    else:
        st.success("No violation flags recorded for this session. Candidate maintained 100% integrity.")

with col_summary:
    st.subheader("🤖 CrewAI Verdict Summary")
    st.markdown(f"""
    <div class="app-card">
        <h4 style="margin-top:0; color:{verdict_color};">Status: {verdict}</h4>
        <p style="color: #94A3B8; font-size:0.9rem;">
            <strong>Baseline Score:</strong> 100.0%<br>
            <strong>Total Session Deductions:</strong> -{total_deductions:.1f}%<br>
            <strong>Absolute Score:</strong> {absolute_score:.1f}% / 100.0%<br>
            <strong>Policy Compliance:</strong> {'Violated' if verdict == 'FAIL' else 'Compliant'}
        </p>
        <hr style="margin: 12px 0;">
        <p style="font-size:0.8rem; color:#CBD5E1;">
            <em>Evaluated cumulatively across all timestamped audio and vision telemetry logs for {session_id}.</em>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Download button for selected session report
    report_json = json.dumps(selected_session, indent=4)
    st.download_button(
        label="📥 Download Session Report (JSON)",
        data=report_json,
        file_name=f"report_{session_id}_{student_id}.json",
        mime="application/json",
        use_container_width=True
    )

# -----------------------------------------------------------------------------
# ALL HISTORICAL SESSIONS OVERVIEW TABLE
# -----------------------------------------------------------------------------
st.divider()
st.subheader("📚 All Historical Assessment Sessions Overview")

history_summary = []
for s in all_sessions:
    s_logs = s.get("events", [])
    s_deductions = sum(PENALTY_WEIGHTS.get(l.get("type") or l.get("status"), 5.0) for l in s_logs)
    s_score = max(0.0, 100.0 - s_deductions)
    
    history_summary.append({
        "Session ID": s.get("session_id"),
        "Student ID": s.get("student_id"),
        "Total Violations": len(s_logs),
        "Deductions": f"-{s_deductions:.1f}%",
        "Absolute Score": f"{s_score:.1f}%",
        "Verdict": "PASS" if s_score >= 75.0 else ("NEEDS REVIEW" if s_score >= 50.0 else "FAIL")
    })

st.dataframe(pd.DataFrame(history_summary), use_container_width=True)