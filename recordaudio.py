import sounddevice as sd
def recordAudio(text):
  from scipy.io.wavfile import write
  fs = 44100  # Sample rate
  seconds = 5  # Duration of recording
  text=text+".wav"
  myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
  sd.wait()  # Wait until recording is finished
  write(text, fs, myrecording)  # Save as WAV file

recordAudio("Hello")
