import pyttsx3 as pyt

def textToSpeech(text):
    engine=pyt.init()
    rate=engine.getProperty('rate')
    engine.setProperty('rate',rate-30)
    engine.say(text)
    engine.runAndWait()

textToSpeech("Hello World")
