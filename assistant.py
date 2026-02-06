import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import datetime

# Initialize voice engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    r.energy_threshold = 300
    r.pause_threshold = 0.8

    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source, timeout=5, phrase_time_limit=5)

    try:
        command = r.recognize_google(audio)
        command = command.lower()
        print("Processed:", command)
        return command

    except sr.UnknownValueError:
        return ""

    except sr.RequestError:
        speak("Internet problem")
        return ""

def run_command(command):

    if "chrome" in command:
        speak("Opening Chrome")
        os.system("start chrome")

    elif "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak("The time is " + now)

    elif "exit" in command or "quit" in command:
        speak("Goodbye Shihab")
        exit()

    else:
        speak("I did not understand")

# ----------------- MAIN -----------------

speak("Assistant started")

while True:
    cmd = listen()
    if cmd:
        run_command(cmd)
