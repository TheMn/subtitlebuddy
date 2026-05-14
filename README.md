# Subtitle Buddy

Subtitle Buddy is a lightweight, scalable platform designed to easily generate subtitles from audio and video files. It is built to specifically support English and Persian languages natively, aiming to provide an accessible and fast solution for transcribing spoken words into timeline-accurate subtitle files (`.srt`).

## Features (Current & Planned)

- **Audio & Video Support**: Extract and transcribe audio directly from uploaded media files.
- **Bilingual Focus**: Optimized for both English and Persian (Farsi) languages.
- **Accurate Subtitles**: Generates standard `.srt` files matching the media timeline.
- **Minimalist UI**: Simple HTML/CSS/JS frontend for easy uploads and processing.
- **Future-Ready**: Built with a modular architecture to seamlessly support upcoming features like translation, detailed progress tracking, and user authentication.

## Tech Stack

- **Backend**: [FastAPI](https://fastapi.tiangolo.com/) - A modern, fast (high-performance), web framework for building APIs with Python.
- **Frontend**: Plain HTML, CSS, and vanilla JavaScript for a lightweight, dependency-free UI.
- **Transcription Engine**: [faster-whisper](https://github.com/SYSTRAN/faster-whisper) - For efficient, accurate, and offline transcription of both English and Persian.
- **Media Processing**: `ffmpeg` - Used for extracting audio streams from video files.

## Project Architecture & Scalability

Subtitle Buddy is designed to be a Minimum Viable Product (MVP) right now, but with growth in mind.
The application separates routing, processing logic, and static front-end assets. This modular approach ensures that adding features—such as real-time WebSocket progress updates, user login systems, or cloud storage integration—can be implemented smoothly in the future without a complete rewrite.

## Installation & Setup

### Prerequisites

1. **Python 3.9+**
2. **FFmpeg**: You must have `ffmpeg` installed on your system to process media files.
   - **Ubuntu/Debian**: `sudo apt update && sudo apt install ffmpeg`
   - **MacOS**: `brew install ffmpeg`
   - **Windows**: Download from the [official site](https://ffmpeg.org/download.html) or use `winget install ffmpeg`.

### Running the Project

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd subtitle-buddy
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   *(Note: ensure `fastapi`, `uvicorn`, `faster-whisper`, and `python-multipart` are in the requirements file once set up).*

4. **Start the FastAPI server**:
   ```bash
   uvicorn main:app --reload
   ```

5. **Access the Application**:
   Open your browser and navigate to `http://127.0.0.1:8000`.

## License

This project is open-source. (Add License details here)
