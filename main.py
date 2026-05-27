import asyncio
import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers.transcription import router as transcription_router

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

# Include routers
app.include_router(transcription_router)

# Mount the static directory to serve index.html and other assets
app.mount("/", StaticFiles(directory="static", html=True), name="static")
