import pyttsx3 as p
import speech_recognition as sr
from selenium_web import *
from YT_auto import *
from News import *
import randfacts
from jokes import *
from Weather import *
import datetime

#  conda install conda=23.11.0
engine=p.init()

rate=engine.getProperty('rate')
engine.setProperty('rate',210)
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
print(voices)

def speak(text):
    engine.say(text)
    engine.runAndWait()

today_date=datetime.datetime.now()
r=sr.Recognizer()

speak("Hello there, i'm your voice assistant.")
speak("Today is "+ str(today_date.strftime()))
speak("Temperature at you place is "+ str(temp())+" degrees celsius "+" and with "+ str(des()) ) 
speak("What can i do for you? ")

with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    audio=r.listen(source)
    text=r.recognize_google(audio)
    print(text)

if "what" and "about" and "you" or "How" and "are" and "you" in text:
    speak("I'm having a good day, sir")

    with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print("Listening..")
        audio=r.listen(source)
        text=r.recognize_google(audio)

if "information" in text2:
    speak("you need information related to which field?")
    
    with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print("Listening..")
        audio=r.listen(source)
        infor=r.recognize_google(audio)

    speak("searching {} in wikipedia".format(infor))
    print("searching {} in wikipedia".format(infor))
    assist = infow()
    assist.get_info(infor)

elif "play" and "video" in text2:
    speak("You want to play which video?")
    with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print("Listening..")
        audio=r.listen(source)
        vid=r.recognize_google(audio)
        print("Playing {} on youtube".format(vid))
        assist=music()
        assist.play()

elif "News" in text2:
    print("Sure, lets read some news.")
    speak("Sure, lets read some news.")

    arr=news()
    for i in range(len(arr)):
        print(arr[i])
        speak(arr[i])

elif "fact" or "facts" in text2:
    speak("Sure sir, ")
    x=randfacts.getFact()
    print(x)
    speak("Did you know that, "+x)

elif "joke" or "jokes" in text2:
    speak("Sure, get ready for some chukkles")
    arr=joke()
    print(arr[0])
    speak(arr[0])
    print(arr[1])
    speak(arr[1])
