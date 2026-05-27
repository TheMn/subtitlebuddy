from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routers import upload

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

# Include routers
app.include_router(upload.router)

# Mount the static directory to serve index.html and other assets
app.mount("/", StaticFiles(directory="static", html=True), name="static")
