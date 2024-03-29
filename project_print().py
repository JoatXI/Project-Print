import speech_recognition as sr
import pyttsx3
import wikipedia
import pywhatkit
import datetime
import pyjokes
import random
import webbrowser
import time
import pyautogui

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

wake_commands = ["hello print", "are you there print", "print are you there", "ok print", "hey print", "excuse me print", "yo print", "do you have a moment print", "can you help me with this print", "can you help me out with this print", "print can you help me with this", "print can you help me out with this", "what's up print", "print what's up" "check this out print", "print check this out", "can you listen to this print", "print can you listen to this", "listen to this print", "print listen to this", "wake up print", "print, wake up"]

wake_response = ["hello, how may I help you", "hello, what's up", "hi, how can I help you?", "hello, what do you need?", "hey, what can I do for you?"]

unknown_command_response = ["sorry, I did not get that", "sorry, can you repeat that?", "I didn't hear that clearly", "say that again please", "beg your pardon, could you repeat that?", "that was unclear, can you speak more clearly?"]

search_queries = ["who is", "tell me about", "what do you know about", "who the hell is", "do a search on"]

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def taking_voice_commands():
    try:
        with sr.Microphone() as source:
            print("listening...")
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source, timeout=60)
            command = listener.recognize_google(voice)
            command = command.lower()
# print() being the name of this AI (Note: should progamme AI with the abililty to change it's name through user command)
    except:
        pass
        return None
    else:
        return command

def run_print():
    voice_command = taking_voice_commands()
    print(voice_command)
    if 'google' in voice_command:
        question = voice_command.replace('google', '')
        info = wikipedia.summary(question, 1)
        print(info)
        speak(info)
    elif "play" in voice_command:
        sound = voice_command.replace('play', '')
        speak('playing' + sound)
        pywhatkit.playonyt(sound)
    elif 'time' in voice_command:
        time = datetime.datetime.now().strftime('%H:%M')
        speak("The time is" + time)
    elif 'joke' in voice_command:
        speak(pyjokes.get_joke())
    elif search_queries in voice_command:
        search = voice_command.replace(search_queries, '')
        webbrowser.open('https://www.google.com/search?q=' + search)
    else:
        speak(random.choice(unknown_command_response))
        
def wake_mode():
    try:
        with sr.Microphone() as voice_source:
            print("listening in wake mode...")
            listener.adjust_for_ambient_noise(voice_source)
            voice = listener.listen(voice_source, phrase_time_limit=3)
            alert_command = listener.recognize_google(voice)
            alert_command = alert_command.lower()

            if alert_command in wake_commands:
                print(alert_command)
                speak(random.choice(wake_response))
                while True:
                    run_print()
    except:
        pass
        return None
    else:
        return alert_command
      
        
while True:
    wake_mode()