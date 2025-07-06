import pyttsx3 #pip install pyttsx3 == text to speech
import datetime
#import pyaudio
import speech_recognition as sr


engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)

def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon") 
    elif hour >= 18 and hour <24:
        speak("Good Evening")
    else:
        speak("Good Night")           

def wishme():
    speak("welcome")
    time()
    date()
    greeting()
    speak("how can i help you")

def takeCommandCMD():
    query = input("please tell me how can i help you?\n")
    return query    

def takeCommandMIC():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language ="en-IN")
        print("User said : "+ query)


    except Exception as e:
        print(e) 
        speak("Say that again please....")
        return("None")    
    return query
   
if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommandMIC().lower()
        if 'time' in query:
            time()
        elif 'date' in query:
            date()     
