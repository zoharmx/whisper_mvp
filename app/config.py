import os

class Settings:
    MODEL_SIZE = os.getenv("MODEL_SIZE", "large")  # Tamaño del modelo: tiny, base, small, medium, large
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "./temp")
    ALLOWED_EXTENSIONS = {"mp3", "mp4", "m4a", "wav", "webm", "mpga"}
    GOOGLE_DRIVE_UPLOAD = os.getenv("GOOGLE_DRIVE_UPLOAD", "false").lower() == "true"
    WHISPER_LANGUAGE = os.getenv("WHISPER_LANGUAGE", None)  # Puedes forzar "es" o dejarlo como None para autodetectar

settings = Settings()
