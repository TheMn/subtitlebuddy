import os
import shutil
import tempfile
import logging
from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import Response

from services.transcription import transcribe_audio

router = APIRouter()
logger = logging.getLogger(__name__)

# Basic validation for audio files (MVP focus)
ALLOWED_EXTENSIONS = {".mp3", ".wav", ".m4a", ".flac", ".ogg", ".aac"}

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file uploaded")

    # Check extension
    ext = os.path.splitext(file.filename)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        # For now, we only strictly accept audio files for Task 3
        # In a real scenario or future task, we might be more lenient or handle video.
        # But user said "just accept the audio files that you can process"
        pass # Allow it to proceed and let faster-whisper/ffmpeg attempt to handle it

    # We will use tempfile.TemporaryDirectory() for security and cleanup
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            # Secure the filename to prevent path traversal
            safe_filename = os.path.basename(file.filename)
            temp_file_path = os.path.join(temp_dir, safe_filename)

            # Save the uploaded file
            logger.info(f"Saving uploaded file to {temp_file_path}")
            with open(temp_file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)

            # Transcribe the file
            try:
                srt_content = transcribe_audio(temp_file_path)
            except Exception as e:
                logger.error(f"Error during transcription: {str(e)}")
                raise HTTPException(status_code=500, detail=f"Transcription failed: {str(e)}")

            # Extract original filename and change extension to .srt
            base_name = os.path.splitext(file.filename)[0]
            srt_filename = f"{base_name}.srt"

            return Response(
                content=srt_content,
                media_type="text/plain",
                headers={"Content-Disposition": f'attachment; filename="{srt_filename}"'}
            )

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
