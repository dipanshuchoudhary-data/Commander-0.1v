import sounddevice as sd
import numpy as np
from faster_whisper import WhisperModel


class MicListener:
    def __init__(self):
        self.device_index = 2   # 👈 CHANGE THIS TO YOUR MIC INDEX
        self.model = WhisperModel(
            "base",
            device="cpu",
            compute_type="float32"
        )

    def record_and_transcribe(self, duration=5):
        print("Listening...")

        audio = sd.rec(
            int(duration * 16000),
            samplerate=16000,
            channels=1,
            device=self.device_index,
            dtype="float32"
        )
        sd.wait()

        audio = np.squeeze(audio)

        # 🔍 Check if audio is actually captured
        if audio.max() < 0.01:
            return ""

        segments, info = self.model.transcribe(audio)

        text = "".join(segment.text for segment in segments).strip()
        return text
