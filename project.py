import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import psutil
import spotipy
import webbrowser
import os
import pyautogui
import time as t
import random
import pyjokes
import wolframalpha
import datetime
from datetime import date, time
import numpy as np
import cv2
import smtplib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pathlib import Path

# spotify addon keys
username = 'n79t9p5qos64sjc422g4jj8sj'
clientID = '537f836f3f1547c0b2f468ab7590ac09'
clientSecret = '57db1d304f53432ab0efd141f15632cb'
redirect_uri = 'http://google.com/callback/'
oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirect_uri)
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
spotifyObject = spotipy.Spotify(auth=token)
user_name = spotifyObject.current_user()

# voice engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# wolframealpha api addon key
client = wolframalpha.Client("JQEETJ-H8GVGQX757")

print('''                      PROJECT REX
              YOUR ARTIFICIAL ASSISTANT  ''')

# speak function


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# authentication user
print("Welcome User! ")
speak(f"Welcome User!")


def check_user():

    speak(f"Please verify your identity to continue. ")
    password = takeCommand()

    if "start" in password:
        speak(f"Access Granted")
        speak(f"""powering up the systems . 
                We well be ready in 3 ; 2 ; 1. All systems are connected ; 
                online ; and working well. We are all set to go""")
    else:
        speak(f"Cannot give my access to you.")
        return check_user()


# startup greetings
def wishMe():
    strTime = datetime.datetime.now().strftime("%I:%M %p")
    today = date.today()

    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 17:
        speak("Good Afternoon!")

    elif hour >= 17 and hour < 19:
        speak("Good Evening!")

    else:
        speak("It seems darker outside!")
    speak(f"Its {today} today;and {strTime} right now")
    speak(" Sir ! What can i do for you?")


# time notify
def notify():
    hour = int(datetime.datetime.now().hour)
    if hour == 0 or hour >= 0 and hour <= 4:
        speak(f"Its too late you should sleep now.")
        if 'yes' in query:
            speak(f"Should i shut down everything? sir!")
            if "close everything" in query:
                speak("Disconnecting everything and Shutting down your device")
                os.system("netsh interface set interface 'Wifi' disabled")
                os.system("shutdown /f /s")
                exit()


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('<your email id>', 'password')
    server.sendmail('<your email id>', to, content)
    server.close()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit=3)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"Command: {query}\n")

    except Exception as e:

        speak("Sorry! i cannot understant you. ")
        return "None"
    return query


if __name__ == "__main__":

    check_user()
    wishMe()
    notify()

    while True:
        query = takeCommand().lower()

        # GOOGLE SEARCH COMMANDS

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            speak(results)

        elif 'write a mail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("whome should i send this mail")
                to = input("Enter mail address:\n")
                sendEmail(to, content)
                speak("Mail has been sent to {to}")

            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        elif 'open youtube' in query:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("Opening youtube for you")

        elif 'open google' in query:
            webbrowser.openopen_new_tab("google.com")
            speak("Opening google for you")

        elif 'open my mail' in query:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail is opening now")

        elif 'song from youtube' in query:
            speak("what should i search on youtube")
            search = takeCommand()
            speak("Searched."+search+"on youtube and i found this")
            yt_url = "https://www.youtube.com/results?search_query=" + search
            webbrowser.open_new_tab(yt_url)

        elif 'who are you' in query:
            speak(f"hello! i am an Artificial Assistant `. I am designed to take care of your daily tasks.  What do you want to know about me ?  ")

        elif 'what can you do' in query:
            speak(f'''I can do a lot of things, some of them includes  :
                      Can play music for you and even make you laugh with my jokes.
                      Can open any application if you want and sometimes can take ur important notes and pictures .
                      Can open your mail and even send one if you want.
                      Can help you in controlling your device with your voice commands.
                      and last but not the least i can help in solving your maths problems.''')

        elif 'who is your creator' in query:
            speak(
                f"I am developed by a freak protagonist Udit aka Rex_codes. Anything else, Sir?")

        elif 'how are you ' in query:
            speak(
                f"i am fine sir. Was just thinking of you and u came. How was your day? ")

        elif 'see you later' in query:
            speak(
                f"As you wish Sir! turning down all my systems in 3 ; 2 ; 1. Should i log off your account too?")
            query = takeCommand()
            if "yes" in query:
                check_user()
            if "no" in query:
                speak(
                    f"As you wish sir. I am just a call away , You can call me anytime if you need ")
                exit()

        elif 'do you have friends' in query:
            speak(
                f"Yes i have a few friends. Will you be my friend? we will have a lot of fun together.")
        elif 'yes' in query:
            speak(f'amazing! its great to have you my friend.')

        elif 'what is your name' in query:
            speak(f"did i forget to introduce my self? hi! i am Rex")

        elif 'tell me a joke' in query:
            a = pyjokes.get_joke()
            speak(f"yes sir! why not. What about this one?")
            speak(a)

        elif 'that was not funny' in query:
            speak(f"I have another one for you")
            a = pyjokes.get_joke()
            speak(a)

        elif "go to sleep" in query:
            speak("Shutting down your device")
            os.system("shutdown /f /s")
            exit()

        elif "log out my device" in query:
            speak("logging down your device")
            os.system("shutdown /f /l")

        elif "let my device sleep" in query:
            speak("Hibernating your device")
            os.system("shutdown /f /h")
            exit()

        elif "abort shut down " in query:
            speak("Aborting shutdown procedure")
            os.system("shutdown /a")

        elif "battery status" in query:
            battery_data = psutil.sensors_battery()
            a = "Battery left : {}%".format(battery_data.percent)
            speak(a)
            if battery_data.power_plugged:
                b = "Charger is connected."
                speak(b)
            else:
                speak('Standby time left : {}'.format(
                    datetime.timedelta(seconds=battery_data.secsleft)))

        elif "screenshot" in query:
            name = random.randint(0, 100)
            image = pyautogui.screenshot('image'+str(name)+'.png')
            speak("Screenshot saved ")

        elif "write a note" in query:
            speak("What should i write in it?")
            note = takeCommand()
            file = open('rex.txt', 'w')
            speak("adding date and time in it ?")
            strTime = datetime.datetime.now().strftime("%I:%M %p")
            file.write(strTime)
            file.write(" :- ")
            file.write(note)

        elif "show note" in query:
            i = 1
            speak("Showing Notes")
            file = open("rex.txt", "r")
            i = i+1
            print(file.read())
            speak(file.read(6))

        elif 'tell the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"Sir, its {strTime} right now")

        elif "tell me" in query:
            query = takeCommand()
            res = client.query(query)
            output = next(res.results).text
            print(output)
            speak(output)

        elif "thanks" in query:
            speak(f"I am glad to answer all your questions. Anything else ? sir!")

        elif 'open code' in query:
            path = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
        elif 'open chrome' in query:
            path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(path)
        elif 'open game mode' in query:
            path = "D:\\Games\\"
            os.startfile(path)

        elif 'music' in query:
            speak("Music mode on")
            speak(" Search for a song")
            speak(" Exit music player ")
            speak("Enter Your Choice: ")
            user_input = takeCommand().lower()
            if user_input == 'Play':
                speak("What should i play for you today: ")
                search_song = takeCommand()
                results = spotifyObject.search(search_song, 1, 0, "track")
                songs_dict = results['tracks']
                song_items = songs_dict['items']
                song = song_items[0]['external_urls']['spotify']
                webbrowser.open(song)
                speak('Song has opened in your browser.')
            elif user_input == '0':
                speak("Good Bye, Have a great day!")
                break
            else:
                speak("Please enter valid user-input.")
