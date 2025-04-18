from fastapi import FastAPI, HTTPException
from app.models.request import SpeechRequest
from app.services.tts import generate_speech
from app.services.cloudinary import upload_audio
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API Can I Talk está rodando! 🎉"}

@app.post("/generate")
def generate_audio(request: SpeechRequest):
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Texto não pode estar vazio.")

    try:
        # 1. Gera áudio
        local_path = generate_speech(request.text, request.speed)

        # 2. Faz upload
        url = upload_audio(local_path)

        # 3. Remove o arquivo temporário
        if os.path.exists(local_path):
            os.remove(local_path)

        return {
            "message": "Áudio gerado com sucesso!",
            "url": url
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))