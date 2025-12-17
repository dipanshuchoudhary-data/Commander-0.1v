import subprocess
from pathlib import Path

def play_music(song_name: str, music_dir="C:/Users/Public/Music"):
    files = list(Path(music_dir).rglob("*.mp3"))

    if not files:
        return "No music found."

    if song_name:
        for f in files:
            if song_name.lower() in f.name.lower():
                subprocess.Popen(["cmd", "/c", f"start {f}"])
                return f"Playing {f.name}"

    subprocess.Popen(["cmd", "/c", f"start {files[0]}"])
    return f"Playing {files[0].name}"
