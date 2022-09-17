from logging import exception
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[0].id)

# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# To convert voice to text
def takecommand(): 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=2,phrase_time_limit=5)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")

        except Exception as e:
            speak("Say that again please...")
            return "none"
        return query

# To wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Welcome Sir, My name is Jarvis. Please tell me how can i help you.")

# To send Email
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('shivendra1114@gmail.com', 'ShadowMonarch')
    server.sendEmail('shivendra1114@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wish()
    # while True:
    if 1:

        query = takecommand().lower()

        # Logic building for tasks

        if "open notepad" in query:
            npath = "C:\\Windows\\notepad.exe"
            os.startfile(npath)
        
        elif "open adobe reader" in query:
            apath = "C:\\Program Files\\Adobe\\Acrobat DC\\Acrobat\\Acrobat.exe"
            os.startfile(apath)

        elif "open command prompt" in query:
            os.system("start cmd")
         
        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow("webcam", img)
                k = cv2.waitKey(50)
                if k==27:
                    break
            cap.release()
            cv2.destroyAllWindows()
        
        elif "play music" in query:
            music_dir = "C:\\music"
            songs = os.listdir(music_dir)
            # rd = random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, songs[0]))


        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

        elif "wikipedia" in query:
            speak('what should i search on wikipedia?')

            speak('searching wikipedia....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=1)
            speak('according to wikipedia')
            speak(results)
            # print(results)
        
        elif "open youtube" in query:
            webbrowser.open('www.youtube.com')
        
        elif "open discord" in query:
            webbrowser.open('www.discord.com')
        
        elif "open stackoverflow" in query:
            webbrowser.open('www.stackoverflow.com')
        
        elif "open google" in query:
            speak('sir, what should i search on google')
            cm = takecommand().lower()
            webbrowser.open(f'{cm}')

        elif "send message" in query:
            kit.sendwhatmsg('+916204137813','hello',2,38)  #If this code is not working write the number with the country code and the message in a string.

        elif "play song on youtube" in query:
            speak('what song should i play sir')
            yo = takecommand().lower()
            kit.playonyt(f'{yo}')

        elif "send email" in query:
            try:
                speak('what should i say?')
                content = takecommand().lower()
                to = 'pramila5981@gmail.com'
                sendEmail(to,content)
                speak('email has been sent.')

            except Exception as e:
                print(e)
                speak('sorry sir, I am not able to sent this email.')

        elif "no thanks" in query:
            speak('thanks for using me sir, have a good day.')
            sys.exit()
