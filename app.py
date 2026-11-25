import streamlit as st
from pathlib import Path
from datetime import datetime
from models.transcription import transcribe_audio
from models.summarization import summarize_text
from utils.document_export import create_word_document, create_pdf_document

st.set_page_config(
    page_title="Recap",
    page_icon="🎙️",
    layout="wide"
)

if "audio_file_path" not in st.session_state:
    st.session_state.audio_file_path = None

if "transcription" not in st.session_state:
    st.session_state.transcription = None

if "summary" not in st.session_state:
    st.session_state.summary = None

st.title("Recap")
st.write("Record your audio, and turn it into a summary using AI.")

audio = st.audio_input("Click to record your audio")

if audio is not None:
    st.audio(audio)

    if st.button("Save Recording"):
        recordings_dir = Path("recordings")
        recordings_dir.mkdir(exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = recordings_dir / f"recording_{timestamp}.wav"

        file_path.write_bytes(audio.getvalue())
        st.success(f"Recording saved as {file_path.name}")

        st.session_state.audio_file_path = str(file_path)

st.divider()

if st.session_state.audio_file_path:
        if st.button("Transcribe Recording"):
            with st.spinner("Our AI is working on your recording ..."):
                st.session_state.transcription = transcribe_audio(st.session_state.audio_file_path)

                st.session_state.summary = None

        if st.session_state.transcription:
            st.subheader("Transcription")
            st.session_state.transcription = st.text_area(
                "Edit your transcription:",
                value=st.session_state.transcription,
                height=300
            )

            if st.button("Summarize Transcription"):
                with st.spinner("Our AI is summarizing your transcription ..."):
                    st.session_state.summary = summarize_text(st.session_state.transcription)

        if st.session_state.summary:
            st.subheader("Summary")
            st.session_state.summary = st.text_area(
                "Edit your summary:",
                value=st.session_state.summary,
                height=200
            )

            st.divider()
            st.subheader("Download your notes")

            word_file = create_word_document(st.session_state.transcription, st.session_state.summary)
            pdf_file = create_pdf_document(st.session_state.transcription, st.session_state.summary)

            col1, col2 = st.columns(2)

            with col1:
                st.download_button(
                    label="Download as Word Document",
                    data=word_file,
                    file_name="recap_notes.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )

            with col2:
                st.download_button(
                    label="Download as PDF Document",
                    data=pdf_file,
                    file_name="recap_notes.pdf",
                    mime="application/pdf"
                )