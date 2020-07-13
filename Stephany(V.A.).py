import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import random

webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Stephanie Sir. Please tell me how may I help you")       

# def takeCommand():
#     #It takes microphone input from the user and returns string output

#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 1
#         audio = r.listen(source)

#     try:
#         print("Recognizing...")    
#         query = r.recognize_google(audio, language='en-in')
#         print(f"User said: {query}\n")

#     except Exception as e:
#         # print(e)    
#         print("Say that again please...")  
#         return "None"
#     return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        # query = takeCommand().lower() 
        query = input().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open' in query and 'in browser' in query:
            query = query.replace('open ','')
            query = query.replace(' in browser','')
            webbrowser.get('chrome').open(f"{query}.com")

        elif 'open' in query and '.' in query:
            query = query.replace('open ','')
            webbrowser.get('chrome').open(f"{query}")

        elif 'google search' in query:
            speak('Searching')
            webbrowser.get('chrome').open(f"https://www.google.com/search?q={query.replace('google search ','')}")

        elif 'search song' in query:
            query = '%20'.join(query.replace('search song ','').split(' '))
            c = ['Okay! nice one','oh! i love this song','oh! cool','yeah this song is amazing','nice pick']
            speak(random.choice(c))
            webbrowser.get('chrome').open(f"https://soundcloud.com/search?q={query}")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to ' in query:
            query = query.replace('email to ','')
            try:
                speak("What should I say?")
                content = takeCommand()
                to = f"{query}@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")

        elif 'bye' in query:
            speak(random.choice(['Okay sir! we will meet later','Ok bye sir! you are awsome','see you soon sir, i think i should charge myself now','you are amazing nie talking to you Bye!']))
            break