import os
import sounddevice as sd
import acoustid
import chromaprint
import numpy as np
import matplotlib.pyplot as plt
from fuzzywuzzy import fuzz
from scipy.io.wavfile import write

def recordAudio(text):
  fs = 44100
  seconds = 3  
  text="tempRecording/"+text+".wav"
  myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
  sd.wait() 
  write(text, fs, myrecording)  

def textToSpeech(text):
    engine=pyt.init()
    rate=engine.getProperty('rate')
    engine.setProperty('rate',rate-30)
    engine.say(text)
    engine.runAndWait()

def voiceDiarization(inputAudioFile,listFile):
    max_similarity = 100
    duration1, fp_encoded1 = acoustid.fingerprint_file(inputAudioFile)
    fingerprint1, version1 = chromaprint.decode_fingerprint(fp_encoded1)
    for i in listFile:
        duration2, fp_encoded2 = acoustid.fingerprint_file(audioFile)
        fingerprint2, version2 = chromaprint.decode_fingerprint(fp_encoded2)
        similarity = fuzz.ratio(fingerprint1, fingerprint2)
        if similarity < max_similarity:
            max_similarity = similarity
            max_file = i
    return max_file

if __name__ == "__main__" :
    print("Hey Good Morning.....")
    listFile=os.listdir('wav/')
    nList = list([1,2])

    for i in nList:
        print("start recording")
        recordAudio(i)
        print("Audio Recorded .....")
        print("start voice diarization")
        file = "tempRecording/"+str(i)+".wav"
        speaker = voiceDiarization(file,listFile)
        print(speaker, "is present.")