# Yap to Text 🗣️➡️📄

**yap to Text** ist ein intelligentes Speech-to-Text-Tool, das speziell für die persönliche Nutzung entwickelt wird. Es verwandelt gesprochene Sprache in Text und erkennt dabei Versprecher, thematische Abschweifungen und andere Kontexteffekte. Die Anwendung läuft im Web und erlaubt individuelle Konfigurationen wie z. B. Hotkeys.

## 🚀 Features (in Planung)

- 🎙️ Echtzeit-Spracherkennung via Mikrofon
- 🧠 Intelligente Fehlerkorrektur (z. B. Versprecher erkennen, Ablenkungen filtern)
- 🖥️ Webbasierte Oberfläche zur Konfiguration (Hotkey, Sprache, Layout etc.)
- 🧪 Experimentelle Funktionen:
  - Live-Transkription mit Pausenerkennung
  - Rücknahme bei thematischer Abschweifung

## 🛠 Tech Stack (geplant)

- **Frontend**: React, TailwindCSS
- **Backend**: FastAPI (Python)
- **Speech Engine**: OpenAI Whisper (optional: Vosk oder andere lokale Modelle)

## 📁 Projektstruktur (vorläufig)

```
jap-to-text/
├── backend/                  # FastAPI Backend (Python)
│   ├── app/
│   │   ├── api/              # API-Routen (Transkription, Einstellungen)
│   │   ├── core/             # Konfiguration & Setup
│   │   ├── services/         # STT-Logik & Fehlererkennung
│   │   ├── models/           # Datenmodelle
│   │   └── main.py           # FastAPI Entry Point
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/                 # Web-UI mit React & TailwindCSS
│   ├── public/
│   ├── src/
│   │   ├── components/       # UI-Komponenten
│   │   ├── pages/            # Seiten (Home, Settings)
│   │   ├── hooks/            # Audio Hooks etc.
│   │   ├── lib/              # API-Client, Hilfsfunktionen
│   │   └── App.tsx
│   ├── tailwind.config.js
│   └── package.json
│
├── .env                     # Umgebungsvariablen
├── .gitignore               # Git-Konfiguration
└── README.md                # Projektdokumentation
```

## 📦 Installation (folgt später)

Anleitungen zur lokalen Installation und Nutzung werden mit dem ersten funktionalen Release ergänzt.

## ⚠️ Hinweis

Dieses Projekt befindet sich in aktiver Entwicklung. Der Fokus liegt auf Qualität, modularer Architektur und intelligenter Nutzerinteraktion.

## 📃 Lizenz

Prototypisch, private Nutzung. Eine offizielle Lizenz wird zu einem späteren Zeitpunkt ergänzt.

## 📋 Umgebungsvariablen

```env
DEFAULT_LANGUAGE=ja
MODEL_SIZE=base
```
