"""
Offline Behavioral Analysis & Evidence RAG System
=================================================
Streamlit UI  –  v0.4.0

Four tabs:
  Chat        – Conversational RAG / LangGraph interface
  Events      – Filterable event table + evidence image gallery
  Candidates  – Per-candidate timeline & behavioral summary
  Pipeline    – Ingest, analyze, index, cluster controls
"""

import os
import uuid
import json

import requests
import streamlit as st


# =========================================================
# CONFIG
# =========================================================

API_URL = os.getenv(
    "API_URL",
    "http://127.0.0.1:8000"
)

EVENT_TYPE_COLORS = {
    "repeated_side_looking": "#e67e22",
    "phone_visible":          "#e74c3c",
    "body_turned_away":       "#8e44ad",
    "excessive_movement":     "#2980b9",
    "absent_from_frame":      "#c0392b",
    "extra_person_detected":  "#16a085",
}

EVENT_TYPE_ICONS = {
    "repeated_side_looking": "👁",
    "phone_visible":          "📱",
    "body_turned_away":       "🔄",
    "excessive_movement":     "⚡",
    "absent_from_frame":      "❌",
    "extra_person_detected":  "👥",
}


# =========================================================
# PAGE SETUP
# =========================================================

st.set_page_config(
    page_title="Behavioral Analysis System",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>
    /* ---- Typography ---- */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

    /* ---- Sidebar ---- */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f1117 0%, #1a1d27 100%);
        border-right: 1px solid #2d2d3a;
    }
    [data-testid="stSidebar"] * { color: #e8e8f0 !important; }

    /* ---- Event badges ---- */
    .event-badge {
        display: inline-block;
        padding: 2px 10px;
        border-radius: 12px;
        font-size: 12px;
        font-weight: 600;
        color: #fff;
        margin: 2px 0;
    }
    .suspicious-banner {
        background: rgba(231,76,60,0.15);
        border-left: 3px solid #e74c3c;
        border-radius: 0 8px 8px 0;
        padding: 8px 14px;
        margin: 4px 0;
    }
    .common-banner {
        background: rgba(39,174,96,0.1);
        border-left: 3px solid #27ae60;
        border-radius: 0 8px 8px 0;
        padding: 8px 14px;
        margin: 4px 0;
    }

    /* ---- Evidence image card ---- */
    .evidence-card {
        background: #1e2130;
        border: 1px solid #2d2d3a;
        border-radius: 10px;
        padding: 8px;
        margin: 4px;
    }

    /* ---- Pipeline step ---- */
    .step-card {
        background: #1a1d27;
        border: 1px solid #2d3250;
        border-radius: 10px;
        padding: 14px 18px;
        margin-bottom: 12px;
    }
    .step-number {
        font-size: 22px;
        font-weight: 700;
        color: #5b8dee;
    }

    /* ---- Metrics ---- */
    [data-testid="stMetric"] {
        background: #1e2130;
        border: 1px solid #2d2d3a;
        border-radius: 8px;
        padding: 10px 14px;
    }

    /* ---- Mode chip ---- */
    .mode-chip {
        display: inline-block;
        padding: 3px 12px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: 600;
        letter-spacing: 0.5px;
        text-transform: uppercase;
    }
    .mode-rag   { background: #1a4a6e; color: #5b8dee; }
    .mode-tools { background: #1a4a1a; color: #27ae60; }
    .mode-crew  { background: #4a1a4a; color: #9b59b6; }
    .mode-error { background: #4a1a1a; color: #e74c3c; }

    /* ---- Divider ---- */
    hr { border-color: #2d2d3a !important; }

    /* ---- Chat message ---- */
    [data-testid="stChatMessage"] {
        border-radius: 12px;
        margin-bottom: 8px;
    }

    /* ---- Hide Streamlit branding ---- */
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)


# =========================================================
# SESSION STATE
# =========================================================

def init_session():
    defaults = {
        "session_id": f"SESSION_{uuid.uuid4().hex[:10]}",
        "messages": [],
        "test_id": None,
        "last_mode": None,
        "last_tool_calls": [],
    }
    for key, val in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = val

init_session()


# =========================================================
# API HELPERS
# =========================================================

def api_get(endpoint, timeout=30):
    response = requests.get(
        f"{API_URL}{endpoint}",
        timeout=timeout
    )
    response.raise_for_status()
    return response.json()


def api_post(endpoint, payload, timeout=600):
    response = requests.post(
        f"{API_URL}{endpoint}",
        json=payload,
        timeout=timeout
    )
    response.raise_for_status()
    return response.json()


@st.cache_data(ttl=5)
def get_tests():
    try:
        return api_get("/tests").get("tests", [])
    except Exception:
        return []


@st.cache_data(ttl=10)
def get_test_summary(test_id):
    try:
        return api_get(f"/tests/{test_id}")
    except Exception:
        return {}


@st.cache_data(ttl=10)
def get_candidates(test_id):
    try:
        return api_get(f"/tests/{test_id}/candidates").get("candidates", [])
    except Exception:
        return []


@st.cache_data(ttl=15)
def get_events(test_id, suspicious_only=False):
    try:
        return api_get(
            f"/tests/{test_id}/events"
            f"?suspicious_only={str(suspicious_only).lower()}"
        ).get("events", [])
    except Exception:
        return []


@st.cache_data(ttl=15)
def get_candidate_timeline(test_id, candidate_id):
    try:
        return api_get(
            f"/tests/{test_id}/candidates/{candidate_id}/timeline"
        ).get("events", [])
    except Exception:
        return []


@st.cache_data(ttl=15)
def get_statistics(test_id):
    try:
        return api_get(f"/tests/{test_id}/statistics").get("statistics", [])
    except Exception:
        return []


@st.cache_data(ttl=60)
def get_health():
    try:
        return api_get("/health")
    except Exception:
        return {}


@st.cache_data(ttl=5)
def get_llm_status():
    try:
        return api_get("/llm/status")
    except Exception:
        return {}


# =========================================================
# EVIDENCE DISPLAY
# =========================================================

def display_evidence(evidence, max_items=12, cols=3):
    """Render evidence images in a responsive grid."""

    if not evidence:
        st.info("No evidence images linked to these results.")
        return

    # Deduplicate.
    unique = {}
    for item in evidence:
        fid = item.get("frame_id")
        if fid and fid not in unique:
            unique[fid] = item

    items = list(unique.values())[:max_items]

    if not items:
        st.info("No evidence images available.")
        return

    columns = st.columns(min(len(items), cols))

    for idx, item in enumerate(items):
        col = columns[idx % len(columns)]
        image_path = (item.get("image_path") or "").replace("\\", "/")
        event_type = item.get("event_type", "")
        color = EVENT_TYPE_COLORS.get(event_type, "#555")
        icon = EVENT_TYPE_ICONS.get(event_type, "📷")

        with col:
            if image_path and os.path.exists(image_path):
                st.image(
                    image_path,
                    caption=(
                        f"{icon} {item.get('candidate_id', '?')}  "
                        f"·  {item.get('timestamp', '')}"
                    ),
                    use_container_width=True
                )
                st.markdown(
                    f"<div class='event-badge' "
                    f"style='background:{color}'>"
                    f"{event_type}</div>",
                    unsafe_allow_html=True
                )
            else:
                st.warning("Image unavailable")
                st.caption(image_path or "No path")


# =========================================================
# EVENT TYPE BADGE (inline HTML)
# =========================================================

def event_badge(event_type):
    color = EVENT_TYPE_COLORS.get(event_type, "#666")
    icon = EVENT_TYPE_ICONS.get(event_type, "")
    return (
        f"<span class='event-badge' style='background:{color}'>"
        f"{icon} {event_type}"
        f"</span>"
    )


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("## Behavioral Analysis")
    st.markdown("*Post-test evidence review system*")
    st.divider()

    # --- Health ---
    health = get_health()
    api_ok = health.get("api") == "ok"
    llm_ok = health.get("llm_reachable", False)
    vec_count = health.get("vector_store_count", 0)

    st.markdown("**System Status**")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            f"{'🟢' if api_ok else '🔴'} API  "
            f"{'🟢' if llm_ok else '🔴'} LLM"
        )
    with col2:
        st.markdown(f"📦 {vec_count} vectors")

    if health.get("orchestrator"):
        st.caption(f"Orchestrator: {health['orchestrator']}")

    st.divider()

    # --- LLM provider toggle ---
    st.markdown("**LLM Provider**")

    llm_status = get_llm_status()
    current_provider = llm_status.get("active_provider", "gemini")

    gemini_info = llm_status.get("gemini", {})
    ollama_info = llm_status.get("ollama", {})

    provider_labels = {
        "gemini": f"Gemini ({gemini_info.get('model', '?')})",
        "ollama": f"Ollama ({ollama_info.get('model', '?')})"
    }

    selected_label = st.radio(
        "LLM Provider",
        options=["gemini", "ollama"],
        format_func=lambda p: provider_labels[p],
        index=["gemini", "ollama"].index(current_provider),
        label_visibility="collapsed",
        horizontal=True,
        key="llm_provider_radio"
    )

    if not gemini_info.get("configured"):
        st.caption("⚠️ Gemini has no API key configured")

    if selected_label != current_provider:
        try:
            api_post(
                "/llm/switch",
                {"provider": selected_label},
                timeout=15
            )
            get_llm_status.clear()
            get_health.clear()
            st.rerun()
        except Exception as error:
            st.error(f"Could not switch provider: {error}")

    st.divider()

    # --- Test selector ---
    st.markdown("**Select Test**")
    tests = get_tests()

    if tests:
        test_ids = [t["test_id"] for t in tests]
        selected_test = st.selectbox(
            "Test",
            test_ids,
            label_visibility="collapsed"
        )
        st.session_state.test_id = selected_test
    else:
        st.warning("No tests found. Use the Pipeline tab to ingest data.")
        st.session_state.test_id = None

    # --- Test metrics ---
    if st.session_state.test_id:
        test_id = st.session_state.test_id
        summary = get_test_summary(test_id)
        candidates = get_candidates(test_id)

        col1, col2, col3 = st.columns(3)
        col1.metric("Frames", summary.get("frames", 0))
        col2.metric("Events", summary.get("behavior_events", 0))
        col3.metric("Candidates", len(candidates))

    st.divider()

    # --- Reset session ---
    if st.button(" New conversation"):
        st.session_state.session_id = (
            f"SESSION_{uuid.uuid4().hex[:10]}"
        )
        st.session_state.messages = []
        st.session_state.last_mode = None
        st.session_state.last_tool_calls = []
        st.rerun()

    st.caption(f"Session: {st.session_state.session_id[-8:]}")


# =========================================================
# MAIN TABS
# =========================================================

tab_chat, tab_events, tab_candidates, tab_pipeline = st.tabs([
    " Chat",
    " Events",
    " Candidates",
    " Pipeline",
])


# =========================================================
# TAB 1 — CHAT
# =========================================================

with tab_chat:

    if not st.session_state.test_id:
        st.info(" Select a test from the sidebar to begin.")
        st.stop()

    # Header
    st.markdown(
        f"### Behavioral Evidence Q&A  "
        f"<small style='color:#888'>— {st.session_state.test_id}</small>",
        unsafe_allow_html=True
    )

    # Render conversation history
    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

            if message["role"] == "assistant":

                # Mode chip
                mode = message.get("mode", "rag")
                st.markdown(
                    f"<span class='mode-chip mode-{mode}'>{mode}</span>",
                    unsafe_allow_html=True
                )

                # Tool calls disclosure
                tool_calls = message.get("tool_calls", [])
                if tool_calls:
                    with st.expander(
                        f" {len(tool_calls)} tool call(s) used"
                    ):
                        for tc in tool_calls:
                            if tc.get("tool") == "error":
                                st.error(
                                    f"Tool selection failed: "
                                    f"{tc.get('result', 'unknown error')}"
                                )
                            else:
                                st.code(
                                    f"{tc.get('tool')}("
                                    f"{json.dumps(tc.get('args', {}), indent=2)})"
                                    f"\n-> {str(tc.get('result'))[:500]}",
                                    language="json"
                                )

                # Evidence images
                evidence = message.get("evidence", [])
                if evidence:
                    with st.expander(
                        f" {len(evidence)} evidence frame(s)"
                    ):
                        display_evidence(evidence, max_items=9)

    # Chat input
    prompt = st.chat_input(
        "Ask about behavioral observations, candidates, events…"
    )

    if prompt:

        # Append user message.
        st.session_state.messages.append(
            {"role": "user", "content": prompt}
        )

        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Retrieving evidence and generating answer…"):

                try:
                    result = api_post(
                        "/chat",
                        {
                            "test_id": st.session_state.test_id,
                            "session_id": st.session_state.session_id,
                            "question": prompt,
                        }
                    )

                    answer = result.get("answer", "No answer returned.")
                    evidence = result.get("evidence", [])
                    mode = result.get("mode", "rag")
                    tool_calls = result.get("tool_calls", [])

                    st.markdown(answer)
                    st.markdown(
                        f"<span class='mode-chip mode-{mode}'>{mode}</span>",
                        unsafe_allow_html=True
                    )

                    if tool_calls:
                        with st.expander(
                            f" {len(tool_calls)} tool call(s) used"
                        ):
                            for tc in tool_calls:
                                if tc.get("tool") == "error":
                                    st.error(
                                        f"Tool selection failed: "
                                        f"{tc.get('result', 'unknown error')}"
                                    )
                                else:
                                    st.code(
                                        f"{tc.get('tool')}("
                                        f"{json.dumps(tc.get('args', {}), indent=2)})"
                                        f"\n-> {str(tc.get('result'))[:500]}",
                                        language="json"
                                    )

                    if evidence:
                        with st.expander(
                            f" {len(evidence)} evidence frame(s)"
                        ):
                            display_evidence(evidence, max_items=9)

                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": answer,
                        "mode": mode,
                        "tool_calls": tool_calls,
                        "evidence": evidence,
                    })

                    # Cache for sidebar
                    st.session_state.last_mode = mode
                    st.session_state.last_tool_calls = tool_calls

                except Exception as error:
                    err_msg = f"Request failed: {error}"
                    st.error(err_msg)
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": err_msg,
                        "mode": "error",
                    })


# =========================================================
# TAB 2 — EVENTS
# =========================================================

with tab_events:

    if not st.session_state.test_id:
        st.info("Select a test from the sidebar.")
        st.stop()

    test_id = st.session_state.test_id
    st.markdown(f"### Behavioral Events  —  `{test_id}`")

    # --- Controls ---
    ctrl_col1, ctrl_col2, ctrl_col3, ctrl_col4 = st.columns([2, 2, 2, 2])

    with ctrl_col1:
        suspicious_only = st.toggle(
            "Suspicious only",
            value=False
        )

    with ctrl_col2:
        candidates = get_candidates(test_id)
        candidate_filter = st.selectbox(
            "Filter by candidate",
            ["All"] + candidates,
            key="event_candidate_filter"
        )

    with ctrl_col3:
        event_type_options = [
            "All",
            "repeated_side_looking",
            "phone_visible",
            "body_turned_away",
            "excessive_movement",
            "absent_from_frame",
            "extra_person_detected",
        ]
        type_filter = st.selectbox(
            "Filter by event type",
            event_type_options,
            key="event_type_filter"
        )

    with ctrl_col4:
        if st.button(" Run clustering", key="cluster_btn_events"):
            try:
                r = api_post(f"/tests/{test_id}/cluster", {})
                st.success(
                    f"✅ Clustered {r['events_clustered']} events: "
                    f"{r['suspicious']} suspicious, "
                    f"{r['common']} common."
                )
                get_events.clear()
            except Exception as e:
                st.error(f"Clustering failed: {e}")

    # --- Load events ---
    all_events = get_events(test_id, suspicious_only=suspicious_only)

    # Apply filters.
    if candidate_filter != "All":
        all_events = [
            e for e in all_events
            if e.get("candidate_id") == candidate_filter
        ]

    if type_filter != "All":
        all_events = [
            e for e in all_events
            if e.get("event_type") == type_filter
        ]

    st.caption(f"{len(all_events)} event(s) shown")

    if not all_events:
        st.info("No events match the current filters.")
    else:
        # Summary counts per type
        type_counts = {}
        for e in all_events:
            t = e.get("event_type", "unknown")
            type_counts[t] = type_counts.get(t, 0) + 1

        badge_cols = st.columns(min(len(type_counts), 6))
        for i, (t, c) in enumerate(sorted(
            type_counts.items(),
            key=lambda x: -x[1]
        )):
            color = EVENT_TYPE_COLORS.get(t, "#666")
            icon = EVENT_TYPE_ICONS.get(t, "")
            with badge_cols[i % len(badge_cols)]:
                st.markdown(
                    f"<div class='event-badge' style='background:{color}'>"
                    f"{icon} {t}<br>"
                    f"<span style='font-size:16px;font-weight:700'>{c}</span>"
                    f"</div>",
                    unsafe_allow_html=True
                )

        st.divider()

        # Event list
        for event in all_events:

            is_suspicious = bool(event.get("is_suspicious"))
            banner_class = (
                "suspicious-banner"
                if is_suspicious
                else "common-banner"
            )

            flag = "⚑ FLAGGED" if is_suspicious else ""
            label = event.get("cluster_label", "not clustered")
            event_type = event.get("event_type", "unknown")
            color = EVENT_TYPE_COLORS.get(event_type, "#666")
            icon = EVENT_TYPE_ICONS.get(event_type, "")

            with st.expander(
                f"{icon} {event.get('candidate_id')}  ·  "
                f"{event_type}  ·  "
                f"{event.get('duration', 0):.0f}s  "
                f"{flag}"
            ):

                st.markdown(
                    f"<div class='{banner_class}'>"
                    f"{event.get('description', '')}"
                    f"</div>",
                    unsafe_allow_html=True
                )

                info_col1, info_col2, info_col3, info_col4 = (
                    st.columns(4)
                )

                info_col1.metric(
                    "Start",
                    event.get("start_time", "–")
                )
                info_col2.metric(
                    "End",
                    event.get("end_time", "–")
                )
                info_col3.metric(
                    "Duration",
                    f"{event.get('duration', 0):.1f}s"
                )
                info_col4.metric(
                    "Confidence",
                    f"{event.get('confidence', 0):.2f}"
                )

                st.caption(
                    f"Event ID: {event.get('event_id')}  ·  "
                    f"Cluster: {label}  ·  "
                    f"Track: {event.get('track_id')}"
                )

                # Evidence frames for this event.
                evidence_json = event.get("evidence_json", "[]")
                try:
                    frame_ids = json.loads(evidence_json)
                except Exception:
                    frame_ids = []

                if frame_ids:
                    st.caption(
                        f"Evidence frames: {len(frame_ids)}"
                    )


# =========================================================
# TAB 3 — CANDIDATES
# =========================================================

with tab_candidates:

    if not st.session_state.test_id:
        st.info(" Select a test from the sidebar.")
        st.stop()

    test_id = st.session_state.test_id
    st.markdown(f"### Candidate Profiles  —  `{test_id}`")

    candidates = get_candidates(test_id)
    stats = get_statistics(test_id)

    if not candidates:
        st.info(
            "No candidates found. "
            "Run analysis first via the Pipeline tab."
        )
        st.stop()

    # --- Per-candidate aggregate stats table ---
    if stats:
        st.markdown("#### Behavioral Summary")

        # Group stats by candidate.
        by_candidate = {}
        for row in stats:
            cid = row["candidate_id"]
            by_candidate.setdefault(cid, []).append(row)

        summary_rows = []
        for cid in sorted(by_candidate.keys()):
            rows = by_candidate[cid]
            total = sum(r["count"] for r in rows)
            suspicious = sum(r["suspicious_count"] or 0 for r in rows)
            duration = sum(r["total_duration"] or 0 for r in rows)
            summary_rows.append({
                "Candidate": cid,
                "Total Events": total,
                "Flagged": suspicious,
                "Total Duration (s)": round(duration, 1),
            })

        st.dataframe(
            summary_rows,
            use_container_width=True,
            hide_index=True
        )

        st.divider()

    # --- Individual candidate timeline ---
    selected_candidate = st.selectbox(
        "Select candidate",
        candidates,
        key="candidate_select"
    )

    if selected_candidate:

        timeline = get_candidate_timeline(test_id, selected_candidate)

        st.markdown(
            f"#### {selected_candidate} — "
            f"{len(timeline)} event(s)"
        )

        if not timeline:
            st.info("No behavioral events recorded for this candidate.")
        else:
            # Type breakdown
            type_counts = {}
            for e in timeline:
                t = e.get("event_type", "unknown")
                type_counts[t] = type_counts.get(t, 0) + 1

            badge_html_parts = []
            for t, c in sorted(type_counts.items(), key=lambda x: -x[1]):
                bg = EVENT_TYPE_COLORS.get(t, "#666")
                ic = EVENT_TYPE_ICONS.get(t, "")
                badge_html_parts.append(
                    f"<span class='event-badge' style='background:{bg}'>"
                    f"{ic} {t}: {c}"
                    f"</span>"
                )
            badge_html = " ".join(badge_html_parts)

            st.markdown(badge_html, unsafe_allow_html=True)
            st.markdown(" ")

            # Timeline events
            for event in timeline:

                event_type = event.get("event_type", "unknown")
                is_suspicious = bool(event.get("is_suspicious"))
                color = EVENT_TYPE_COLORS.get(event_type, "#666")
                icon = EVENT_TYPE_ICONS.get(event_type, "")
                flag = " ⚑" if is_suspicious else ""

                banner_class = (
                    "suspicious-banner"
                    if is_suspicious
                    else "common-banner"
                )

                with st.expander(
                    f"{icon} {event.get('start_time', '?')}  ·  "
                    f"{event_type}  "
                    f"({event.get('duration', 0):.0f}s)"
                    f"{flag}"
                ):

                    st.markdown(
                        f"<div class='{banner_class}'>"
                        f"{event.get('description', '')}"
                        f"</div>",
                        unsafe_allow_html=True
                    )

                    t_col1, t_col2, t_col3 = st.columns(3)
                    t_col1.metric("Start", event.get("start_time", "–"))
                    t_col2.metric("End", event.get("end_time", "–"))
                    t_col3.metric(
                        "Confidence",
                        f"{event.get('confidence', 0):.2f}"
                    )

                    st.caption(
                        f"Event ID: {event.get('event_id')}  ·  "
                        f"Cluster: {event.get('cluster_label', 'not clustered')}"
                    )


# =========================================================
# TAB 4 — PIPELINE
# =========================================================

with tab_pipeline:

    st.markdown("### Pipeline Control")
    st.markdown(
        "Run each stage of the analysis pipeline. "
        "Stages must be run in order for a new test."
    )
    st.divider()

    # --- Step 1: Ingest ---
    st.markdown(
        "<div class='step-card'>"
        "<span class='step-number'>① Ingest</span>  "
        "Discover images, validate, deduplicate, run YOLO detection"
        "</div>",
        unsafe_allow_html=True
    )

    with st.form("ingest_form"):
        ingest_col1, ingest_col2 = st.columns(2)
        with ingest_col1:
            new_test_id = st.text_input(
                "Test ID",
                placeholder="e.g. TEST_003",
                key="ingest_test_id"
            )
        with ingest_col2:
            source_dir = st.text_input(
                "Source directory",
                placeholder="e.g. data/raw/TEST_003",
                key="ingest_source_dir"
            )
        ingest_submitted = st.form_submit_button(
            " Run ingest",
            type="primary"
        )

    if ingest_submitted:
        if not new_test_id or not source_dir:
            st.error("Both Test ID and source directory are required.")
        else:
            with st.spinner("Ingesting images…"):
                try:
                    r = api_post(
                        "/tests/ingest",
                        {
                            "test_id": new_test_id,
                            "directory": source_dir
                        }
                    )
                    st.success(
                        f"✅ Ingested **{r.get('processed', 0)}** images  ·  "
                        f"{r.get('exact_duplicates', 0)} exact dupes  ·  "
                        f"{r.get('near_duplicates', 0)} near-dupes  ·  "
                        f"{r.get('detections', 0)} detections"
                    )
                    if r.get("errors"):
                        st.warning(
                            f"{len(r['errors'])} file(s) had errors. "
                            f"First: {r['errors'][0]}"
                        )
                    get_tests.clear()
                    get_test_summary.clear()
                except Exception as e:
                    st.error(f"Ingest failed: {e}")

    st.divider()

    # --- Step 2: Analyze ---
    st.markdown(
        "<div class='step-card'>"
        "<span class='step-number'>② Analyze</span>  "
        "Track persons, estimate pose, extract behavior features, "
        "detect events"
        "</div>",
        unsafe_allow_html=True
    )

    if st.session_state.test_id:

        if st.button(
            f" Analyze  `{st.session_state.test_id}`",
            key="analyze_btn"
        ):
            with st.spinner(
                "Running pose analysis and event detection… "
                "(this can take a few minutes)"
            ):
                try:
                    r = api_post(
                        f"/tests/{st.session_state.test_id}/analyze",
                        {}
                    )
                    st.success(
                        f"✅ Analyzed **{r.get('frames_analyzed', 0)}** frames  ·  "
                        f"{r.get('observations', 0)} observations  ·  "
                        f"{r.get('events', 0)} events generated"
                    )
                    get_events.clear()
                    get_test_summary.clear()
                except Exception as e:
                    st.error(f"Analysis failed: {e}")
    else:
        st.info("Select a test in the sidebar first.")

    st.divider()

    # --- Step 3: Index ---
    st.markdown(
        "<div class='step-card'>"
        "<span class='step-number'>③ Index</span>  "
        "Build sentence-transformer embeddings + FAISS vector store "
        "for semantic RAG retrieval"
        "</div>",
        unsafe_allow_html=True
    )

    if st.session_state.test_id:

        if st.button(
            f" Index  `{st.session_state.test_id}`",
            key="index_btn"
        ):
            with st.spinner("Building FAISS index…"):
                try:
                    r = api_post(
                        f"/tests/{st.session_state.test_id}/index",
                        {}
                    )
                    st.success(
                        f"✅ Indexed **{r.get('indexed', 0)}** events into FAISS."
                    )
                    get_health.clear()
                except Exception as e:
                    st.error(f"Indexing failed: {e}")

    st.divider()

    # --- Step 4: Cluster ---
    st.markdown(
        "<div class='step-card'>"
        "<span class='step-number'>④ Cluster</span>  "
        "Run DBSCAN/HDBSCAN on behavioral feature vectors to identify "
        "suspicious (rare) vs common (baseline) events"
        "</div>",
        unsafe_allow_html=True
    )

    if st.session_state.test_id:

        cluster_col1, cluster_col2 = st.columns([3, 1])

        with cluster_col1:
            algorithm = st.radio(
                "Algorithm",
                ["dbscan", "hdbscan"],
                horizontal=True,
                key="cluster_algo"
            )

        with cluster_col2:
            run_cluster = st.button(
                f" Cluster",
                key="cluster_btn_pipeline"
            )

        if run_cluster:
            with st.spinner("Clustering events…"):
                try:
                    r = api_post(
                        f"/tests/{st.session_state.test_id}/cluster"
                        f"?algorithm={algorithm}",
                        {}
                    )
                    st.success(
                        f"✅ Clustered **{r.get('events_clustered', 0)}** events  ·  "
                        f"{r.get('suspicious', 0)} suspicious  ·  "
                        f"{r.get('common', 0)} common"
                    )
                    get_events.clear()
                    get_statistics.clear()
                except Exception as e:
                    st.error(f"Clustering failed: {e}")

    st.divider()

    # --- System info ---
    st.markdown("#### System Information")

    health_data = get_health()

    if health_data:
        info_cols = st.columns(3)
        info_cols[0].metric("Vector store", health_data.get("vector_store_count", 0))
        info_cols[1].metric("LLM model", health_data.get("llm_model", "–"))
        info_cols[2].metric(
            "LLM reachable",
            "✅ Yes" if health_data.get("llm_reachable") else "❌ No"
        )
    else:
        st.warning("Could not reach API for health information.")