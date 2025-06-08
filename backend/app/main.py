from fastapi import FastAPI
from app.api import transcribe

app = FastAPI(
    title="Jap to Text",
    description="Intelligentes Speech-to-Text Tool mit ML-Fehlererkennung",
    version="0.1.0"
)

# Routen registrieren
app.include_router(transcribe.router, prefix="/api/transcribe")