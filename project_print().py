import speech_recognition as sr
import pyttsx3
import wikipedia
import pywhatkit
import datetime
import pyjokes
import selenium
import random

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

wake_commands = ["hello print", "are you there print", "print are you there", "ok print", "hey print", "excuse me print", "yo print", "do you have a moment print", "can you help me with this print", "can you help me out with this print", "print, can you help me with this", "print can you help me out with this", "what's up print", "print what's up" "check this out print", "print check this out", "can you listen to this print", "print can you listen to this", "listen to this print", "print listen to this"]

wake_response = ["hello, how may I help you", "hello, what's up", "hi, how can I help you?", "hello, what do you need?"]

unknown_command_response = ["sorry, I did not get that", "sorry, can you repeat that?", "I didn't hear that clearly", "say that again please", "beg your pardon, could you repeat that?", "that was unclear, can you speak more clearly?"]

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
            #if "print" in command: # print() being the name of this AI (Note: should progamme AI with the abililty to change it's name through user command)
                #command = command.replace("print", "")
                #speak(command)
    except:
        pass
    return command

def run_print():
    voice_command = taking_voice_commands()
    print(voice_command)
    if 'google' in voice_command:
        question = voice_command.replace('google', '')
        info = wikipedia.summary(question, 1)
        speak(info)
        print(info)
        
def wake_mode():
    voice_alert = taking_voice_commands()
    print(voice_alert)
    if voice_alert in wake_commands:
        speak(random.choice(wake_response))
        #run_print()
        print("that is all")
    else:
        speak(random.choice(unknown_command_response))
      
        
while True:
    wake_mode()