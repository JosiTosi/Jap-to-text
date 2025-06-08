from pydantic import BaseModel

class TranscriptionRequest(BaseModel):
    language: str = "ja"

class TranscriptionResponse(BaseModel):
    text: str 