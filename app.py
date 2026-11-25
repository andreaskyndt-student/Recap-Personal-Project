import streamlit as st
from pathlib import Path
from datetime import datetime
from models.transcription import transcribe_audio
from models.summarization import summarize_text
from utils.document_export import create_word_document, create_pdf_document

st.set_page_config(
    page_title="Recap | Audio into summaries",
    page_icon="🎙️",
    layout="wide",
)

st.markdown(
    """
    <style>
    :root {
        --recap-green: #c7f9cc;
        --recap-deep: #2d6a4f;
        --recap-ink: #18352b;
        --recap-muted: #648075;
        --recap-paper: #f6fbf6;
    }
    .stApp { background: var(--recap-paper); color: var(--recap-ink); }
    [data-testid="stHeader"] { background: transparent; }
    .block-container { max-width: 1100px; padding-top: 2.2rem; padding-bottom: 4rem; }
    .recap-brand { display: flex; align-items: center; gap: .8rem; margin-bottom: .4rem; }
    .recap-mark {
        width: 48px; height: 48px; display: grid; place-items: center;
        border-radius: 16px; background: var(--recap-green); font-size: 1.5rem;
    }
    .recap-brand h1 { margin: 0; color: var(--recap-ink); font-size: 2rem; letter-spacing: -.04em; }
    .recap-intro { color: var(--recap-muted); font-size: 1.05rem; margin: .25rem 0 1.5rem; }
    .recap-section-title { color: var(--recap-ink); font-size: 1.25rem; font-weight: 700; margin: 0 0 .25rem; }
    .recap-section-copy { color: var(--recap-muted); margin-bottom: 1rem; }
    [data-testid="stVerticalBlockBorderWrapper"] {
        background: #fff; border: 1px solid #dfede2; border-radius: 20px;
        box-shadow: 0 8px 28px rgba(24, 53, 43, .045); padding: .35rem;
    }
    div.stButton > button, div.stDownloadButton > button {
        border-radius: 12px; min-height: 2.8rem; font-weight: 650;
        border: 1px solid var(--recap-deep); color: white; background: var(--recap-deep);
        transition: transform .15s ease, background .15s ease, box-shadow .15s ease;
    }
    div.stButton > button:hover, div.stDownloadButton > button:hover {
        background: #1f513b; border-color: #1f513b; color: white;
        transform: translateY(-1px); box-shadow: 0 5px 14px rgba(45, 106, 79, .2);
    }
    div[data-testid="stAudioInput"] { border-radius: 14px; }
    [data-testid="stTextArea"] textarea {
        border-radius: 12px; border-color: #d7e8dc; background: #fbfefb; line-height: 1.65;
    }
    [data-testid="stTextArea"] textarea:focus { border-color: var(--recap-deep); box-shadow: 0 0 0 1px var(--recap-deep); }
    [data-testid="stAlert"] { border-radius: 12px; }
    hr { border-color: #dfede2; }
    .recap-footer { color: #82978c; text-align: center; font-size: .88rem; padding-top: 1.3rem; }
    @media (max-width: 640px) {
        .block-container { padding-top: 1rem; }
        .recap-brand h1 { font-size: 1.7rem; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

if "audio_file_path" not in st.session_state:
    st.session_state.audio_file_path = None

if "transcription" not in st.session_state:
    st.session_state.transcription = None

if "summary" not in st.session_state:
    st.session_state.summary = None

st.markdown(
    '<div class="recap-brand"><div class="recap-mark">🎙️</div><h1>Recap</h1></div>'
    '<p class="recap-intro">From spoken audio to clear insights — in a few steps.</p>',
    unsafe_allow_html=True,
)

with st.container(border=True):
    st.markdown('<p class="recap-section-title">01 · Record your audio</p>', unsafe_allow_html=True)
    st.markdown('<p class="recap-section-copy">Record a conversation, lesson, or idea. You can listen to the fragment before proceeding.</p>', unsafe_allow_html=True)
    audio = st.audio_input("Record audio", label_visibility="collapsed")

    if audio is not None:
        st.audio(audio)
        if st.button("Save recording", type="primary"):
            recordings_dir = Path("recordings")
            recordings_dir.mkdir(exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_path = recordings_dir / f"recording_{timestamp}.wav"
            file_path.write_bytes(audio.getvalue())
            st.session_state.audio_file_path = str(file_path)
            st.session_state.transcription = None
            st.session_state.summary = None
            st.success(f"Recording saved: {file_path.name}")

if st.session_state.audio_file_path:
    st.write("")
    with st.container(border=True):
        st.markdown('<p class="recap-section-title">02 · Convert audio to text</p>', unsafe_allow_html=True)
        st.markdown('<p class="recap-section-copy">Let Recap convert the recording to text. You can then edit the text.</p>', unsafe_allow_html=True)
        st.caption(f"Selected recording: {Path(st.session_state.audio_file_path).name}")
        if st.button("Create transcript", type="primary"):
            with st.spinner("The recording is being transcribed…"):
                st.session_state.transcription = transcribe_audio(st.session_state.audio_file_path)
                st.session_state.summary = None

        if st.session_state.transcription:
            st.text_area(
                "Edit your transcript",
                key="transcription",
                height=260,
                help="Edit the text before creating a summary.",
            )
            if st.button("Create summary", type="primary"):
                with st.spinner("The text is being summarized…"):
                    st.session_state.summary = summarize_text(st.session_state.transcription)

if st.session_state.summary:
    st.write("")
    with st.container(border=True):
        st.markdown('<p class="recap-section-title">03 · Your summary</p>', unsafe_allow_html=True)
        st.markdown('<p class="recap-section-copy">Check and edit your key points. Download your notes when they are ready.</p>', unsafe_allow_html=True)
        st.text_area("Edit your summary", key="summary", height=190)

        st.divider()
        st.markdown('<p class="recap-section-title">Export your notes</p>', unsafe_allow_html=True)
        word_file = create_word_document(st.session_state.transcription, st.session_state.summary)
        pdf_file = create_pdf_document(st.session_state.transcription, st.session_state.summary)

        col1, col2 = st.columns(2)
        with col1:
            st.download_button(
                label="Download as Word",
                data=word_file,
                file_name="recap_notes.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                use_container_width=True,
            )
        with col2:
            st.download_button(
                label="Download as PDF",
                data=pdf_file,
                file_name="recap_notes.pdf",
                mime="application/pdf",
                use_container_width=True,
            )

st.markdown('<p class="recap-footer">Recap · From recording to overview</p>', unsafe_allow_html=True)
