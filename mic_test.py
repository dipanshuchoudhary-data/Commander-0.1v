import sounddevice as sd
import numpy as np

device_index = 2  # same index

print("Speak now...")
audio = sd.rec(16000 * 3, samplerate=16000, channels=1, device=device_index)
sd.wait()

audio = np.squeeze(audio)
print("Max amplitude:", audio.max())
