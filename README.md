# Recap

**Turn speech into clear, concise summaries with AI.**

Recap is an AI-powered lecture assistant that records audio, converts speech into text, and generates easy-to-read summaries using open-source AI models from Hugging Face.

This project started as a way to explore open-source AI models and their practical applications. After attending a lecture by Niels Rogge, an engineer at Hugging Face, I became interested in the capabilities of open-source models and wanted to experiment with integrating them into a real application.

> **Project Status:** This project is done!

## Features

### Implemented
- **Audio Recording** – Record audio directly through your microphone.
- **Speech-to-Text** – Transcribe audio recordings using Whisper through Faster-Whisper.
- **English Language Support** – Transcribe English-language recordings.
- **GPU Acceleration** – Run transcription using an NVIDIA GPU with CUDA support.
- **AI Summarization** – Generate concise summaries from transcribed audio.
- **Editable Content** – Review and edit transcripts and generated summaries.
- **Document Export** – Export lecture notes as Word and PDF documents.

## Demo

[Watch the demo video](Recap-Example-Video.mp4)

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | User interface |
| Faster-Whisper | Speech-to-text transcription |
| CTranslate2 | Optimized model inference |
| PyAV | Audio decoding |
| NVIDIA CUDA | GPU acceleration |
| Hugging Face Transformers | Loading and running AI models |
| PyTorch | Deep learning framework |
| python-docx | Word document generation |
| ReportLab | PDF generation |

## AI Models

Recap uses open-source AI models available through Hugging Face.

| Model | Purpose |
|---|---|
| Whisper Base (Faster-Whisper) | Audio transcription |
| `facebook/bart-large-cnn` | Text summarization |

*The models are selected with hardware limitations in mind. I'm experimenting with different models to find a good balance between performance, resource usage, and summary quality.*

## How It Works

Recap follows a simple workflow:

1. **Record** – Start recording a lecture using your microphone.
2. **Transcribe** – Whisper converts the recorded audio into text.
3. **Summarize** – An AI model processes the transcript and generates a concise summary.
4. **Review** – View and edit the transcription and generated summary.
5. **Export** – Download your lecture notes as a Word or PDF document.

## Getting Started

### Requirements

- Python
- Git
- An NVIDIA GPU with compatible CUDA libraries for the current GPU configuration.

### Installation

1. Clone the repository:

   ```bash
   git clone <your-repository-url>
   ```

2. Navigate to the project directory:

   ```bash
   cd Recap
   ```

3. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

4. Activate the virtual environment (Windows PowerShell):

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

5. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Start the application:

   ```bash
   streamlit run app.py
   ```

> **Note:** The current GPU configuration was developed and tested on Windows with an NVIDIA GPU. Other hardware and operating systems may require additional configuration.

## Roadmap

- [x] Set up the project structure
- [x] Implement audio recording
- [x] Integrate Whisper for speech transcription
- [x] Implement GPU acceleration
- [x] Integrate an AI summarization model
- [x] Build the Streamlit user interface
- [x] Display editable transcripts and summaries
- [x] Implement PDF export
- [x] Implement Word export
- [x] Add application screenshots and demo

## Project Goals

This project is being developed as a personal portfolio project to explore:

- Open-source AI models and the Hugging Face ecosystem.
- Speech recognition and natural language processing.
- Audio processing with Python.
- Building applications with Streamlit.
- Integrating multiple AI models into one application.

---

**Built with Python and open-source AI models.**
