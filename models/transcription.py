import os
from pathlib import Path

site_packages = Path(__file__).resolve().parent.parent / ".venv" / "Lib" / "site-packages"

cuda_paths = [
    site_packages / "nvidia" / "cublas" / "bin",
    site_packages / "nvidia" / "cudnn" / "bin",
    site_packages / "nvidia" / "cuda_runtime" / "bin",
]

os.environ["PATH"] = os.pathsep.join(
    str(path) for path in cuda_paths
) + os.pathsep + os.environ["PATH"]

dll_directories = [
    os.add_dll_directory(str(path))
    for path in cuda_paths
]

from faster_whisper import WhisperModel

model = WhisperModel(
    "base",
    device="cuda",
    compute_type="float16"
)

def transcribe_audio(audio_path):
    audio_path = Path(audio_path)

    segments, info = model.transcribe(
        audio_path,
        beam_size=5,
        language="en"
    )

    transcription = " ".join(segment.text.strip() for segment in segments)

    return transcription