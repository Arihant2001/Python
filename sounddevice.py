import sounddevice as sd
duration = 10.5  # seconds
myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
