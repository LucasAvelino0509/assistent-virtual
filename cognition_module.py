import win32api
import pyttsx3
import speech_recognition as sr
import sys

r = sr.Recognizer()
def listen():
    with sr.Microphone() as s:
        while True:
            print("listening")
            try:
                audio = r.listen(s)
                speech = r.recognize_google(audio, language='pt-BR')
                print(speech)
                return speech
            except  Exception as e:
                print(sys.exc_info())
                return ""

def speak(txt):
    speaker = pyttsx3.init('sapi5')
    voices = speaker.getProperty('voices')
    for voice in voices:
        if voice.name=='Microsoft Maria Desktop - Portuguese(Brazil)':
            speaker.setProperty('voice',voice.id)
    speaker.say(txt)
    speaker.runAndWait()
