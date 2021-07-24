import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
    print("speak anything...")
    audio=r.listen(source)
    try:
        text=r.recognize_google(audio)
        print("u said: ",format(text))
        if format(text)=="what is your name":
            print("arihant")
    except:
        print("sorry")
