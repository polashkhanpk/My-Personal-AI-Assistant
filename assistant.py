import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import datetime
import pyautogui

engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 185)
engine.setProperty('volume', 1.0)

DESKTOP_PATH = r"C:\Users\shiha\OneDrive\Desktop"
DOWNLOADS_PATH = r"D:\Downloads"
DOCUMENTS_PATH = r"C:\Users\shiha\Documents"
PICTURES_PATH = r"C:\Users\shiha\Pictures"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    r.pause_threshold = 0.8
    r.dynamic_energy_threshold = True

    with sr.Microphone() as source:
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

# COMMAND

def run_command(command):

    # --- OPEN APPS ---

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

    elif "facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("https://facebook.com")

    elif "notepad" in command:
        speak("Opening Notepad")
        os.system("start notepad")

    elif "calculator" in command or "calc" in command:
        speak("Opening Calculator")
        os.system("start calc")

    elif "file explorer" in command:
        speak("Opening File Explorer")
        os.system("explorer")

    # --- FOLDERS ---

    elif "desktop" in command:
        speak("Opening desktop")
        os.startfile(DESKTOP_PATH)

    elif "download" in command:
        speak("Opening downloads")
        os.startfile(DOWNLOADS_PATH)

    elif "documents" in command:
        speak("Opening documents")
        os.startfile(DOCUMENTS_PATH)

    elif "pictures" in command:
        speak("Opening pictures")
        os.startfile(PICTURES_PATH)

    # --- CREATE FOLDER ---

    elif "create folder" in command:
        folder_name = "New Folder"
        path = os.path.join(DESKTOP_PATH, folder_name)

        count = 1
        while os.path.exists(path):
            path = os.path.join(DESKTOP_PATH, f"New Folder {count}")
            count += 1

        os.mkdir(path)
        speak("Folder created on desktop")

    # --- SCREENSHOT ---

    elif "screenshot" in command:
        speak("Taking screenshot")

        now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"screenshot_{now}.png"

        img = pyautogui.screenshot()
        img.save(filename)

        speak("Screenshot saved")

    # --- VOLUME ---

    elif "volume up" in command:
        pyautogui.press("volumeup")
        speak("Volume increased")

    elif "volume down" in command:
        pyautogui.press("volumedown")
        speak("Volume decreased")

    elif "mute" in command:
        pyautogui.press("volumemute")
        speak("Muted")

    # --- MEDIA ---

    elif "play" in command or "pause" in command:
        pyautogui.press("playpause")

    elif "next" in command:
        pyautogui.press("nexttrack")

    elif "previous" in command:
        pyautogui.press("prevtrack")

    # --- WINDOWS CONTROL ---

    elif "close window" in command:
        pyautogui.hotkey("alt", "f4")

    elif "minimize window" in command:
        pyautogui.hotkey("win", "down")

    elif "maximize window" in command:
        pyautogui.hotkey("win", "up")

    elif "show desktop" in command:
        pyautogui.hotkey("win", "d")

    elif "task manager" in command:
        pyautogui.hotkey("ctrl", "shift", "esc")

    # --- SYSTEM ---

    elif "lock computer" in command:
        os.system("rundll32.exe user32.dll,LockWorkStation")

    elif "sleep computer" in command:
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

    elif "shutdown" in command:
        speak("Shutting down computer")
        os.system("shutdown /s /t 5")

    elif "restart" in command:
        speak("Restarting computer")
        os.system("shutdown /r /t 5")

    # --- TIME ---

    elif "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak("The time is " + now)

    # --- EXIT ---

    elif "exit" in command or "quit" in command:
        speak("Goodbye Shihab")
        exit()

    else:
        speak("I did not understand")


speak("Assistant started")

while True:
    command = listen()
    if command:
        run_command(command)
