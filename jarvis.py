import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

print("Initializing Jarvis")
master="Yashwanth"
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()
speak("Initializing Jarvis...")

    
    
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning" + master)
    elif hour>=12 and hour<18:
        speak("Good Afternoon" + master)
    else:
        speak("Good Evening" + master)
    speak("I am Jarvis. How may I help you?")
def main():
    def takeCommand():
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio=r.listen(source)
        try:
            print("Re-cognizing...")
            query=r.recognize_google(audio, language = 'en-in')
            print(f"user said:{query}\n")
        except Exception as e:
            speak("Can you please say that again " + master)
            query=None
        return query
    wishMe()
    query=takeCommand()
    if 'wikipedia' in query.lower():
        speak('Searching in Wikipedia ' + master)
        query=query.replace("wikipedia","")
        results=wikipedia.summary(query, sentences=2)
        speak(results)
        print(results)
    
    elif 'open youtube' in query.lower():
        speak("Opening Youtube " + master)
        webbrowser.open('https://www.youtube.com/')
    
    elif 'game' in query.lower():
        speak("Opening Tanki Online " + master)
        webbrowser.open('https://tankionline.com/en/')
    
    elif 'music' in query.lower():
        speak("Playing Music" + master)
        songs_dir="C:\songs"
        songs=os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[0]))
    
    elif 'time' in query.lower():
        strTime= datetime.datetime.now().strftime("%H:%M:%S")
        speak(master + "the time is " + strTime)
        print(strTime)
    
    elif 'code' in query.lower():
        speak("Opening the Coding platform " + master)
        webbrowser.open('https://www.codechef.com/users/yashwanth64')
 
main()

