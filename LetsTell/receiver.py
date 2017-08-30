import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone(device_index=0) as source:
        audio = r.listen(source)

        print("You said :" + r.recognize_google(audio))
