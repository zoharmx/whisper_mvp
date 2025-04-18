import whisper

model = whisper.load_model("base")  # más ligero, ~300MB RAM

def transcribe_audio(path: str) -> str:
    result = model.transcribe(path)
    return result["text"]
