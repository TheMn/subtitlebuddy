import os
import shutil
import tempfile
from fastapi import APIRouter, File, UploadFile
from fastapi.responses import Response

from services.transcription import transcribe_audio_to_srt

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    # Create a temporary directory to store the uploaded file
    with tempfile.TemporaryDirectory() as temp_dir:
        # Use a safe temporary filename instead of the user-provided filename
        # to prevent arbitrary file write / path traversal vulnerabilities.
        safe_filename = "uploaded_audio"
        temp_file_path = os.path.join(temp_dir, safe_filename)

        # Save the uploaded file to the temporary location
        with open(temp_file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Transcribe the audio and get the SRT content
        srt_content = transcribe_audio_to_srt(temp_file_path)

    # The temporary file and directory are automatically deleted when the with block exits

    # Extract original filename and change extension to .srt
    original_filename = file.filename if file.filename else "subtitles"
    base_name = os.path.splitext(original_filename)[0]
    srt_filename = f"{base_name}.srt"

    return Response(
        content=srt_content,
        media_type="text/plain",
        headers={"Content-Disposition": f'attachment; filename="{srt_filename}"'}
    )
