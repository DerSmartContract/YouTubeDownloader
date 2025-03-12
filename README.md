# 🎥 YouTube Video Downloader 📥

🚀 **Ein  Python-Tool zum Herunterladen von YouTube-Videos in höchster Qualität mit `yt-dlp`.**  
Dieses Tool ermöglicht es, Videos von YouTube effizient herunterzuladen, inklusive der besten verfügbaren Auflösung und Audioqualität.

---

## 📌 **Features**
✅ **Höchste Videoqualität**: Lädt automatisch das beste `bestvideo+bestaudio` Format herunter.  
✅ **MP4 als Standardformat**: Falls YouTube Video und Audio trennt, wird das Video zu einer `.mp4`-Datei kombiniert.  
✅ **Keine Playlists**: Es wird nur das einzelne Video heruntergeladen, keine gesamten Playlists.  
✅ **Automatische `venv`-Erkennung**: Falls eine virtuelle Umgebung existiert, wird sie automatisch genutzt.  
✅ **Plattformübergreifend**: Funktioniert auf **macOS**, **Linux** und **Windows**.

---

## 🚀 **Installation & Setup**
### 🔧 **1️⃣ Python & Virtuelle Umgebung einrichten**
Falls du noch keine **virtuelle Umgebung (`venv`)** hast, erstelle und aktiviere sie:

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

📦 2️⃣ Abhängigkeiten installieren

Installiere yt-dlp (bessere Alternative zu pytube):

pip install yt-dlp

Falls du FFmpeg benötigst (für Video-Audio-Zusammenführung), installiere es mit:

brew install ffmpeg  # macOS mit Homebrew
sudo apt install ffmpeg  # Linux (Ubuntu/Debian)
choco install ffmpeg  # Windows mit Chocolatey



⸻

🎯 Verwendung

Starte den Downloader mit:

python 1.py

Das Skript lädt das Video in höchster Auflösung herunter und speichert es im downloads/-Ordner.

⸻

💻 Code-Snippet (1.py)

import yt_dlp

def download_video(url, output_path="downloads"):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'noplaylist': True,
        'quiet': False
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=qnXfZ_cQgEU"
    download_video(video_url)



⸻

⚠ Troubleshooting

🔹 Problem: ModuleNotFoundError: No module named 'yt_dlp'
✔ Lösung: Stelle sicher, dass du die venv aktiviert hast und installiere yt-dlp erneut:

pip install yt-dlp

🔹 Problem: HTTP Error 403: Forbidden
✔ Lösung: YouTube kann pytube blockieren. Nutze yt-dlp oder aktualisiere es:

pip install --upgrade yt-dlp

🔹 Problem: ffmpeg fehlt für Video-Audio-Zusammenführung
✔ Lösung: Installiere ffmpeg (siehe Installation oben).

⸻

📜 Lizenz

Dieses Projekt steht unter der MIT-Lizenz – du kannst es frei nutzen, verändern und verbessern.

⸻

❤️ Mitwirken

Gerne Pull Requests stellen oder Issues öffnen, wenn du das Projekt verbessern möchtest! 😊

📩 Fragen? Einfach melden! 🚀

