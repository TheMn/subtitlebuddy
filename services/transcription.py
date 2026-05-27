import os
from faster_whisper import WhisperModel

# Initialize the model once. Using the small model for MVP balance of speed and accuracy.
# Adjust compute_type or device if you have specific hardware requirements.
model = WhisperModel("small", device="cpu", compute_type="int8")

def format_timestamp(seconds: float) -> str:
    """Converts seconds to SRT timestamp format (HH:MM:SS,mmm)."""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millisecs = int((seconds - int(seconds)) * 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millisecs:03d}"

def transcribe_audio_to_srt(file_path: str) -> str:
    """
    Transcribes an audio file and returns the content in SRT format.
    """
    segments, info = model.transcribe(file_path, beam_size=5)

    srt_content = ""
    for idx, segment in enumerate(segments, start=1):
        start_time = format_timestamp(segment.start)
        end_time = format_timestamp(segment.end)
        text = segment.text.strip()

        srt_content += f"{idx}\n"
        srt_content += f"{start_time} --> {end_time}\n"
        srt_content += f"{text}\n\n"

    return srt_content
