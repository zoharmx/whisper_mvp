# 🎙️ Whisper Transcription API

Este proyecto es un backend basado en FastAPI que permite transcribir archivos de audio/video (mp3, mp4, wav, webm, etc.) usando el modelo Whisper de OpenAI. Opcionalmente puede subir los resultados a Google Drive.

## 🚀 Requisitos

- Python 3.10+
- ffmpeg (instalado y en el PATH)
- Whisper (OpenAI)
- FastAPI
- Uvicorn
- yt-dlp (para descargas desde YouTube, TikTok, etc.)

## 🛠️ Instalación

```bash
git clone https://github.com/tu-usuario/whisper-api.git
cd whisper-api
python -m venv venv
source venv/bin/activate  # o .\venv\Scripts\activate en Windows
pip install -r requirements.txt
