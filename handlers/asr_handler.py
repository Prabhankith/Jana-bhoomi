import io
import numpy as np
from pydub import AudioSegment
from transformers import pipeline

# Init Whisper pipeline
asr_pipeline = pipeline("automatic-speech-recognition", model="openai/whisper-small", device="cpu")

def transcribe_audio(audio_bytes: bytes) -> str:
    """
    Transcribe audio (wav, mp3, m4a) into text.
    Uses pydub to ensure correct PCM format.
    """
    try:
        # Load audio with pydub (auto-decodes wav, mp3, m4a)
        audio = AudioSegment.from_file(io.BytesIO(audio_bytes))
        audio = audio.set_frame_rate(16000).set_channels(1)

        # Convert to numpy float32 array
        samples = np.array(audio.get_array_of_samples()).astype(np.float32) / 32768.0

        # Run Whisper ASR
        result = asr_pipeline(samples)
        return result["text"]

    except Exception as e:
        return f"⚠️ Transcription error: {str(e)}"
