import streamlit as st
from pathlib import Path
from datetime import datetime
from models.transcription import transcribe_audio

st.set_page_config(
    page_title="Recap",
    page_icon="🎙️",
    layout="wide"
)

if "audio_file_path" not in st.session_state:
    st.session_state.audio_file_path = None

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
            transcription = transcribe_audio(st.session_state.audio_file_path)

        st.subheader("Transcription")
        st.write(transcription)