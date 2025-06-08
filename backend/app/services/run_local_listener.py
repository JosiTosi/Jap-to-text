import keyboard
from app.services.audio_capture import record_audio
from app.services.whisper_service import transcribe_audio

print("[🟢] Listener gestartet. Drücke F9 für Aufnahme.")

while True:
    keyboard.wait("F9")
    filepath = record_audio()
    text = transcribe_audio(filepath)
    print(f"📝 Transkribierter Text:\n{text}\n")