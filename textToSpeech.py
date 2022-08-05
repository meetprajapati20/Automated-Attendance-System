import psutil
import pyttsx3

def func(c):
    engine=pyttsx3.init() 
    if(c==True):
        engine.say("Charger Plugged")
    else:
        engine.say("Charger Unplugged")
    engine.runAndWait() 


battery=psutil.sensors_battery()
a=battery.power_plugged
engine=pyttsx3.init() 
low=False
high=False
func(a)
while (True):
    x=int(battery.percent)
    if(x==100 and high==False):
        engine.say("Fully Charged")
        engine.runAndWait()
        high=True
    elif(x==15 and low==False):
        engine.say("Battery Low, Charge Soon")
        engine.runAndWait()
        low=True
    elif(x>15 and x<100):
        low=high=False
    battery=psutil.sensors_battery()
    b=battery.power_plugged
    if not(a==b):
        func(b)
        a=b
        