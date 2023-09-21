import json
import spotipy
import webbrowser
import speech_recognition as sr
import pyttsx3
import datetime
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

username = 'n79t9p5qos64sjc422g4jj8sj'
clientID = '537f836f3f1547c0b2f468ab7590ac09'
clientSecret = '57db1d304f53432ab0efd141f15632cb'
redirect_uri = 'http://google.com/callback/'
oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirect_uri)
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
spotifyObject = spotipy.Spotify(auth=token)
user_name = spotifyObject.current_user()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
# To print the JSON response from
# browser in a readable format.
# optional can be removed
# print(json.dumps(user_name, sort_keys=True, indent=4))
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
        speak(f"Turning off the system ")
        exit()
        # return check_user()

def wishMe():
    strTime = datetime.datetime.now().strftime("%I:%M %p")
    today = datetime.date.today()

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
    # speak(" Sir ! What can i do for you?")
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        # r.pause_threshold = 1
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
while True:
	speak("0 - Exit music player ")
	speak("1 - Search for a song")
	speak("Enter Your Choice: ")
	user_input = takeCommand().lower()
	if user_input == 'search':
		speak("Enter the song name: ")
		search_song = takeCommand()
		results = spotifyObject.search(search_song, 1, 0, "track")
		songs_dict = results['tracks']
		song_items = songs_dict['items']
		song = song_items[0]['external_urls']['spotify']
		webbrowser.open(song)
		speak('Song has opened in your browser.')
	elif user_input == 'exit':
		speak("Good Bye, Have a great day!")
		break
	else:
		speak("Please give valid user-input.")
