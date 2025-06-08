import whisper

model = whisper.load_model("base")  # Du kannst später tiny, small, medium, large probieren

def transcribe_audio(filepath: str) -> str:
    print(f"[🔍] Transkription gestartet: {filepath}")
    result = model.transcribe(filepath)
    print(f"[📄] Transkription abgeschlossen.")
    return result["text"]