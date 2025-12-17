import json
from fastmcp import FastMCP
from audio_listener import MicListener
from command_router import interpret_text
from actions.open_app import open_application
from actions.play_music import play_music
from actions.search_files import search_files

mcp = FastMCP("commander-0.1")

@mcp.tool
def listen_and_execute():
    """
    Listens via microphone, converts to text using Whisper, 
    routes the command, and performs the action.
    """
     
    listener = MicListener()
    text = listener.record_and_transcribe()

    action,payload = interpret_text(text)

    if action == "open_app":
        result = open_application(payload)

    elif action == "search_file":
        result = search_files(payload)
    elif action == "play_music":
        result = play_music(payload)
    else:
        result = f"Unknown command: {text}"

    return {
        "heard": text,
        "action": action,
        "result": result
    }


if __name__ == "__main__":
    mcp.run()
