import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime 
import os 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    strTime = datetime.datetime.now().strftime("%I:%M %p")  
    today = datetime.date.today()
    
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<17:
        speak("Good Afternoon!")   

    elif hour>=17 and hour<19:
        speak("Good Evening!")
        
    else:
        speak("It seems darker outside!")     
    speak(f"Its {today} today;and {strTime} right now")
    speak(" Sir ! What can i do for you?")     

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
    

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source)

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