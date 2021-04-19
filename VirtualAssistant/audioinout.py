'''this file contains speech recognition and speech code'''

import speech_recognition as sr
import pyttsx3

def speak(audio,voice=0):
    global engine,voices
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    try:
        engine.setProperty('voice',voices[voice].id)
    except:
        print('no more voices found')
    engine.say(audio)
    engine.runAndWait()

def takecommand(saythatagain=True,usersaid=True,listening_recognizing=True):
    '''takes command (it recognizes the speech spoken by the user)'''
    '''this is still under progress so this is just beta'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening......')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        if listening_recognizing is True:
            print('Recogizing....')
        query = r.recognize_google(audio,language='en-in')
        if usersaid is True:
            print(f"User Said:{query.lower()}\n")

    except Exception as e:
        if saythatagain is True:
            speak("Say That again please....")
            print("Say That again please....")
        return "None"
    return query.lower()

def getvoices(number=0):
  engine.getProperty('voices')
  try:
    return voices[number].id
  except:
      return f'error: No voices found for {number}'
