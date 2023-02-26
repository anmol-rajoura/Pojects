from platform import win32_is_iot
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import pywhatkit as kit
import cv2
# from wikipedia.wikipedia import random
from requests import get
import sys
import pyautogui
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 185)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("hello sir I am jarvis your assistant. Please tell me how may I help you")
    # speak("mai hoon om")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        # speak("say that again please....")
        return "None"
    query = query.lower()
    return query


# if __name__ == "__main__":
#     wishMe()
names=["Sanjeev", "Himanshu", "Pawan", "Sumit", "Devdutt","Anmol"]

def TaskExe():
    wishMe()

    while True:                                                  

        # if 1:

        query = takeCommand()

      # Logic for executing tasks based on query
      
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'who are you' in query or 'what can you do' in query:
            speak('I am Friday version 1 point O your personal assistant. I am programmed to do minor tasks like'
                  'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather exsectra')
            break
        elif ' ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f"your ip address is {ip}")

        elif 'open command prompt' in query:
            os.system("start cmd")

        elif 'open camera' in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break
            cap.release()
            cv2.destroyAllWindows()


        elif 'switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")   
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'on youtube' in query:
            speak('ok sir')
            query = query.replace("jarvis", "")
            query = query.replace("on youtube", "")
            web = 'https://www.youtube.com/results?search_query=' + query
            kit.playonyt(web)

        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'search google' in query:
            speak('ok sir')
            query = query.replace("jarvis","")
            query = query.replace("search google","")
            kit.search(query)

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'shutdown' in query:
            print('shutingdown. thank you')
            speak('shutingdown. thank you')
            r = kit.shutdown(time=180)

        elif 'stop shutting down' in query:
            print('ok canceling')
            speak('ok canceling')
            r = kit.cancel_shutdown()

        elif 'play music' in query:
            music_dir = 'C:\\songs'
            songs = os.listdir(music_dir)
            # rd = random.choice(songs)
            # print(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M %p")
            print(strTime)
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = 'C:\\Users\\anmol\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(codePath)

        elif 'quit' in query or 'bye' in query:
            speak("quiting sir. thanks for your time. have a nice day ahead")
            sys.exit()

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
        
        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Anmol.")
        
        elif "where is" in query:
            query = query.replace("where is jarvis", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")
        # # elif 'anjali' in query:






        # #     speak("hello anjali. i hope you doing good")

        elif 'tell me about myself' in query:
            speak('tell me your name')
            name = takeCommand()
            speak(f"hey how are you{name}")
            if name==names:
                speak("Hello sir, i wish you doing good")
          
            

if __name__ == "__main__":
    # TaskExe()
    while True:
        Permission = takeCommand()
        if 'wake up' in Permission:
            TaskExe()
        elif 'goodbye' in Permission:
            sys.exit()
            