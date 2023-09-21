import pyttsx3 
import speech_recognition as sr 
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
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
    speak(" Sir ! What have to be sent today?")       

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 0.5
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
    
    wishMe()
        
    while True:
        speak("Ready for your commands . ")
        query = takeCommand().lower()

        if 'mail' in query:
            from_addr='Harpreet '
            to_addr=['uditshuklaking@gmail.com']  
            msg=MIMEMultipart()
            msg['From']=from_addr
            msg['To']=" ,".join(to_addr)
            msg['subject']='just to check'
            speak("Please tell what is to be written in the mail ? ")
            body=takeCommand().lower()

            msg.attach(MIMEText(body,'plain'))

            email='harpreet930kaur@gmail.com'
            password='Harpreet100@'

            mail=smtplib.SMTP('smtp.gmail.com',587)
            mail.ehlo()
            mail.starttls()
            mail.login(email,password)
            text=msg.as_string()
            mail.sendmail(from_addr,to_addr,text)
            speak("Your mail send successfully!!")
            print("Your mail send successfully!!")
            mail.quit()

        elif 'thank you ' in query:
                exit()
        else :
            exit()        
