import cloudinary
import cloudinary.uploader
from app.config import CLOUDINARY_CLOUD_NAME, CLOUDINARY_API_KEY, CLOUDINARY_API_SECRET

# Configura o Cloudinary
cloudinary.config(
    cloud_name=CLOUDINARY_CLOUD_NAME,
    api_key=CLOUDINARY_API_KEY,
    api_secret=CLOUDINARY_API_SECRET,
    secure=True
)

def upload_audio(file_path: str) -> str:
    response = cloudinary.uploader.upload(
        file_path,
        resource_type="video",  # necessário para .wav
        folder="can_i_talk"
    )
    return response["secure_url"]