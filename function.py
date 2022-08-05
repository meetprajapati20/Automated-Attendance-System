import os
import sounddevice as sd
import acoustid
import chromaprint
import numpy as np
import matplotlib.pyplot as plt
import pyttsx3 as pyt
from fuzzywuzzy import fuzz
from scipy.io.wavfile import write
from copy import copy
from xlutils.copy import copy
from xlrd import open_workbook
import datetime

def recordAudio(text):
  fs = 44100
  seconds = 5 
  text="tempRecording/"+str(text)+".wav"
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
    max_similarity = 0
    duration1, fp_encoded1 = acoustid.fingerprint_file(inputAudioFile)
    fingerprint1, version1 = chromaprint.decode_fingerprint(fp_encoded1)
    for i in listFile:
        duration2, fp_encoded2 = acoustid.fingerprint_file("wav/"+str(i))
        fingerprint2, version2 = chromaprint.decode_fingerprint(fp_encoded2)
        similarity = fuzz.ratio(fingerprint1, fingerprint2)
        if similarity > max_similarity:
            max_similarity = similarity
            max_file = i
        print(similarity,i)
    return max_file

def attandance(rollno,status):
    current_time = datetime.datetime.now()
    rb = open_workbook("Attendance_Entry.xls")
    wb = copy(rb)
    w_sheet = wb.get_sheet(0)
    if status == rollno:
        w_sheet.write(rollno, current_time.day, 'P')
    else:
        w_sheet.write(rollno, current_time.day, 'A')
    wb.save('Attendance_Entry.xls')

def getStudentEnroll():
    wb = open_workbook("Attendance_Entry.xls")
    w_sheet = wb.sheet_by_index(0)
    enRoll = list()
    while (w_sheet.cell_value(i,0) != ''):
        enRoll.append(w_sheet.cell_value(i,0))
        i+=1
    return enRoll

if __name__ == "__main__" :
    print("Hey Good Morning.....")
    listFile=os.listdir('wav/')
    nList = getStudentEnroll()

    for i in nList:
        print("start recording")
        recordAudio(i)
        print("Audio Recorded .....")
        print("start voice diarization")
        file = "tempRecording/"+str(i)+".wav"
        speaker = voiceDiarization(file,listFile)
        print(speaker.split(".")[0], "is present.")
        attandance(i,speaker.split(".")[0])
