import speech_recognition as sr
from gtts import gTTS
import os
r=sr.Recognizer()
with sr.Microphone() as source:
    print("speak anything...")
    audio=r.listen(source)
    try:
        text=r.recognize_google(audio)
        print("u said: ",format(text))
        if format(text)=="what is your name":
            myText="my name is arihant"
            output=gTTS(text=myText,lang="en",slow=False)
            output.save("name.mp3")
            os.system("start name.mp3")
        elif format(text)=="ok":
            myText="green"
            output=gTTS(text=myText,lang="en",slow=False)
            output.save("lan.mp3")
            os.system("start lan.mp3")
        else:
            print("program not running")
    except:
        print("sorry")