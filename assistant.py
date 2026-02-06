import speech_recognition as sr
import pyttsx3
import os
import webbrowser

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except:
        return ""

def run_command(command):

    if "open chrome" in command:
        speak("Opening Chrome")
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "time" in command:
        import datetime
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak("The time is " + time)

    elif "exit" in command:
        speak("Goodbye Shihab")
        exit()

    else:
        speak("I did not understand")

# main loop
speak("Assistant started")

while True:
    cmd = listen()
    run_command(cmd)

