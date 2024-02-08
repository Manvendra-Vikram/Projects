import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from langdetect import detect
from translate import Translator

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()





def run_alexa():
    
    command= take_command()
    print(command)
    if 'goodbye' in command:
        talk('shutting down')
        exit(0)
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'what' or 'symptoms' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 10)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command1 = listener.recognize_google(voice)
            
            command1 = command1.lower()
            if 'alexa' in command1:
                command1 = command1.replace('alexa', '')
                print(command1)
    except:
        pass
    return command1


while True:
    run_alexa()

