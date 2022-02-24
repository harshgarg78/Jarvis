from http import server
from msilib.schema import tables
from typing import Mapping
from unittest import result
from urllib.parse import quote_from_bytes
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
from requests import get
import random
import pywhatkit as kit
import socket
import pyjokes
import pyautogui
from PyDictionary import PyDictionary as Diction
socket.getaddrinfo('localhost', 8080)
# import pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)

    if hour>=6 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good evening")
    
    speak("I am jarvis Sir. Please tell me how may i help you")

def takecommand():
    # it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
        speak(query)

    except Exception as e:
        # print(e)
        print("Say that again please....")
        speak("Say that again please")
        return "None"
    return query

def Dict():
    speak("Activated Dictionary")
    speak("Tell me the problem")
    prob = takecommand()

    if 'meaning' in prob:
        speak("speak the word for which you want meaning")
        prob = takecommand()
        result = Diction.meaning(prob)
        print(result)
        speak(f"the meaning of {prob} is {result}")

    elif 'synonym' in prob:
        speak("speak the word for which you want synonym")
        prob = takecommand()
        result = Diction.synonym(prob)
        speak(f"the synonym of {prob} is {result}")

    elif 'antonym' in prob:
        speak("speak the word for which you want antonym")
        prob = takecommand()
        result = Diction.antonym(prob)
        speak(f"the antonym of {prob} is {result}")

    speak("Dictionary exited")

def sendEmail(to,content):
    server = smtplib.SMTP('smtp@gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('harshkaku78@gmail.com','harshgarg1A@')
    server.sendmail('harshkaku78@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()

        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia... ")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences = 1)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("Youtube.com")

        elif 'open google' in query:
            speak("sir what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'send message' in query:
            kit.sendwhatmsg("+917988384689","hyy harsh garg",14,24)

        elif 'play music' in query:
            music_dir='D:\\songs\\audio song'
            songs = os.listdir(music_dir)
            r = random.randint(1,50)
            os.startfile(os.path.join(music_dir,songs[r]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open vs code' in query:
            codePath = "C:\\Users\\harsh\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'screenshot' in query:
            speak("tell the name of file")
            path = takecommand()
            pathname = path + ".png"
            path1 = "C:\\Users\harsh\\Desktop\\3 sem\\project\\" + pathname
            kk = pyautogui.screenshot()
            kk.save(path1)
            speak("screenshot has been taken")

        elif 'joke' in query:
            get = pyjokes.get_joke()
            speak(get)
        
        elif 'my location' in query:
            webbrowser.open('https://www.google.com/maps/place/Bahal,+Haryana+127028/@28.6281129,75.6105709,15z/data=!3m1!4b1!4m5!3m4!1s0x3913074cf2a6cf59:0x5576097c222813b3!8m2!3d28.6296193!4d75.6178991')

        elif 'email to harsh' in query:
            try:
                speak("What should I say?")
                content = takecommand().lower()
                to = "harshkaku78@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry")

        elif 'open jc bose' in query:
            webbrowser.open("jcboseust.ac.in")

        elif 'who developed you' in query:
            speak("Mr. harsh garg and Mr. mayank")

        elif 'what is your name' in query:
            speak("jarvis")

        elif 'dictionary' in query:
            Dict()

        elif 'quit' in query:
            exit()


