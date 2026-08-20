import json
import sys
import uuid
from pathlib import Path
from typing import Any, Dict

import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.audio.validator import validate_audio
from src.audio.preprocess import preprocess_audio
from src.audio.chunker import chunk_audio
from src.audio.analyzer import analyze_audio_chunk
from src.agent.graph import AudioReActGraph
from src.agent.ollama_reasoner import OllamaReasoner
from src.rag.store import AudioRAGStore

# ---------------- CONFIG ----------------
MAX_REACT_STEPS = 3
LOW_CONFIDENCE_THRESHOLD = 0.60
HIGH_CONFIDENCE_THRESHOLD = 0.80
OLLAMA_MODEL = "qwen3.5:9b"
OLLAMA_BASE_URL = "http://localhost:11434"
OLLAMA_TIMEOUT = 90
OLLAMA_MAX_RETRIES = 2
EMBEDDING_MODEL = "nomic-embed-text"
SEMANTIC_TOP_K = 5
CHUNK_SECONDS = 5.0
OVERLAP_SECONDS = 1.0

st.set_page_config(
    page_title="Audio Detection Agent | Local ReAct Agent",
    page_icon="🎧",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------- STATE ----------------
def init_state():
    defaults = {
        "page": "Dashboard",
        "final_state": None,
        "report_data": None,
        "report_path": None,
        "audio_file_id": None,
        "student_id": "",
        "historical_count": None,
        "uploaded_audio_path": None,
        "processed_audio_path": None,
        "chunk_paths": {},
        "chunks": [],
        "precomputed_analyses": {},
        "last_filename": None,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_state()

# ---------------- HELPERS ----------------
def safe_float(value: Any, default: float = 0.0) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def generate_audio_id() -> str:
    return f"audio_{uuid.uuid4().hex[:10]}"


def build_report(final_state, audio_file_id, source_file, student_id):
    results = final_state.get("report_results", [])
    label_summary = {}
    for r in results:
        label = str(r.get("assigned_label", "OTHER"))
        label_summary[label] = label_summary.get(label, 0) + 1
    return {
        "project": "Local Audio Detection ReAct Agent with Student-Scoped Semantic RAG",
        "student_id": student_id,
        "audio_file_id": audio_file_id,
        "source_file": str(source_file),
        "configuration": {
            "max_react_steps": MAX_REACT_STEPS,
            "low_confidence_threshold": LOW_CONFIDENCE_THRESHOLD,
            "high_confidence_threshold": HIGH_CONFIDENCE_THRESHOLD,
            "ollama_model": OLLAMA_MODEL,
            "embedding_model": EMBEDDING_MODEL,
            "chunk_seconds": CHUNK_SECONDS,
            "overlap_seconds": OVERLAP_SECONDS,
            "semantic_top_k": SEMANTIC_TOP_K,
        },
        "chunks_processed": len(results),
        "review_required": sum(bool(r.get("review_required")) for r in results),
        "chunks_with_semantic_context": sum(bool(r.get("context_used")) for r in results),
        "chunks_reanalyzed": sum(bool(r.get("reanalyzed")) for r in results),
        "label_summary": label_summary,
        "results": results,
    }


def save_report(report, audio_file_id):
    directory = PROJECT_ROOT / "data" / "audio_reports"
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / f"{audio_file_id}_report.json"
    path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    return path


def confidence_pct(v):
    return max(0, min(100, safe_float(v) * 100))


def badge(label, tone="blue"):
    return f'<span class="badge {tone}">{label}</span>'


def label_tone(label):
    s = str(label).upper()
    if "REVIEW" in s:
        return "amber"
    if "SPEECH" in s:
        return "violet"
    if "NOISE" in s:
        return "cyan"
    return "blue"


def render_metric(label, value, caption="", tone=""):
    st.markdown(
        f'''<div class="metric-card {tone}">
        <div class="metric-label">{label}</div>
        <div class="metric-value">{value}</div>
        <div class="metric-caption">{caption}</div>
        </div>''',
        unsafe_allow_html=True,
    )


def render_pipeline(active=None):
    steps = [
        ("01", "Upload", "Input"),
        ("02", "Validate", "Quality"),
        ("03", "Preprocess", "Normalize"),
        ("04", "Chunk", "Temporal"),
        ("05", "Analyze", "Acoustic"),
        ("06", "RAG", "Memory"),
        ("07", "ReAct", "Reasoning"),
        ("08", "Report", "Output"),
    ]
    html = '<div class="pipeline">'
    for num, title, sub in steps:
        cls = "active" if active == title else ""
        html += f'''<div class="pipe-step {cls}">
            <div class="pipe-num">{num}</div><div><b>{title}</b><small>{sub}</small></div>
        </div>'''
    html += '</div>'
    st.markdown(html, unsafe_allow_html=True)


def render_audio_timeline(chunks, results=None):
    if not chunks:
        return
    results_by_id = {str(r.get("chunk_id")): r for r in (results or [])}
    max_end = max(safe_float(c.get("end_timestamp")) for c in chunks) or 1
    st.markdown('<div class="timeline-wrap">', unsafe_allow_html=True)
    cols = st.columns(len(chunks))
    for i, chunk in enumerate(chunks):
        cid = str(chunk.get("chunk_id", i))
        result = results_by_id.get(cid, {})
        label = result.get("assigned_label", "Pending")
        conf = confidence_pct(result.get("confidence_score", 0))
        start = safe_float(chunk.get("start_timestamp"))
        end = safe_float(chunk.get("end_timestamp"))
        with cols[i]:
            st.markdown(
                f'''<div class="chunk-tile"><div class="chunk-index">CHUNK {i:02d}</div>
                <div class="chunk-label">{label}</div><div class="chunk-time">{start:.1f}s — {end:.1f}s</div>
                <div class="mini-bar"><span style="width:{conf:.0f}%"></span></div>
                <small>{conf:.0f}% confidence</small></div>''',
                unsafe_allow_html=True,
            )
            path = chunk.get("storage_path")
            if path and Path(path).exists():
                st.audio(str(path), format="audio/wav")
    st.markdown('</div>', unsafe_allow_html=True)


def render_chunk_card(result, index):
    cid = result.get("chunk_id", f"chunk_{index:02d}")
    label = result.get("assigned_label", "OTHER")
    conf = safe_float(result.get("confidence_score"))
    review = bool(result.get("review_required"))
    tone = label_tone(label)
    status = badge("REVIEW REQUIRED", "amber") if review else badge("AUTO-COMPLETE", "green")
    st.markdown(
        f'''<div class="result-card">
        <div class="result-top"><div><span class="eyebrow">CHUNK {index+1:02d}</span>
        <h3>{label}</h3></div><div>{status}</div></div>
        <div class="result-meta"><span>{result.get("start_timestamp", 0):.1f}s → {result.get("end_timestamp", 0):.1f}s</span>
        <span>{badge(f"{conf*100:.0f}% confidence", tone)}</span></div>
        <div class="confidence"><div class="confidence-track"><span style="width:{confidence_pct(conf):.0f}%"></span></div></div>
        </div>''', unsafe_allow_html=True)
    a, b, c = st.columns(3)
    with a:
        if result.get("chunk_path") and Path(result["chunk_path"]).exists():
            st.audio(result["chunk_path"], format="audio/wav")
        else:
            path = st.session_state.get("chunk_paths", {}).get(str(cid))
            if path and Path(path).exists():
                st.audio(path, format="audio/wav")
    with b:
        st.metric("Semantic context", "Used" if result.get("context_used") else "Not used")
    with c:
        st.metric("ReAct steps", result.get("react_steps", 0))
    tabs = st.tabs(["🧠 Why this decision", "🔎 Evidence", "🔬 Technical"])
    with tabs[0]:
        reasoning = result.get("reasoning") or "No reasoning text returned."
        st.info(reasoning)
        actions = result.get("action_history") or []
        if actions:
            st.caption("Agent path")
            st.code("  →  ".join(map(str, actions)))
    with tabs[1]:
        context = result.get("context_observations", result.get("retrieved_context", [])) or []
        if context:
            rows = []
            for item in context:
                rows.append({
                    "Event": item.get("event", "OTHER"),
                    "Similarity": round(safe_float(item.get("similarity")), 3),
                    "Confidence": round(safe_float(item.get("confidence")), 3),
                    "Chunk": item.get("chunk_id", ""),
                })
            st.dataframe(rows, use_container_width=True, hide_index=True)
        else:
            st.caption("No historical semantic context was used for this chunk.")
    with tabs[2]:
        left, right = st.columns(2)
        with left:
            st.write("**Detected event**", result.get("detected_event", "OTHER"))
            st.write("**Final event**", result.get("final_event", "OTHER"))
            st.write("**Confidence**", f"{conf:.3f}")
        with right:
            st.write("**Context used**", bool(result.get("context_used")))
            st.write("**Re-analyzed**", bool(result.get("reanalyzed")))
            st.write("**Review**", review)
        if result.get("reanalyzed"):
            st.json(result.get("reanalysis_comparison", {}))
        with st.expander("Raw result"):
            st.json(result)

# ---------------- CSS ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');
:root{--ink:#172033;--muted:#687386;--line:#e8ebf2;--bg:#f7f8fc;--card:#fff;--primary:#5b5ce2;--cyan:#18a8c7;--green:#179b67;--amber:#d99016;--violet:#805ad5}
.stApp{background:var(--bg);font-family:'DM Sans',sans-serif;color:var(--ink)}
.block-container{padding:1.6rem 2.4rem 3rem;max-width:1500px}
h1,h2,h3{font-family:'Space Grotesk',sans-serif;color:var(--ink)!important}
[data-testid="stSidebar"]{background:#101528;border-right:1px solid #1e2740}
[data-testid="stSidebar"] *{color:#e9edf7!important}
[data-testid="stSidebar"] .stRadio label{padding:8px 10px;border-radius:10px}
.hero{background:linear-gradient(135deg,#11182c 0%,#24295a 55%,#5054c9 100%);border-radius:24px;padding:30px 34px;color:white;margin-bottom:20px;box-shadow:0 18px 50px rgba(24,32,68,.16)}
.hero h1{color:white!important;font-size:2.35rem;margin:0 0 5px}.hero p{color:#cfd5e9;margin:0;font-size:1rem}.hero-right{text-align:right;color:#d9dded;font-size:.9rem}
.eyebrow{font-size:.72rem;font-weight:700;letter-spacing:.12em;color:#818ba1}.section-head{display:flex;align-items:end;justify-content:space-between;margin:26px 0 12px}.section-head h2{font-size:1.25rem;margin:0}.section-head p{margin:0;color:var(--muted);font-size:.85rem}
.metric-card{background:white;border:1px solid var(--line);border-radius:17px;padding:18px 19px;min-height:112px;box-shadow:0 5px 18px rgba(30,40,70,.035)}.metric-label{font-size:.78rem;color:var(--muted);font-weight:600}.metric-value{font-family:'Space Grotesk';font-size:1.75rem;font-weight:700;margin-top:8px}.metric-caption{font-size:.75rem;color:#9099a9;margin-top:4px}
.pipeline{display:grid;grid-template-columns:repeat(8,1fr);gap:8px;background:#fff;border:1px solid var(--line);padding:10px;border-radius:17px}.pipe-step{display:flex;align-items:center;gap:9px;padding:10px;border-radius:12px;color:#697387}.pipe-step.active{background:#f0efff;color:#3e40aa}.pipe-num{font-size:.7rem;font-weight:700;color:#9aa2b2}.pipe-step b{font-size:.78rem;display:block}.pipe-step small{font-size:.66rem;color:#9aa2b2}
.upload-card{background:white;border:1px dashed #b8bfd0;border-radius:18px;padding:20px}.result-card,.evidence-card,.system-card{background:white;border:1px solid var(--line);border-radius:18px;padding:20px;margin-bottom:12px;box-shadow:0 5px 18px rgba(30,40,70,.035)}
.result-top{display:flex;justify-content:space-between;align-items:start}.result-card h3{margin:4px 0;font-size:1.25rem}.result-meta{display:flex;justify-content:space-between;align-items:center;color:var(--muted);font-size:.82rem;margin-top:12px}.confidence{margin-top:14px}.confidence-track,.mini-bar{height:7px;background:#edf0f6;border-radius:99px;overflow:hidden}.confidence-track span,.mini-bar span{display:block;height:100%;background:linear-gradient(90deg,#5b5ce2,#22b6ce);border-radius:99px}.chunk-tile{border:1px solid var(--line);background:#fff;border-radius:15px;padding:13px;margin-bottom:8px}.chunk-index{font-size:.65rem;font-weight:700;color:#919aaa;letter-spacing:.1em}.chunk-label{font-weight:700;margin-top:5px;font-size:.9rem}.chunk-time{font-size:.75rem;color:var(--muted);margin:3px 0 9px}.chunk-tile small{font-size:.68rem;color:#8b94a5}
.badge{display:inline-block;border-radius:99px;padding:5px 9px;font-size:.68rem;font-weight:700}.badge.green{background:#e8f8f1;color:#087b50}.badge.amber{background:#fff4df;color:#9a6200}.badge.blue{background:#eceeff;color:#4749b7}.badge.cyan{background:#e6f8fc;color:#087e99}.badge.violet{background:#f1eaff;color:#7040b7}
.callout{background:#f5f6ff;border:1px solid #dfe1ff;border-radius:15px;padding:16px}.success-callout{background:#edfaf5;border-color:#ccefe0}.warning-callout{background:#fff7e8;border-color:#f4dfb6}.code-panel{background:#121728;border-radius:16px;padding:16px;color:#dbe2f1;font-family:monospace}.divider{height:1px;background:var(--line);margin:22px 0}
.stButton>button{border-radius:11px!important;font-weight:600!important}.stDownloadButton>button{border-radius:11px!important}
@media(max-width:1100px){.pipeline{grid-template-columns:repeat(4,1fr)}}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.markdown("<div style='font-family:Space Grotesk;font-size:1.2rem;font-weight:700'>🎧 Audio Detection Agent</div>", unsafe_allow_html=True)
    st.caption("Local detection • RAG • ReAct")
    st.divider()
    options = ["Dashboard", "Analyze Audio", "Results", "Agent Reasoning", "Evidence", "Student Memory", "System"]
    current = st.session_state.page if st.session_state.page in options else "Dashboard"
    page = st.radio("WORKSPACE", options, index=options.index(current), label_visibility="visible")
    st.session_state.page = page
    st.divider()
    st.markdown("**LOCAL STACK**")
    st.caption("● Ollama  ·  qwen3.5:9b")
    st.caption("● ChromaDB  ·  semantic memory")
    st.caption("● LangGraph  ·  ReAct orchestration")
    st.caption("● Librosa  ·  acoustic analysis")
    st.divider()
    st.caption("🔒 Audio and reasoning are designed to stay local.")

# ---------------- HEADER ----------------
st.markdown(f'''<div class="hero"><div style="display:flex;justify-content:space-between;gap:30px"><div>
<div class="eyebrow" style="color:#aeb6d4">LOCAL AI WORKSPACE</div>
<h1>Audio Detection Agent</h1><p>Inspectable audio detection powered by acoustic evidence, student-scoped semantic memory and a bounded ReAct agent.</p>
</div><div class="hero-right">● SYSTEM READY<br><span style="opacity:.65">Ollama · ChromaDB · LangGraph</span></div></div></div>''', unsafe_allow_html=True)

# ---------------- DASHBOARD ----------------
if page == "Dashboard":
    st.markdown('<div class="section-head"><div><h2>Workspace overview</h2><p>Run an analysis and inspect every decision.</p></div></div>', unsafe_allow_html=True)
    results = (st.session_state.report_data or {}).get("results", [])
    total = len(results)
    review = sum(bool(r.get("review_required")) for r in results)
    context = sum(bool(r.get("context_used")) for r in results)
    reanalyzed = sum(bool(r.get("reanalyzed")) for r in results)
    avg = sum(safe_float(r.get("confidence_score")) for r in results)/total if total else 0
    m = st.columns(5)
    with m[0]: render_metric("Chunks processed", total, "Latest run")
    with m[1]: render_metric("Avg confidence", f"{avg*100:.0f}%", "Across final decisions")
    with m[2]: render_metric("RAG retrievals", context, "Historical context used")
    with m[3]: render_metric("Re-analysis", reanalyzed, "Second-pass checks")
    with m[4]: render_metric("Review queue", review, "Needs human attention", "warning" if review else "")
    st.markdown('<div class="section-head"><div><h2>Pipeline</h2><p>Eight controlled stages from audio input to report.</p></div></div>', unsafe_allow_html=True)
    render_pipeline()
    c1,c2 = st.columns([1.35,1])
    with c1:
        st.markdown('<div class="evidence-card"><div class="eyebrow">WHY THIS PROJECT FEELS DIFFERENT</div><h3>Every decision stays inspectable.</h3><p style="color:#687386">The analyzer produces acoustic observations. Nomic embeddings and ChromaDB provide student-scoped context. LangGraph controls the allowed actions and Qwen reasons over the evidence.</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="evidence-card"><div class="eyebrow">FAST START</div><h3>Ready to analyze audio?</h3><p style="color:#687386">Upload a recording, select a student and run the local pipeline.</p></div>', unsafe_allow_html=True)
        if st.button("🎵 Open Audio Workspace", type="primary", use_container_width=True):
            st.session_state.page = "Analyze Audio"
            st.rerun()
    if results:
        st.markdown('<div class="section-head"><div><h2>Latest decision snapshot</h2></div></div>', unsafe_allow_html=True)
        render_audio_timeline(st.session_state.chunks, results)

# ---------------- ANALYZE ----------------
elif page == "Analyze Audio":
    st.markdown('<div class="section-head"><div><h2>Analyze audio</h2><p>Run the complete local pipeline without leaving this workspace.</p></div></div>', unsafe_allow_html=True)
    render_pipeline("Upload")
    left, right = st.columns([1.35, .65], gap="large")
    with left:
        st.markdown('<div class="upload-card">', unsafe_allow_html=True)
        student_id = st.text_input("Student ID", value=st.session_state.student_id or "", placeholder="e.g. Student01")
        uploaded_file = st.file_uploader("Drop an audio file here", type=["wav"], label_visibility="visible")
        if uploaded_file:
            st.audio(uploaded_file)
            st.success(f"Ready · {uploaded_file.name}")
        st.markdown('</div>', unsafe_allow_html=True)
    with right:
        st.markdown('<div class="system-card"><div class="eyebrow">ANALYSIS PROFILE</div><h3>Local / Explainable</h3><p>5s chunks · 1s overlap</p><p>Top-K retrieval · {}</p><p>Confidence thresholds · 60 / 80%</p><p>Reasoning model · {}</p></div>'.format(SEMANTIC_TOP_K, OLLAMA_MODEL), unsafe_allow_html=True)
    run = st.button("▶  Run Local Audio Agent", type="primary", use_container_width=True, disabled=uploaded_file is None or not str(student_id).strip())
    if run:
        student_id = str(student_id).strip()
        audio_file_id = generate_audio_id()
        st.session_state.update({"audio_file_id": audio_file_id, "student_id": student_id, "last_filename": uploaded_file.name})
        upload_dir = PROJECT_ROOT / "data" / "streamlit_uploads"; upload_dir.mkdir(parents=True, exist_ok=True)
        safe_name = Path(uploaded_file.name).name
        original = upload_dir / f"{audio_file_id}_{safe_name}"
        original.write_bytes(uploaded_file.getbuffer())
        st.session_state.uploaded_audio_path = str(original)
        progress = st.progress(0)
        status = st.empty()
        try:
            status.info("01 / 08 · Validating audio")
            validation = validate_audio(str(original)); duration = safe_float(validation.get("duration")); progress.progress(10)
            status.info("02 / 08 · Preprocessing to mono / 16 kHz")
            proc_dir = PROJECT_ROOT / "data" / "processed_audio"; proc_dir.mkdir(parents=True, exist_ok=True)
            processed = proc_dir / f"{audio_file_id}.wav"; preprocess_audio(input_path=str(original), output_path=str(processed)); st.session_state.processed_audio_path = str(processed); progress.progress(20)
            status.info("03 / 08 · Building overlapping chunks")
            chunk_dir = PROJECT_ROOT / "data" / "audio_chunks" / audio_file_id; chunk_dir.mkdir(parents=True, exist_ok=True)
            chunks = chunk_audio(wav_path=str(processed), output_dir=str(chunk_dir), chunk_seconds=CHUNK_SECONDS, overlap_seconds=OVERLAP_SECONDS)
            if not chunks: raise RuntimeError("No audio chunks were created.")
            st.session_state.chunks = chunks
            st.session_state.chunk_paths = {str(c.get("chunk_id")): c.get("storage_path") for c in chunks}
            progress.progress(30)
            status.info("04 / 08 · Extracting acoustic evidence")
            analyses = {}
            for c in chunks: analyses[str(c["chunk_id"])] = analyze_audio_chunk(c["storage_path"])
            st.session_state.precomputed_analyses = analyses; progress.progress(45)
            status.info("05 / 08 · Connecting student-scoped semantic memory")
            rag = AudioRAGStore(ollama_base_url=OLLAMA_BASE_URL, embedding_model=EMBEDDING_MODEL)
            try: historical = rag.count_student_observations(student_id)
            except Exception: historical = None
            st.session_state.historical_count = historical; progress.progress(58)
            status.info("06 / 08 · Starting LangGraph ReAct controller")
            reasoner = OllamaReasoner(model=OLLAMA_MODEL, base_url=OLLAMA_BASE_URL, timeout=OLLAMA_TIMEOUT, max_retries=OLLAMA_MAX_RETRIES)
            agent = AudioReActGraph(rag_store=rag, reasoner=reasoner, low_confidence_threshold=LOW_CONFIDENCE_THRESHOLD, high_confidence_threshold=HIGH_CONFIDENCE_THRESHOLD, max_react_steps=MAX_REACT_STEPS, semantic_top_k=SEMANTIC_TOP_K)
            progress.progress(70)
            status.info("07 / 08 · Reasoning over evidence")
            final_state = agent.run(audio_file_id=audio_file_id, source_file=str(original), chunks=chunks, student_id=student_id, precomputed_analyses=analyses)
            progress.progress(92)
            status.info("08 / 08 · Writing structured report")
            report = build_report(final_state, audio_file_id, original, student_id); report_path = save_report(report, audio_file_id)
            st.session_state.final_state = final_state; st.session_state.report_data = report; st.session_state.report_path = report_path
            progress.progress(100); status.success(f"Analysis complete · {duration:.1f}s audio · {len(chunks)} chunks")
            st.session_state.page = "Results"
            st.rerun()
        except Exception as exc:
            status.error("Pipeline stopped. Check the error below.")
            st.exception(exc)
    if st.session_state.chunks:
        st.markdown('<div class="section-head"><div><h2>Audio timeline</h2><p>Each chunk is independently inspectable.</p></div></div>', unsafe_allow_html=True)
        render_audio_timeline(st.session_state.chunks, (st.session_state.report_data or {}).get("results", []))

# ---------------- RESULTS ----------------
elif page == "Results":
    report = st.session_state.report_data or {}
    results = report.get("results", [])
    if not results:
        st.info("No analysis results yet. Open Analyze Audio to run the pipeline.")
    else:
        review = sum(bool(r.get("review_required")) for r in results)
        context = sum(bool(r.get("context_used")) for r in results)
        reanalyzed = sum(bool(r.get("reanalyzed")) for r in results)
        avg = sum(safe_float(r.get("confidence_score")) for r in results)/len(results)
        st.markdown(f'<div class="section-head"><div><h2>Analysis results</h2><p>{st.session_state.last_filename or "Audio file"} · {st.session_state.student_id}</p></div><div>{badge("REVIEW QUEUE: "+str(review), "amber" if review else "green")}</div></div>', unsafe_allow_html=True)
        m = st.columns(5)
        vals = [("Chunks",len(results)),("Avg confidence",f"{avg*100:.0f}%"),("RAG used",context),("Re-analyzed",reanalyzed),("Review",review)]
        for col,(lab,val) in zip(m,vals):
            with col: render_metric(lab,val)
        st.markdown('<div class="section-head"><div><h2>Decision timeline</h2><p>Listen to each segment and inspect the final decision.</p></div></div>', unsafe_allow_html=True)
        render_audio_timeline(st.session_state.chunks, results)
        st.markdown('<div class="section-head"><div><h2>Chunk decisions</h2><p>Click into any result to see reasoning and evidence.</p></div></div>', unsafe_allow_html=True)
        for i,r in enumerate(results): render_chunk_card(r,i)
        report_json = json.dumps(report, indent=2, ensure_ascii=False)
        st.download_button("⬇ Download JSON report", report_json, f"{st.session_state.audio_file_id}_report.json", "application/json")

# ---------------- AGENT ----------------
elif page == "Agent Reasoning":
    results = (st.session_state.report_data or {}).get("results", [])
    st.markdown('<div class="section-head"><div><h2>Agent reasoning</h2><p>Inspectable LangGraph / ReAct execution path.</p></div></div>', unsafe_allow_html=True)
    if not results:
        st.info("Run an analysis first.")
    else:
        for i,r in enumerate(results):
            actions = r.get("action_history") or []
            st.markdown(f'''<div class="evidence-card"><div class="eyebrow">CHUNK {i+1:02d}</div><h3>{r.get("assigned_label","OTHER")}</h3><p style="color:#687386">Confidence {safe_float(r.get("confidence_score"))*100:.0f}% · {len(actions)} recorded actions</p></div>''', unsafe_allow_html=True)
            if actions:
                st.code("\n↓\n".join(map(str, actions)))
            else:
                st.caption("No explicit action history returned.")
            if r.get("reasoning"):
                st.info(r["reasoning"])

# ---------------- EVIDENCE ----------------
elif page == "Evidence":
    results = (st.session_state.report_data or {}).get("results", [])

    st.markdown(
        '<div class="section-head">'
        '<div><h2>Evidence explorer</h2>'
        '<p>Student-scoped semantic context retrieved for each decision.</p>'
        '</div></div>',
        unsafe_allow_html=True,
    )

    if not results:
        st.info("Run an analysis first.")
    else:
        for i, r in enumerate(results):
            label = r.get("assigned_label", "OTHER")
            confidence = confidence_pct(r.get("confidence_score", 0))
            review = bool(r.get("review_required"))
            status = (
                badge("REVIEW REQUIRED", "amber")
                if review
                else badge("AUTO-COMPLETE", "green")
            )

            st.markdown(
                f"""
                <div class="evidence-card">
                    <div class="result-top">
                        <div>
                            <div class="eyebrow">SEMANTIC EVIDENCE · CHUNK {i+1:02d}</div>
                            <h3>{label}</h3>
                            <div style="color:#687386;font-size:.82rem;margin-top:5px">
                                {safe_float(r.get("start_timestamp")):.1f}s
                                → {safe_float(r.get("end_timestamp")):.1f}s
                                &nbsp;·&nbsp; {confidence:.0f}% confidence
                            </div>
                        </div>
                        <div>{status}</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            context = r.get(
                "context_observations",
                r.get("retrieved_context", [])
            ) or []

            if context:
                rows = []
                for rank, item in enumerate(context, start=1):
                    rows.append(
                        {
                            "Rank": rank,
                            "Event": item.get("event", "OTHER"),
                            "Similarity": round(
                                safe_float(item.get("similarity")), 3
                            ),
                            "Confidence": round(
                                safe_float(item.get("confidence")), 3
                            ),
                            "Chunk": item.get("chunk_id", ""),
                        }
                    )

                st.dataframe(
                    rows,
                    use_container_width=True,
                    hide_index=True,
                    column_config={
                        "Rank": st.column_config.NumberColumn(
                            "Rank", width="small"
                        ),
                        "Event": st.column_config.TextColumn(
                            "Event", width="large"
                        ),
                        "Similarity": st.column_config.NumberColumn(
                            "Similarity", format="%.3f"
                        ),
                        "Confidence": st.column_config.NumberColumn(
                            "Confidence", format="%.3f"
                        ),
                        "Chunk": st.column_config.TextColumn(
                            "Source chunk", width="medium"
                        ),
                    },
                )

                top_similarity = max(
                    (
                        safe_float(item.get("similarity"))
                        for item in context
                    ),
                    default=0.0,
                )

                st.caption(
                    f"Top semantic similarity: {top_similarity:.3f} · "
                    f"{len(context)} student-scoped observation(s) retrieved."
                )

                with st.expander(
                    "View retrieved historical observations"
                ):
                    for rank, item in enumerate(context, start=1):
                        event = item.get("event", "OTHER")
                        similarity = safe_float(item.get("similarity"))
                        item_conf = safe_float(item.get("confidence"))

                        st.markdown(
                            f"**#{rank} · {event}**  \n"
                            f"Similarity: `{similarity:.3f}` · "
                            f"Confidence: `{item_conf:.3f}`"
                        )

                        if item.get("chunk_id"):
                            st.caption(
                                f"Historical chunk: {item.get('chunk_id')}"
                            )

                        if item.get("reason"):
                            st.caption(item.get("reason"))

                        if rank < len(context):
                            st.divider()
            else:
                st.markdown(
                    '<div class="callout">'
                    '<b>No semantic context used</b><br>'
                    '<span style="color:#687386">'
                    'This decision did not retrieve a matching '
                    'student-scoped historical observation.'
                    '</span></div>',
                    unsafe_allow_html=True,
                )


# ---------------- STUDENT ----------------
elif page == "Student Memory":
    st.markdown('<div class="section-head"><div><h2>Student memory</h2><p>Controlled semantic memory for the selected student.</p></div></div>', unsafe_allow_html=True)
    sid = st.text_input("Student ID", value=st.session_state.student_id or "Student01")
    if st.session_state.historical_count is not None:
        m=st.columns(3)
        with m[0]: render_metric("Student",sid,"Active scope")
        with m[1]: render_metric("Historical observations",st.session_state.historical_count,"Available in ChromaDB")
        with m[2]: render_metric("Top-K",SEMANTIC_TOP_K,"Retrieval limit")
    st.markdown('<div class="callout"><b>How student-scoped RAG works</b><br><span style="color:#687386">Semantic similarity finds related observations while metadata filtering keeps retrieval restricted to the relevant student.</span></div>', unsafe_allow_html=True)

# ---------------- SYSTEM ----------------
elif page == "System":
    st.markdown('<div class="section-head"><div><h2>System configuration</h2><p>Runtime profile used by the local agent.</p></div></div>', unsafe_allow_html=True)
    cols=st.columns(2)
    with cols[0]:
        st.markdown('<div class="system-card"><div class="eyebrow">REASONING</div><h3>Qwen via Ollama</h3><p><b>Model:</b> {}</p><p><b>Endpoint:</b> {}</p><p><b>Timeout:</b> {}s</p><p><b>Max ReAct steps:</b> {}</p></div>'.format(OLLAMA_MODEL,OLLAMA_BASE_URL,OLLAMA_TIMEOUT,MAX_REACT_STEPS),unsafe_allow_html=True)
        st.markdown('<div class="system-card"><div class="eyebrow">SEMANTIC MEMORY</div><h3>ChromaDB + Nomic</h3><p><b>Embedding:</b> {}</p><p><b>Top-K:</b> {}</p><p><b>Scope:</b> Student-specific</p></div>'.format(EMBEDDING_MODEL,SEMANTIC_TOP_K),unsafe_allow_html=True)
    with cols[1]:
        st.markdown('<div class="system-card"><div class="eyebrow">AUDIO</div><h3>Signal processing</h3><p><b>Chunk:</b> {} sec</p><p><b>Overlap:</b> {} sec</p><p><b>Preprocess:</b> Mono / 16 kHz WAV</p><p><b>Analysis:</b> RMS · ZCR · spectral features · MFCC</p></div>'.format(CHUNK_SECONDS,OVERLAP_SECONDS),unsafe_allow_html=True)
        st.markdown('<div class="system-card"><div class="eyebrow">DECISION POLICY</div><h3>Review stays in the loop</h3><p>Low confidence: &lt; {:.0f}%</p><p>High confidence: ≥ {:.0f}%</p><p>Uncertain or failed reasoning can fall back to manual review.</p></div>'.format(LOW_CONFIDENCE_THRESHOLD*100,HIGH_CONFIDENCE_THRESHOLD*100),unsafe_allow_html=True)
