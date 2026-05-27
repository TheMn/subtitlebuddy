import logging
from faster_whisper import WhisperModel

# Configure basic logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Initialize model globally so it's loaded once
logger.info("Loading Whisper model 'small' on CPU with int8 compute type...")
model = WhisperModel("small", device="cpu", compute_type="int8")
logger.info("Model loaded successfully.")

def format_timestamp(seconds: float) -> str:
    """Formats seconds into SRT timestamp format (HH:MM:SS,mmm)"""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    milliseconds = int((seconds - int(seconds)) * 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{milliseconds:03d}"

def transcribe_audio(audio_path: str) -> str:
    """
    Transcribes the given audio file and returns the content in SRT format.
    """
    logger.info(f"Starting transcription for {audio_path}")

    segments, info = model.transcribe(audio_path, beam_size=5)

    logger.info(f"Detected language '{info.language}' with probability {info.language_probability}")

    srt_content = []

    for i, segment in enumerate(segments, start=1):
        start_time = format_timestamp(segment.start)
        end_time = format_timestamp(segment.end)
        text = segment.text.strip()

        # Log progress to server
        logger.info(f"Generated segment {i}: [{start_time} --> {end_time}] {text}")

        srt_content.append(f"{i}\n{start_time} --> {end_time}\n{text}\n")

    logger.info("Transcription completed successfully.")

    return "\n".join(srt_content)
