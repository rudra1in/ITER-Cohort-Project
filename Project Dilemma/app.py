from pathlib import Path

import streamlit as st

from src.graph import workflow


# ============================================================
# Paths
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"
ID_DIR = DATA_DIR / "ids"
VIDEO_DIR = DATA_DIR / "videos"

ID_DIR.mkdir(parents=True, exist_ok=True)
VIDEO_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================
# Page
# ============================================================

st.set_page_config(
    page_title="Offline Identity Verification",
    page_icon="🔐",
    layout="centered",
)

st.title("🔐 Offline Identity Verification")
st.caption(
    "Agentic AI powered identity verification"
)

st.divider()


# ============================================================
# STEP 1 — ID
# ============================================================

st.header("1. Identity Document")

id_file = st.file_uploader(
    "Upload your ID image",
    type=["jpg", "jpeg", "png"],
    key="id_upload",
)

id_path = None

if id_file:

    id_path = ID_DIR / "current_id.jpg"

    with open(id_path, "wb") as file:
        file.write(
            id_file.getbuffer()
        )

    st.success("Identity document uploaded.")

    st.image(
        id_file,
        caption="Identity Document",
        width=400,
    )


st.divider()


# ============================================================
# STEP 2 — VIDEO
# ============================================================

st.header("2. Verification Video")

video_file = st.file_uploader(
    "Upload your verification video",
    type=[
        "mp4",
        "webm",
        "mov",
        "avi",
    ],
    key="video_upload",
)

video_path = None

if video_file:

    video_path = (
        VIDEO_DIR
        / "verification_video.mp4"
    )

    with open(video_path, "wb") as file:
        file.write(
            video_file.getbuffer()
        )

    st.success(
        "Verification video uploaded."
    )

    st.video(
        str(video_path)
    )


st.divider()


# ============================================================
# STEP 3 — VERIFY
# ============================================================

st.header("3. Verify Identity")

st.write(
    "The LangGraph workflow will analyze the "
    "identity document, process the video, "
    "generate face embeddings, compare the "
    "identity, and record the result."
)


if st.button(
    "🔍 Verify Identity",
    type="primary",
    use_container_width=True,
):

    if id_path is None:

        st.error(
            "Please upload an ID image first."
        )

    elif video_path is None:

        st.error(
            "Please upload a verification video first."
        )

    else:

        with st.spinner(
            "Running Agentic AI verification..."
        ):

            try:

                result = workflow.invoke(
                    {
                        "id_image_path":
                            str(id_path),

                        "video_path":
                            str(video_path),

                        "errors": [],
                    }
                )

            except Exception as exc:

                st.error(
                    f"Verification failed: {exc}"
                )

                st.stop()


        # ====================================================
        # RESULTS
        # ====================================================

        st.divider()

        st.header(
            "Verification Result"
        )


        errors = result.get(
            "errors",
            []
        )

        if errors:

            st.warning(
                "Some processing warnings occurred:"
            )

            for error in errors:
                st.write(
                    f"• {error}"
                )


        verification_result = (
            result.get(
                "verification_result"
            )
        )

        similarity = result.get(
            "face_similarity"
        )


        if (
            verification_result
            == "VERIFIED"
        ):

            st.success(
                "✅ IDENTITY VERIFIED"
            )

        else:

            st.error(
                "❌ IDENTITY NOT VERIFIED"
            )


        # ====================================================
        # METRICS
        # ====================================================

        col1, col2, col3 = st.columns(3)


        with col1:

            if similarity is not None:

                st.metric(
                    "Face Similarity",
                    f"{similarity:.4f}",
                )

            else:

                st.metric(
                    "Face Similarity",
                    "N/A",
                )


        with col2:

            st.metric(
                "Video Frames",
                len(
                    result.get(
                        "frame_paths",
                        []
                    )
                ),
            )


        with col3:

            st.metric(
                "Face Samples",
                len(
                    result.get(
                        "video_face_embeddings",
                        []
                    )
                ),
            )


        # ====================================================
        # ID INFORMATION
        # ====================================================

        identity_data = result.get(
            "identity_data"
        )

        if identity_data:

            st.subheader(
                "Identity Information"
            )

            st.json(
                identity_data
            )


        # ====================================================
        # VERIFICATION DETAILS
        # ====================================================

        reason = result.get(
            "verification_reason"
        )

        if reason:

            st.subheader(
                "Verification Details"
            )

            st.info(reason)


        # ====================================================
        # LEDGER
        # ====================================================

        ledger_entry = result.get(
            "ledger_entry"
        )

        if ledger_entry:

            st.subheader(
                "Verification Ledger"
            )

            st.json(
                ledger_entry
            )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Offline Proctoring • "
    "LangGraph + Vision Agents + "
    "InsightFace + ChromaDB"
)