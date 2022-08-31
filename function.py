import os
import sounddevice as sd
import acoustid
import chromaprint
import numpy as np
import matplotlib.pyplot as plt
import pyttsx3 as pyt
import datetime
import smtplib
from fuzzywuzzy import fuzz
from scipy.io.wavfile import write
from copy import copy
from xlutils.copy import copy
from xlrd import open_workbook

stuEmail = list()
def sendMail(studentEmail,msg):
    fromaddr = "meetprajapati20@gnu.ac.in"
    toaddr = studentEmail
    username = "meetprajapati20@gnu.ac.in"
    password = "gnu15102020"
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr,toaddr,msg)
    server.quit()

def recordAudio():
  fs = 44100
  seconds = 5 
  text="tempRecording/temp.wav"
  myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
  sd.wait() 
  write(text, fs, myrecording)  

def textToSpeech(text):
    engine=pyt.init()
    rate=engine.getProperty('rate')
    engine.setProperty('rate',rate-30)
    engine.say("Roll Number "+str(text))
    engine.runAndWait()

def voiceDiarization(inputAudioFile,File):
    max_similarity = 0
    duration1, fp_encoded1 = acoustid.fingerprint_file(inputAudioFile)
    fingerprint1, version1 = chromaprint.decode_fingerprint(fp_encoded1)
    duration2, fp_encoded2 = acoustid.fingerprint_file(File)
    fingerprint2, version2 = chromaprint.decode_fingerprint(fp_encoded2)
    similarity = fuzz.ratio(fingerprint1, fingerprint2)
    print(similarity,File)
    return similarity

def attandance(rollno,status):
    current_time = datetime.datetime.now()
    rb = open_workbook("Attendance_Entry.xls")
    wb = copy(rb)
    w_sheet = wb.get_sheet(0)
    w_sheet.write(rollno, current_time.day + 2, status)
    wb.save('Attendance_Entry.xls')

def getStudentEnroll():
    wb = open_workbook("Attendance_Entry.xls")
    w_sheet = wb.sheet_by_index(0)
    enRoll = list()
    global stuEmail
    i=1
    j=w_sheet.nrows
    print(j)
    while (i != j):
        enRoll.append(w_sheet.cell_value(i,0))
        stuEmail.append(w_sheet.cell_value(i,2))
        i+=1
    return enRoll

if __name__ == "__main__" :
    current_time = datetime.datetime.now()
    print("Hey Good Morning Students.....")
    listFile=os.listdir('wav/')
    nList = getStudentEnroll()

    for i in nList:
        mp3="wav/"+str(int(i))+".wav"
        textToSpeech(int(i))
        print("start recording")
        recordAudio()
        print("Audio Recorded .....")
        print("start voice diarization")
        file = "tempRecording/temp.wav"
        speaker = voiceDiarization(file,mp3)
        if(speaker>50):
            attandance(i,"P")
            msg = "You've been marked Present on ."+str(current_time.day)+"/"+str(current_time.month)+"."            
        else:
            attandance(i,"A")
            msg = "You've been marked Absent on ."+str(current_time.day)+"/"+str(current_time.month)+"."
        #sendMail(stuEmail[nList.index(i)],msg)
