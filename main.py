import asyncio
import os
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import Response
from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    # Simulate processing delay
    await asyncio.sleep(2)

    # Generate a dummy SRT content
    srt_content = """1
00:00:01,000 --> 00:00:05,000
This is a dummy subtitle.

2
00:00:05,000 --> 00:00:10,000
It was generated from the mock endpoint.
"""

    # Extract original filename and change extension to .srt
    original_filename = file.filename if file.filename else "subtitles"
    base_name = os.path.splitext(original_filename)[0]
    srt_filename = f"{base_name}.srt"

    return Response(
        content=srt_content,
        media_type="text/plain",
        headers={"Content-Disposition": f'attachment; filename="{srt_filename}"'}
    )

# Mount the static directory to serve index.html and other assets
app.mount("/", StaticFiles(directory="static", html=True), name="static")
