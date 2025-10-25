# JupyterLite Local

Dieses Repository soll aufzeigen, wie man JupyterLite sowohl lokal builden und testen kann, als auch via GitHub Actions auf GitHub Pages deployen kann.

## Setup

- `.venv` lokal erstellen ohne Synchronisation in Nextcloud und ohne Tracking via Git
- `.local` ohne Tracking via Git mit einem `requirements.txt` für das lokale Setup für das `.venv`
- JupyterLite Build in `.jlite` ohne Synchronisation in Nextcloud und ohne Tracking via Git

## Building

- `jupyter lite serve` macht einen Build und startet einen lokalen Server auf `http://127.0.0.1:8000/`