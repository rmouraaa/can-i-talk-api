import os
import torch
import soundfile as sf
from kokoro import KPipeline
from app.utils.id_gen import generate_unique_id

# Inicia o pipeline apenas uma vez
pipeline = KPipeline(lang_code='p')  # 'p' = português brasileiro

def generate_speech(text: str, speed: float = 1.0) -> str:
    audio_gen = pipeline(text, speed=speed, voice="af_heart")

    # Pega o primeiro resultado
    result = next(audio_gen)
    audio_tensor = result.audio

    # Converte para numpy
    audio_array = audio_tensor.cpu().numpy()

    # Gera um nome único
    filename = f"{generate_unique_id()}.wav"
    output_path = os.path.join("static", filename)

    # Salva o áudio em 24kHz (padrão do modelo)
    sf.write(output_path, audio_array, samplerate=24000)

    return output_path  # Ex: "static/xyz.wav"