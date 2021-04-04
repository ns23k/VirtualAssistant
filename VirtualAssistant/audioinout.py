'''this file contains speech recognition and speech code'''

import speech_recognition as sr
import pyttsx3

def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.say(audio)
    engine.runAndWait()

def takecommand(saythatagain=True):
    '''takes command'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening......')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recogizing....')
        query = r.recognize_google(audio,language='en-in')
        print(f"User Said:{query}\n")

    except Exception as e:
        if saythatagain == True:
            speak("Say That again please....")
        print("Say That again please....")
        return "None"
    return query
