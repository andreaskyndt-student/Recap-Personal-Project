import streamlit as st
from pathlib import Path
from datetime import datetime

st.set_page_config(
    page_title="Recap",
    page_icon="🎙️",
    layout="wide"
)

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