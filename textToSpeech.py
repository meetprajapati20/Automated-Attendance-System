import pyttsx3 as pyt

engine=pyt.init()
rate=engine.getProperty('rate')
engine.setProperty('rate',rate-30)
engine.say('Hello World')
engine.runAndWait()