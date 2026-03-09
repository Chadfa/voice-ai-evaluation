import whisper
import time

# Load whisper model
model = whisper.load_model("base")

def transcribe_audio(audio_path):
    """
    Transcribes audio to text using Whisper
    """
    
    start_time = time.time()

    result = model.transcribe(audio_path)

    end_time = time.time()

    transcript = result["text"]

    latency = end_time - start_time

    return transcript, latency