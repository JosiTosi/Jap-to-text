#!/bin/bash

# Virtuelle Umgebung aktivieren (falls vorhanden)
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Upload-Verzeichnis erstellen
mkdir -p uploads

# Server starten
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 