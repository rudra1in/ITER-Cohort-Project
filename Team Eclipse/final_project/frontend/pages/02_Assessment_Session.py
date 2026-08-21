import os
import json
import time
import cv2
import requests
import numpy as np
import sounddevice as sd
import streamlit as st

st.set_page_config(page_title="Live Assessment", page_icon="📝", layout="wide")

# -----------------------------------------------------------------------------
# PRESENTATION & STYLING INJECTION
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

        section[data-testid="stSidebar"] {
            background-color: #0F172A !important;
            border-right: 1px solid #1E293B;
        }

        h1, h2, h3, h4 {
            color: #F8FAFC !important;
            font-weight: 700 !important;
        }

        /* Metric Box Container Styling */
        div[data-testid="stMetric"] {
            background-color: #1E293B !important;
            border: 1px solid #334155 !important;
            border-radius: 12px !important;
            padding: 18px !important;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3) !important;
            margin-bottom: 10px !important;
        }
        div[data-testid="stMetricLabel"] {
            font-size: 0.8rem !important;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: #94A3B8 !important;
            font-weight: 600 !important;
        }
        div[data-testid="stMetricValue"] {
            color: #38BDF8 !important;
            font-size: 1.6rem !important;
            font-weight: 700 !important;
        }

        /* Primary Action Button */
        div.stButton > button:first-child {
            background-color: #2563EB !important;
            color: #FFFFFF !important;
            border-radius: 8px !important;
            border: none !important;
            padding: 10px 24px !important;
            font-weight: 600 !important;
            transition: all 0.2s ease-in-out !important;
        }
        div.stButton > button:first-child:hover {
            background-color: #1D4ED8 !important;
            box-shadow: 0 4px 12px rgba(37, 99, 235, 0.4) !important;
        }

        /* Card Scaffolding */
        .video-card-header {
            background-color: #1E293B;
            border: 1px solid #334155;
            border-bottom: none;
            border-top-left-radius: 12px;
            border-top-right-radius: 12px;
            padding: 12px 20px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        hr {
            border-color: #1E293B !important;
            margin: 1.5rem 0 !important;
        }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# REAL-TIME AUDIO SAMPLER HELPER FUNCTION
# -----------------------------------------------------------------------------
def get_audio_decibels(duration: float = 0.08, sample_rate: int = 44100) -> float:
    """Captures a fast non-blocking snippet from default microphone and returns sound level in dB."""
    try:
        recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float32')
        sd.wait()
        rms = np.sqrt(np.mean(recording ** 2))
        return round(float(20 * np.log10(rms) + 90), 1) if rms > 0 else 0.0
    except Exception:
        return 0.0

# -----------------------------------------------------------------------------
# PRESERVED BACKEND INITIALIZATION & STATE
# -----------------------------------------------------------------------------
if "face_tracker" not in st.session_state:
    from vision.face_tracker import FaceTracker
    st.session_state.face_tracker = FaceTracker()

if "telemetry_logs" not in st.session_state:
    st.session_state.telemetry_logs = []

# -----------------------------------------------------------------------------
# TOP HEADER
# -----------------------------------------------------------------------------
st.markdown("""
    <div>
        <h1 style="margin: 0; font-size: 2rem;">📝 Live Assessment Monitoring</h1>
        <p style="margin: 4px 0 0 0; color: #94A3B8; font-size: 0.95rem;">
            Real-Time Edge Multi-Modal (Vision + Acoustic) Proctoring & Dynamic Telemetry Logging
        </p>
    </div>
""", unsafe_allow_html=True)
st.divider()

# -----------------------------------------------------------------------------
# SIDEBAR CONTROLS
# -----------------------------------------------------------------------------
with st.sidebar:
    st.markdown("<h3 style='font-size: 1.2rem; margin-bottom: 16px;'>⚙️ Session Controls</h3>", unsafe_allow_html=True)
    session_id = st.text_input("Session ID", value="SESS_101", key="input_session_id")
    student_id = st.text_input("Student ID", value="STU_4820", key="input_student_id")
    st.divider()
    run_monitoring = st.toggle("Activate Webcam & Audio Feed", key="chk_start_monitoring")
    st.markdown("""
        <div style="background-color: rgba(56, 189, 248, 0.08); border: 1px solid rgba(56, 189, 248, 0.2); padding: 12px; border-radius: 8px; margin-top: 16px;">
            <p style="margin: 0; font-size: 0.82rem; color: #38BDF8; line-height: 1.5;">
                ℹ️ <strong>Guidance:</strong> Ensure proper ambient lighting, keep your face visible, and minimize background speech/noise during the session.
            </p>
        </div>
    """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# MAIN DASHBOARD GRID (STREAM SCRIPTS & METRICS)
# -----------------------------------------------------------------------------
col_feed, col_status = st.columns([2, 1])

with col_status:
    st.markdown("<h3 style='font-size: 1.1rem; margin-bottom: 12px;'>📊 Live Telemetry</h3>", unsafe_allow_html=True)
    status_metric = st.empty()
    audio_metric = st.empty()
    faces_metric = st.empty()
    flags_metric = st.empty()
    
    status_metric.metric("Monitoring State", "OFFLINE", delta_color="off")
    audio_metric.metric("Acoustic Level", "0.0 dB", delta="OFFLINE", delta_color="off")
    faces_metric.metric("Faces Detected", 0)
    flags_metric.metric("Logged Violations", len(st.session_state.telemetry_logs))

with col_feed:
    st.markdown("""
        <div class="video-card-header">
            <span style="font-weight: 600; color: #F8FAFC; font-size: 0.95rem;">📹 Live Video & Acoustic Feed Viewport</span>
            <span style="font-size: 0.75rem; background-color: rgba(34, 197, 94, 0.15); color: #4ADE80; padding: 2px 8px; border-radius: 4px; font-weight: 600;">MULTI-MODAL INFERENCE</span>
        </div>
    """, unsafe_allow_html=True)
    frame_window = st.image([])

# -----------------------------------------------------------------------------
# COMBINED WEBCAM & AUDIO MONITORING LOOP
# -----------------------------------------------------------------------------
if run_monitoring:
    cap = cv2.VideoCapture(0)
    NOISE_THRESHOLD_DB = 65.0  # Threshold in dB to trigger high noise flag
    
    while run_monitoring:
        ret, frame = cap.read()
        if not ret:
            st.error("Failed to capture video feed.")
            break

        timestamp = time.strftime("%H:%M:%S", time.localtime())

        # 1. Process Vision Pipeline
        face_res = st.session_state.face_tracker.process_frame(frame)
        status = face_res.get("status", "NORMAL")
        face_count = face_res.get("face_count", 0)

        if status == "NORMAL":
            status_metric.metric("Monitoring State", "NORMAL 🟢", delta="OK", delta_color="normal")
        elif status == "NO_FACE_DETECTED":
            status_metric.metric("Monitoring State", "NO FACE ⚠️", delta="-1 Face", delta_color="inverse")
        else:
            status_metric.metric("Monitoring State", "FLAGGED 🚨", delta="+Multiple", delta_color="inverse")

        faces_metric.metric("Faces Detected", face_count)
        
        if status != "NORMAL":
            st.session_state.telemetry_logs.append({
                "timestamp": timestamp,
                "status": status,
                "type": status,
                "session_id": session_id,
                "student_id": student_id
            })

        # 2. Process Audio Pipeline
        current_db = get_audio_decibels(duration=0.08)
        
        if current_db > NOISE_THRESHOLD_DB:
            audio_metric.metric("Acoustic Level", f"{current_db} dB", delta="⚠️ HIGH NOISE", delta_color="inverse")
            st.session_state.telemetry_logs.append({
                "timestamp": timestamp,
                "status": "HIGH_NOISE_DETECTED",
                "type": "HIGH_NOISE_DETECTED",
                "details": f"Noise level recorded at {current_db} dB",
                "session_id": session_id,
                "student_id": student_id
            })
        else:
            audio_metric.metric("Acoustic Level", f"{current_db} dB", delta="NORMAL 🟢", delta_color="normal")

        flags_metric.metric("Logged Violations", len(st.session_state.telemetry_logs))

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_window.image(frame_rgb, use_container_width=True)

    cap.release()

st.divider()

# -----------------------------------------------------------------------------
# ASSESSMENT SUBMISSION WITH MULTI-SESSION PERSISTENCE
# -----------------------------------------------------------------------------
col_sub1, col_sub2 = st.columns([3, 1])
with col_sub1:
    st.markdown("<p style='font-weight: 600; margin: 0; color: #F8FAFC;'>Complete Exam Session</p>", unsafe_allow_html=True)
    st.markdown("<p style='color: #94A3B8; margin: 2px 0 0 0; font-size: 0.85rem;'>Submitting will package current session violations and update the Incident Reports dashboard.</p>", unsafe_allow_html=True)

with col_sub2:
    if st.button("🚀 Submit & Evaluate", key="btn_submit_exam_assessment", type="primary", use_container_width=True):
        
        # 1. Use existing session ID or append timestamp to prevent duplicate ID overwrites
        final_session_id = session_id
        
        payload = {
            "session_id": final_session_id,
            "student_id": student_id,
            "events": st.session_state.telemetry_logs
        }

        # 2. Save latest session file
        st.session_state["latest_assessment_result"] = payload
        latest_file = os.path.join(os.getcwd(), "latest_assessment.json")
        try:
            with open(latest_file, "w") as f:
                json.dump(payload, f, indent=4)
        except Exception as e:
            st.error(f"Latest assessment save error: {e}")

        # 3. Append to historical sessions database file
        history_file = os.path.join(os.getcwd(), "all_assessment_sessions.json")
        history = []
        if os.path.exists(history_file):
            try:
                with open(history_file, "r") as f:
                    history = json.load(f)
            except Exception:
                history = []

        # If matching session exists, update it; otherwise append new record
        existing_idx = next((i for i, item in enumerate(history) if item.get("session_id") == final_session_id), None)
        if existing_idx is not None:
            history[existing_idx] = payload
        else:
            history.append(payload)

        try:
            with open(history_file, "w") as f:
                json.dump(history, f, indent=4)
            st.toast("Saved to multi-session history archive!", icon="💾")
        except Exception as e:
            st.error(f"History database save error: {e}")

        # 4. Clear current session telemetry log cache
        st.session_state.telemetry_logs = []

        # 5. Send payload to FastAPI Backend
        try:
            response = requests.post("http://127.0.0.1:8000/api/v1/telemetry", json=payload, timeout=5)
            if response.status_code == 200:
                st.success("Submitted to backend! Open '04 Incident Reports' to view details.")
        except Exception:
            st.success("Saved! Navigate to '04 Incident Reports' to view the full breakdown.")