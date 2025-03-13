import datetime
import os
import openai
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser

from config import apikey

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def ai(prompt):
    openai.api_key = apikey
    text=f"OpenAi response for Prompt:{prompt}\n***********************\n\n"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if os.path.exists("openai"):
        os.mkdir("openai")

    with open(f"Openai/{prompt[0:10]}.txt", "w") as f:
        f.write(text)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 6 <= hour < 12:
        speak("Good Morning sir")
    elif 12 <= hour < 4:
        speak("Good AfterNoon sir")
    elif 4 <= hour < 8:
        speak("Good Evening sir")
    else:
        speak("Good Night sir")

    speak(" Please  tell  me  how  can  I   help  you")

def commandment():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source,0,6)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:,{query}\n")

    except Exception as e:
        # print(e)
        speak("Say that again please sir..")
        return "None"
    return query


speak("Hello sir I  am  Lucifer")
wishMe()
def sendEmail(to, content):
    pass
class Exceptions:
    pass

while True:
    query = commandment().lower()
    if 'wikipedia' in query:
        speak("Searching Wikipedia..")
        query = query.replace("Wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)

    elif 'go to sleep' in query:
        speak("ok sir , You can call me any time")
        break

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        webbrowser.open("google.com")

    elif 'open pycharm' in query:
        psychopath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2023.2.3\\bin\\pycharm64.exe"
        os.startfile(psychopath)

    elif 'the time' in query:
        strfTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir the time is {strfTime}")

    elif 'open code' in query:
        codePath = "C:\\Users\\91990\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)

    elif 'stackoverflow' in query:
        webbrowser.open("stackoverflow.com")

    elif 'send email' in query:
        try:
            speak("What should I say?")
            content = commandment()
            to = "adityaadarsh3167@gmail.com"
            sendEmail(to)
            speak("Email has been sent!")
        except Exceptions as e:
            print(e)
            speak("Sorry sir email can't be sent now")

    elif 'Using Artificial Intelligent' in query:
        ai(prompt=query)


