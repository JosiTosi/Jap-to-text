from fastapi import APIRouter, UploadFile, File
from app.models.transcribe_model import TranscriptionRequest, TranscriptionResponse
from app.services.whisper_service import WhisperService

router = APIRouter()
whisper_service = WhisperService()

@router.post("/transcribe", response_model=TranscriptionResponse)
async def transcribe_audio(
    file: UploadFile = File(...),
    language: str = "ja"
):
    """
    Transkribiert eine Audiodatei in Text.
    """
    result = await whisper_service.transcribe(file, language)
    return TranscriptionResponse(text=result) 