# backend/app/models/request.py

from pydantic import BaseModel, Field

class SpeechRequest(BaseModel):
    text: str = Field(..., description="Texto que será convertido em áudio.")
    speed: float = Field(1.0, gt=0.3, lt=3.0, description="Velocidade da fala (default: 1.0)")
