FROM python:3.10-slim

# Instala dependencias necesarias del sistema
RUN apt-get update && apt-get install -y \
    git \
    ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]


