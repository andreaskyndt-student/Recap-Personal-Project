# Recap

**Turn speach into clear, concise summaries with AI.**

Recap is an AI-powered assistant that records audio, converts speech into text, and generates easy-to-read summaries using open-source AI models from Hugging Face.

The goal of this project is to learn more about using open-source models that are available on Hugging Face. I wanted to try this after experiencing a lecture given by Niels Rogge (an engineer at Hugging Face), he talked about the strengths of the open-source models that exist.

> **Project Status:** In Development

## Features

Planned features include:

- **Audio Recording** – Record speach directly through your microphone.
- **Speech-to-Text** – Convert audio into text using a Hugging Face model (to be decided).
- **AI Summarization** – Generate concise summaries using a Hugging Face model (to be decided).
- **Editable Content** – Review and edit summaries.
- **Export Summaries** – Download summaries as TXT or PDF files.

## Demo

*Screenshots and a demo will be added once the application is functional.*

## Tech Stack

The project is planned to use the following technologies:

| Python | Main programming language |
| Streamlit | User interface |

## AI Models

Recap aims to use open-source models available through Hugging Face.

| Model | Purpose |
|---|---|
| `openai/whisper-base` | Audio transcription |
| `google/flan-t5-base` | Text summarization |

*The selected models may change during development depending on performance, language support and hardware requirements.*

## How It Works

Recap follows a simple workflow:

1. **Record** – Start recording a lecture using your microphone.
2. **Transcribe** – Whisper converts the recorded audio into text.
3. **Summarize** – An AI language model processes the transcript and generates a summary.
4. **Review** – View and edit the generated summary.
5. **Export** – Download the summary for later use.

## Roadmap

- [ ] Set up the project structure
- [ ] Implement audio recording
- [ ] Integrate Whisper for speech transcription
- [ ] Integrate an AI summarization model
- [ ] Build the Streamlit user interface
- [ ] Display editable transcripts and summaries
- [ ] Implement TXT export
- [ ] Implement PDF export
- [ ] Add testing and error handling
- [ ] Add application screenshots and demo

## Project Goals

This project is being developed as a personal portfolio project to explore:

- Open-source AI models.
- Speech recognition and natural language processing.
- Audio processing with Python.
- Building applications with Streamlit.
- Integrating multiple AI models into one application.

---

**Built with Python and open-source AI models.**
