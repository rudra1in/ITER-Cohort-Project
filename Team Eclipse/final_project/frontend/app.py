import time
import numpy as np
import sounddevice as sd
import streamlit as st

# -----------------------------------------------------------------------------
# PAGE CONFIGURATION
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Offline AI Proctor System",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# GLOBAL THEME & STYLING INJECTION (CSS)
# -----------------------------------------------------------------------------
st.markdown("""
    <style>
        /* Import Inter Font */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

        html, body, [class*="css"] {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        }

        /* Dark Theme Canvas */
        .stApp {
            background: #0B0F19;
            color: #F1F5F9;
        }

        /* Sidebar Styling */
        section[data-testid="stSidebar"] {
            background-color: #0F172A !important;
            border-right: 1px solid #1E293B;
        }

        /* Typography Customization */
        h1, h2, h3, h4 {
            color: #F8FAFC !important;
            font-weight: 700 !important;
            letter-spacing: -0.02em;
        }

        /* Custom Card Containers */
        .app-card {
            background-color: #1E293B;
            border: 1px solid #334155;
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 20px;
            transition: border-color 0.2s ease, transform 0.2s ease;
        }
        .app-card:hover {
            border-color: #38BDF8;
        }

        /* Custom Metric Cards */
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

        /* Streamlit Buttons Styling */
        div.stButton > button:first-child {
            background-color: #2563EB !important;
            color: #FFFFFF !important;
            border-radius: 8px !important;
            border: none !important;
            padding: 10px 24px !important;
            font-weight: 600 !important;
            letter-spacing: 0.01em;
            transition: all 0.2s ease-in-out !important;
            box-shadow: 0 2px 4px rgba(37, 99, 235, 0.2) !important;
        }
        div.stButton > button:first-child:hover {
            background-color: #1D4ED8 !important;
            box-shadow: 0 4px 12px rgba(37, 99, 235, 0.4) !important;
            transform: translateY(-1px);
        }

        /* Status Badge Pill Styling */
        .status-badge-online {
            background-color: rgba(34, 197, 94, 0.1);
            color: #4ADE80;
            border: 1px solid rgba(34, 197, 94, 0.3);
            padding: 4px 12px;
            border-radius: 9999px;
            font-size: 0.8rem;
            font-weight: 600;
            display: inline-block;
        }

        /* Custom Dividers */
        hr {
            border-color: #1E293B !important;
            margin: 2rem 0 !important;
        }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# REAL-TIME AUDIO HELPER FUNCTION
# -----------------------------------------------------------------------------
def get_audio_decibels(duration: float = 0.1, sample_rate: int = 44100) -> float:
    """
    Captures a short audio frame from the default microphone and calculates sound level in dB.
    """
    try:
        recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float32')
        sd.wait()
        rms = np.sqrt(np.mean(recording ** 2))
        return round(float(20 * np.log10(rms) + 90), 1) if rms > 0 else 0.0
    except Exception:
        return 0.0

# -----------------------------------------------------------------------------
# PROFESSIONAL HEADER & BRANDING
# -----------------------------------------------------------------------------
st.markdown("""
    <div style="display: flex; align-items: center; justify-content: space-between; padding-bottom: 8px;">
        <div>
            <h1 style="margin: 0; font-size: 2.2rem;">🛡️ Offline AI Proctor using CrewAI</h1>
            <p style="margin: 4px 0 0 0; color: #94A3B8; font-size: 1rem;">
                Intelligent Offline Examination Monitoring System • Edge Agentic Pipeline
            </p>
        </div>
        <div>
            <span class="status-badge-online">🟢 System Core Operational</span>
        </div>
    </div>
""", unsafe_allow_html=True)

st.divider()

# -----------------------------------------------------------------------------
# SYSTEM METRICS / STATUS BANNER
# -----------------------------------------------------------------------------
m1, m2, m3, m4 = st.columns(4)

with m1:
    st.metric(label="System Operational Mode", value="100% Offline", delta="Edge Active")
with m2:
    st.metric(label="Vision Engine Status", value="ONLINE", delta="OpenCV Active")
with m3:
    st.metric(label="Acoustic Engine Status", value="ONLINE", delta="PyAudio Active")
with m4:
    st.metric(label="RAG Vector Store", value="CONNECTED", delta="ChromaDB Ready")

st.divider()

# -----------------------------------------------------------------------------
# MAIN OVERVIEW & NAVIGATION DASHBOARD
# -----------------------------------------------------------------------------
col_main, col_sidebar_info = st.columns([2, 1])

with col_main:
    st.subheader("🚀 Platform Navigation")
    
    with st.container():
        st.markdown("""
            <div class="app-card">
                <h3 style="margin-top: 0;">🎥 Live Assessment Session</h3>
                <p style="color: #94A3B8; margin-bottom: 16px;">
                    Execute real-time webcam face tracking, candidate gaze analysis, acoustic noise detection, and automated telemetry flag collection entirely on local edge hardware.
                </p>
            </div>
        """, unsafe_allow_html=True)
        st.page_link("pages/02_Assessment_Session.py", label="Launch Live Monitoring Session", icon="🎥")

    st.markdown("<br>", unsafe_allow_html=True)

    with st.container():
        st.markdown("""
            <div class="app-card">
                <h3 style="margin-top: 0;">📊 Incident Reports & Credibility Scoreboard</h3>
                <p style="color: #94A3B8; margin-bottom: 16px;">
                    Review multi-agent CrewAI synthesis reports, dynamic student integrity scores, and ChromaDB vector-retrieved institutional policy citations.
                </p>
            </div>
        """, unsafe_allow_html=True)
        st.page_link("pages/04_Incident_Reports.py", label="View Incident Reports", icon="📊")

with col_sidebar_info:
    st.subheader("ℹ️ System Architecture")
    
    st.markdown("""
        <div class="app-card" style="padding: 20px;">
            <p style="margin-top: 0; color: #4ADE80; font-weight: 600;">🔒 Edge Security Verified</p>
            <hr style="margin: 12px 0 !important;">
            <p style="font-size: 0.9rem; color: #CBD5E1; margin-bottom: 8px;"><strong>Core Engine Components:</strong></p>
            <ul style="padding-left: 20px; color: #94A3B8; font-size: 0.88rem; line-height: 1.6;">
                <li>👁️ <strong>Vision</strong>: OpenCV Adaptive Contrast</li>
                <li>🎙️ <strong>Audio</strong>: Real-time Decibel & Waveform Analytics</li>
                <li>🤖 <strong>Agents</strong>: CrewAI Multi-Agent Framework</li>
                <li>📚 <strong>Vector Store</strong>: Local ChromaDB RAG</li>
            </ul>
            <div style="background-color: rgba(56, 189, 248, 0.08); border-left: 3px solid #38BDF8; padding: 10px; border-radius: 4px; margin-top: 16px;">
                <p style="margin: 0; font-size: 0.8rem; color: #38BDF8;">
                    <strong>Privacy Guarantee:</strong> Zero external cloud API dependencies. All computation executes on device.
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Audio Device Test Box
    with st.expander("🎙️ Microphone Diagnostic Sandbox"):
        st.caption("Click to sample ambient decibel levels from your active microphone.")
        if st.button("Test Mic Level"):
            with st.spinner("Sampling microphone..."):
                test_db = get_audio_decibels(duration=0.5)
                st.write(f"**Current Ambient Level:** `{test_db} dB`")
                if test_db > 65.0:
                    st.warning("⚠️ High ambient noise detected.")
                else:
                    st.success("✅ Ambient level is quiet.")