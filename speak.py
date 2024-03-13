import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('rate',150)
engine.setProperty('voices',voices[0].id)

def Speak(*args, **kargs):
    audio = ""
    for i in args:
        audio += str(i)
    print(audio)
    engine.say(audio)
    engine.runAndWait()

# Speak("Hi, my name is jarvis")
"""Yups This is for testing updationn in github repo"""