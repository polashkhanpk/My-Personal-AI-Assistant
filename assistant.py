import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import datetime
import pyautogui
import time

# ------------- VOICE SETUP -------------

engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 185)
engine.setProperty('volume', 1.0)

# Paths
DESKTOP_PATH = r"C:\Users\shiha\OneDrive\Desktop"
DOWNLOADS_PATH = r"D:\Downloads"
DOCUMENTS_PATH = r"C:\Users\shiha\Documents"
PICTURES_PATH = r"C:\Users\shiha\Pictures"

WAKE_WORD = "friday"

# ------------- FUNCTIONS -------------

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen(timeout=None):
    r = sr.Recognizer()
    r.pause_threshold = 0.8
    r.dynamic_energy_threshold = True

    with sr.Microphone() as source:
        if timeout:
            audio = r.listen(source, timeout=timeout, phrase_time_limit=5)
        else:
            print("Listening...")
            r.adjust_for_ambient_noise(source, duration=0.8)
            audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        text = text.lower()
        print("Heard:", text)
        return text
    except:
        return ""

# ------------- COMMAND HANDLER -------------

def run_command(command):

    if "chrome" in command:
        speak("Opening Chrome")
        os.system("start chrome")

    elif "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "google" in command:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif "gmail" in command:
        speak("Opening Gmail")
        webbrowser.open("https://mail.google.com")

    elif "notepad" in command:
        speak("Opening Notepad")
        os.system("start notepad")

    elif "calculator" in command or "calc" in command:
        speak("Opening Calculator")
        os.system("start calc")

    elif "file explorer" in command:
        os.system("explorer")

    elif "desktop" in command:
        os.startfile(DESKTOP_PATH)

    elif "download" in command:
        os.startfile(DOWNLOADS_PATH)

    elif "documents" in command:
        os.startfile(DOCUMENTS_PATH)

    elif "pictures" in command:
        os.startfile(PICTURES_PATH)

    elif "screenshot" in command:
        speak("Taking screenshot")

        now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"screenshot_{now}.png"

        img = pyautogui.screenshot()
        img.save(filename)

        speak("Screenshot saved")

    elif "volume up" in command:
        pyautogui.press("volumeup")

    elif "volume down" in command:
        pyautogui.press("volumedown")

    elif "mute" in command:
        pyautogui.press("volumemute")

    elif "close window" in command:
        pyautogui.hotkey("alt", "f4")

    elif "show desktop" in command:
        pyautogui.hotkey("win", "d")

    elif "task manager" in command:
        pyautogui.hotkey("ctrl", "shift", "esc")

    elif "lock computer" in command:
        os.system("rundll32.exe user32.dll,LockWorkStation")

    elif "shutdown" in command:
        speak("Shutting down computer")
        os.system("shutdown /s /t 5")

    elif "restart" in command:
        speak("Restarting computer")
        os.system("shutdown /r /t 5")

    elif "exit" in command or "quit" in command:
        speak("Goodbye Shihab")
        exit()

        # -------- AUTOMATION MODES --------

    elif "work mode" in command:
        speak("Starting work mode")
        os.system("start chrome")
        os.system("explorer")
        os.startfile(DOCUMENTS_PATH)

    elif "study mode" in command:
        speak("Starting study mode")
        webbrowser.open("https://youtube.com")
        os.system("start notepad")

    elif "fun mode" in command:
        speak("Starting fun mode")
        webbrowser.open("https://youtube.com")
        os.system("start chrome")


    else:
        speak("I did not understand")

# ------------- MAIN LOOP -------------

speak("Say Friday to wake me.")

while True:

    # Always listen for wake word
    heard = listen()

    if WAKE_WORD in heard:
        speak("Yes Shihab, I'm listening")

        # Listen for actual command
        command = listen()

        if command:
            run_command(command)

        time.sleep(1)   # small pause before sleeping again
