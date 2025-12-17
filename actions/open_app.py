import subprocess
from difflib import get_close_matches

APP_MAP = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "chrome": "chrome.exe",
    "edge": "msedge.exe",
}

def open_application(app_name: str):
    if not app_name:
        return "No app name provided"

    keys = list(APP_MAP.keys())
    match = get_close_matches(app_name, keys, n=1, cutoff=0.6)

    if not match:
        return f"App not mapped: {app_name}"

    exe = APP_MAP[match[0]]
    subprocess.Popen(exe)

    return f"Opened {match[0]}"
