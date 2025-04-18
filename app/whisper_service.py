import whisper

model = whisper.load_model("large")

def transcribe_audio(path: str) -> str:
    result = model.transcribe(path)
    return result["text"]
