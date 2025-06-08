import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import time
from datetime import datetime
import os

DURATION = 10  # Sekunden
SAMPLE_RATE = 16000  # Whisper bevorzugt 16000 Hz
OUTPUT_DIR = "recordings"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def record_audio(filename: str = None, duration: int = DURATION, fs: int = SAMPLE_RATE):
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{OUTPUT_DIR}/recording_{timestamp}.wav"
    
    print(f"[🎙️] Aufnahme gestartet ({duration}s)...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype="int16")
    sd.wait()
    wav.write(filename, fs, audio)
    print(f"[✅] Aufnahme gespeichert: {filename}")
    return filename