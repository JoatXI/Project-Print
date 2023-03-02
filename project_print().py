import speech_recognition as sr
import pyttsx3
import wikipedia
import pywhatkit
import datetime
import pyjokes
import selenium

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

wake_commands = ["hello print", "are you there print?", "print, are you there?", "okay print", "hey print", "excuse me print", "yo print", "do you have a moment print?", "can you help me with this print?", "can you help me out with this print?", "print, can you help me with this?", "print, can you help me out with this?", "what's up print?", "print, what's up?" "check this out print", "print, check this out", "can you listen to this print?", "print, can you listen to this?", "listen to this print", "print, listen to this"]

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def taking_voice_commands():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "print" in command: # print() being the name of this AI (Note: should progamme AI with the abililty to change it's name through user command)
                command = command.replace("print", "")
                #speak(command)
    except:
        pass
    return command

def print_run():
    command = taking_voice_commands()
    print(command)
    if command in wake_commands:
        pass