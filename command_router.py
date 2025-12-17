import re

def normalize(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    return text.strip()


def interpret_text(text: str):
    text = normalize(text)

    if not text:
        return "unknown", ""

    if "open" in text:
        return "open_app", text.replace("open", "").strip()

    if "play" in text:
        return "play_music", text.replace("play", "").strip()

    if "search" in text or "find" in text:
        return "search_file", text.replace("search", "").replace("find", "").strip()

    return "unknown", text
