import speech_recognition as sr
import pyttsx3
import os
engine=pyttsx3.init()
r=sr.Recognizer()
with sr.Microphone() as source:
    print("speak anything...")
    audio=r.listen(source)
    try:
        text=r.recognize_google(audio)
        print("u said: ",format(text))
        if format(text)=="name":
            engine.say("my name is arihant")
            engine.runAndWait()
        elif format(text)=="fruit":
            engine.say("apple")
            engine.runAndWait()
        elif format(text)=="song":
            os.system("start LiveWhileWeAreYoung.mp3")
            end()
        else:
            print("program not running")
    except:
        print("sorry")
