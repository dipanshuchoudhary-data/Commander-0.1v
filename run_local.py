import keyboard
from audio_listener import MicListener
from command_router import interpret_text
from actions.open_app import open_application
from actions.search_files import search_files
from actions.play_music import play_music


def main():
    print("🎙️ Local Audio Command Ready")
    print("👉 Press SPACE to speak | Ctrl+C to exit")

    listener = MicListener()

    while True:
        keyboard.wait("space")

        print("🎤 Recording...")
        text = listener.record_and_transcribe(duration=5)

        if not text or len(text.strip()) < 3:
            print("⚠️ No clear speech detected")
            print("-" * 40)
            continue

        print("🧠 Heard:", text)

        action, payload = interpret_text(text)

        if action == "open_app":
            result = open_application(payload)
        elif action == "search_file":
            result = search_files(payload)
        elif action == "play_music":
            result = play_music(payload)
        else:
            result = "Unknown command"

        print("⚙️ Result:", result)
        print("-" * 40)


if __name__ == "__main__":
    main()
