# Subtitle Buddy - Task Board

This document outlines the step-by-step roadmap for building and expanding Subtitle Buddy. Tasks are divided into two main phases: building the Minimum Viable Product (MVP) and implementing Future Enhancements.

## Phase 1: Minimum Viable Product (MVP)

The goal of the MVP phase is to create a functional, local web application capable of accepting media files, processing them to extract spoken text (specifically supporting English and Persian), and providing the user with a downloadable `.srt` file.

### 1. Project Initialization & Setup
- [ ] Set up the standard FastAPI folder structure (e.g., `main.py`, `routers/`, `services/`, `static/`, `templates/`).
- [ ] Define the base `requirements.txt` (`fastapi`, `uvicorn`, `faster-whisper`, `python-multipart`).
- [ ] Create a basic FastAPI health check endpoint to verify the server runs.

### 2. Basic Frontend UI
- [ ] Create a simple HTML page with vanilla CSS and JS.
- [ ] Add a file upload form that accepts audio/video files.
- [ ] Implement UI logic to show a simple "Processing... please wait" message when a file is submitted.
- [ ] Handle the backend response to allow the user to download the generated file.

### 3. Core Transcription Logic (Audio Only)
- [ ] Integrate `faster-whisper` (or standard `openai-whisper`) into the backend services.
- [ ] Create a FastAPI endpoint to accept audio uploads (e.g., `.mp3`, `.wav`).
- [ ] Process the audio file through the model to generate transcription segments.
- [ ] Write a utility function to format the transcription segments into standard `.srt` format (sequence number, start/end timestamps, text).
- [ ] Return the generated `.srt` content as a downloadable file response to the frontend.

### 4. Video Support Expansion
- [ ] Integrate an `ffmpeg` python wrapper or standard `subprocess` calls in the backend.
- [ ] Update the upload endpoint to accept video files (e.g., `.mp4`, `.mkv`).
- [ ] Add a pre-processing step: if the file is a video, use `ffmpeg` to extract the audio stream to a temporary audio file.
- [ ] Pass the extracted audio to the existing transcription logic.

### 5. MVP Polish
- [ ] Add basic error handling (e.g., unsupported file types, empty files).
- [ ] Ensure temporary files (uploaded media, extracted audio) are cleaned up/deleted after processing.
- [ ] Test the pipeline end-to-end with both English and Persian media files to ensure model accuracy and proper encoding (UTF-8).

---

## Phase 2: Future Enhancements

Once the MVP is complete and stable, the following features will be added to scale the application. The current modular architecture should support these additions with minimal refactoring.

### Subtitle Refinement & Translation
- [ ] Add functionality to translate transcribed text (e.g., English to Persian, Persian to English) before generating the `.srt` file.
- [ ] Implement an interactive subtitle editor in the UI, allowing users to tweak timing and text before downloading the final `.srt`.

### Improved User Experience
- [ ] Replace the simple "waiting" message with real-time progress updates (e.g., via WebSockets) to show line-by-line transcription progress or percentage completion.
- [ ] Add support for batch uploading and processing multiple files simultaneously.

### User Management & Cloud Integration
- [ ] Implement a database (e.g., PostgreSQL or SQLite) using an ORM like SQLAlchemy.
- [ ] Add User Authentication (Registration, Login, JWT tokens).
- [ ] Create a user dashboard to save and view the history of previously generated subtitles.
- [ ] Integrate cloud storage (e.g., AWS S3) to store uploaded media and generated subtitles instead of relying on local temporary storage.
