from fastapi import FastAPI, UploadFile, File, Form
from app.whisper_service import transcribe_audio
from app.downloader import download_audio
import shutil

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Whisper API en línea 🚀"}

@app.post("/transcribe/file/")
async def transcribe_file(file: UploadFile = File(...)):
    with open(f"temp.wav", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    result = transcribe_audio("temp.wav")
    return {"transcription": result}

@app.post("/transcribe/url/")
async def transcribe_from_url(url: str = Form(...)):
    path = download_audio(url)
    result = transcribe_audio(path)
    return {"transcription": result}


