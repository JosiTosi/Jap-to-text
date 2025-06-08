from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    # Basis-Pfade
    BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent
    UPLOAD_DIR: Path = BASE_DIR / "uploads"
    
    # Whisper-Einstellungen
    DEFAULT_LANGUAGE: str = "ja"
    MODEL_SIZE: str = "base"
    
    # API-Einstellungen
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Jap-to-Text"
    
    class Config:
        env_file = ".env"

settings = Settings() 