# ================= IMPORTS =================
import os, sys, time, json, datetime, threading, webbrowser, requests, urllib.parse, subprocess, re, math
import numpy as np
import pyttsx3, speech_recognition as sr, wikipedia, pywhatkit, pyautogui
import cv2, pytesseract
from twilio.rest import Client
import geocoder

# ================= CONFIG =================
MODEL_NAME = "phi"
OLLAMA_URL = "http://localhost:11434"
DATA_FILE = "memory.json"
DEBUG = True

# ===== SAFETY =====
TWILIO_SID = ""
TWILIO_AUTH = ""
TWILIO_FROM = ""
EMERGENCY_CONTACT = "+911234567890"

# ===== ACCESSIBILITY =====
LAST_ACTIVITY = time.time()

# ===== POMODORO =====
POMODORO_ACTIVE = False

# ===== AUDIO =====
LAST_AUDIO_FEATURE = {"energy":0,"zcr":0}

# ================= DEBUG =================
def debug(msg):
    if DEBUG:
        print("[DEBUG]", msg)

# ================= MEMORY =================
DEFAULT_MEMORY = {
    "history": [],
    "notes": [],
    "learned": {},
    "tasks": [],
    "usage_stats": {},
    "learning_model": {},
    "safety_log": []
}

def load_memory():
    if not os.path.exists(DATA_FILE):
        json.dump(DEFAULT_MEMORY, open(DATA_FILE, "w"), indent=2)
        return DEFAULT_MEMORY.copy()

    try:
        mem = json.load(open(DATA_FILE))
        for k in DEFAULT_MEMORY:
            if k not in mem:
                mem[k] = DEFAULT_MEMORY[k]
        return mem
    except:
        return DEFAULT_MEMORY.copy()

def save_memory():
    json.dump(MEMORY, open(DATA_FILE, "w"), indent=2)

MEMORY = load_memory()

# ================= SPEECH =================
engine = pyttsx3.init()
engine.setProperty('rate', 175)
speech_lock = threading.Lock()

def speak(text):
    def run():
        print("ACHARYA:", text)
        try:
            with speech_lock:
                engine.say(text)
                engine.runAndWait()
        except:
            pass
    threading.Thread(target=run).start()

# ================= AUDIO FEATURES =================
def extract_audio_features(audio_bytes):
    try:
        audio = np.frombuffer(audio_bytes, dtype=np.int16).astype(np.float32)
        if len(audio) == 0:
            return {"energy":0,"zcr":0}

        energy = float(np.sqrt(np.mean(audio**2)) / (2**15))
        signs = np.sign(audio)
        zcr = float(np.mean(np.abs(np.diff(signs))) / 2.0)

        return {"energy":energy,"zcr":zcr}
    except:
        return {"energy":0,"zcr":0}

# ================= LISTEN =================
recognizer = sr.Recognizer()

def listen():
    global LAST_AUDIO_FEATURE

    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=5)

            raw = audio.get_raw_data(convert_rate=16000, convert_width=2)
            LAST_AUDIO_FEATURE = extract_audio_features(raw)

            return recognizer.recognize_google(audio).lower()
    except:
        return input("YOU: ").lower()

# ================= DISTRESS =================
DISTRESS_WORDS = ["help","save me","danger","emergency","pain"]

def is_distress(text):
    score = 0

    if any(w in text for w in DISTRESS_WORDS):
        score += 0.7

    score += min(LAST_AUDIO_FEATURE["energy"] * 1.2, 0.2)
    score += min(LAST_AUDIO_FEATURE["zcr"] * 0.5, 0.1)

    debug(f"Distress score: {score}")
    return score > 0.75

# ================= OLLAMA =================
def is_ollama_running():
    try:
        return requests.get(f"{OLLAMA_URL}/api/tags").status_code == 200
    except:
        return False

def start_ollama():
    subprocess.Popen(["ollama", "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(4)

def ensure_model():
    try:
        r = requests.get(f"{OLLAMA_URL}/api/tags")
        models = [m["name"] for m in r.json().get("models", [])]
        if not any(MODEL_NAME in m for m in models):
            subprocess.run(["ollama", "pull", MODEL_NAME])
    except:
        pass

def init_ai():
    if not is_ollama_running():
        start_ollama()

    for _ in range(5):
        if is_ollama_running():
            ensure_model()
            return True
        time.sleep(2)
    return False

def ask_ai(prompt):
    try:
        response = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={"model": MODEL_NAME, "prompt": f"Answer briefly: {prompt}", "stream": False},
            timeout=15
        )
        return response.json().get("response", "")
    except:
        return None

# ================= SAFETY =================
def get_location():
    try:
        g = geocoder.ip('me')
        if g.ok:
            return f"https://maps.google.com/?q={g.latlng[0]},{g.latlng[1]}"
    except:
        pass
    return "Location unavailable"

def send_alert(msg):
    if not TWILIO_SID:
        print("[SIM ALERT]:", msg)
        return

    try:
        client = Client(TWILIO_SID, TWILIO_AUTH)
        client.messages.create(body=msg, from_=TWILIO_FROM, to=EMERGENCY_CONTACT)
    except Exception as e:
        print(e)

def trigger_safety(cmd):
    msg = f"EMERGENCY: {cmd} {get_location()}"
    speak("Emergency detected")

    send_alert(msg)
    MEMORY["safety_log"].append(msg)
    save_memory()

# ================= NOTES =================
def add_note(text):
    MEMORY["notes"].append({"text":text,"time":str(datetime.datetime.now())})
    save_memory()
    speak("Note saved")

def list_notes():
    for n in MEMORY["notes"][-5:]:
        speak(n["text"])

# ================= TASK =================
def add_task(task):
    MEMORY["tasks"].append({"task":task,"done":False})
    save_memory()
    speak("Task added")

def list_tasks():
    for t in MEMORY["tasks"]:
        speak(t["task"])

# ================= POMODORO =================
def start_pomodoro():
    global POMODORO_ACTIVE

    if POMODORO_ACTIVE:
        speak("Already running")
        return

    POMODORO_ACTIVE = True
    speak("Focus started for 25 minutes")

    def run():
        global POMODORO_ACTIVE
        time.sleep(1500)
        speak("Time up")
        POMODORO_ACTIVE = False

    threading.Thread(target=run).start()

# ================= VISION =================
def capture_frame():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()
    return frame if ret else None

def vision():
    frame = capture_frame()
    if frame is None:
        speak("Camera error")
        return

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    brightness = np.mean(gray)

    speak("Bright environment" if brightness > 100 else "Dark environment")

def read_text():
    frame = capture_frame()
    if frame is None:
        speak("Camera error")
        return

    text = pytesseract.image_to_string(frame)
    speak(text[:100] if text.strip() else "No text found")

# ================= MEMORY =================
def learn(key,value):
    MEMORY["learned"][key] = value
    save_memory()

def recall(query):
    for k,v in MEMORY["learned"].items():
        if query in k:
            return v

# ================= WEB =================
def open_google(q):
    webbrowser.open("https://www.google.com/search?q="+urllib.parse.quote(q))

def open_youtube(q):
    webbrowser.open("https://www.youtube.com/results?search_query="+urllib.parse.quote(q))

def play_youtube(q):
    pywhatkit.playonyt(q)

# ================= INTENT =================
def detect_intent(t):
    if "exit" in t: return "EXIT"
    if "note" in t: return "NOTE"
    if "task" in t: return "TASK"
    if "pomodoro" in t: return "POMODORO"
    if "play" in t: return "PLAY"
    if "youtube" in t: return "YOUTUBE"
    if "search" in t: return "GOOGLE"
    if "open" in t: return "SYSTEM"
    if "type" in t: return "TYPE"
    if "see" in t: return "VISION"
    if "read" in t: return "OCR"
    return "AI"

# ================= PROCESS =================
def process(cmd):
    global LAST_ACTIVITY
    LAST_ACTIVITY = time.time()

    MEMORY["history"].append({"cmd":cmd,"time":str(datetime.datetime.now())})
    MEMORY["history"]=MEMORY["history"][-50:]
    save_memory()

    if is_distress(cmd):
        trigger_safety(cmd)
        return

    intent = detect_intent(cmd)

    if intent=="EXIT":
        speak("Goodbye")
        sys.exit()

    if intent=="NOTE":
        speak("What to save?")
        add_note(listen())
        return

    if intent=="TASK":
        speak("Tell task")
        add_task(listen())
        return

    if intent=="POMODORO":
        start_pomodoro()
        return

    if intent=="PLAY":
        play_youtube(cmd)
        return

    if intent=="YOUTUBE":
        open_youtube(cmd)
        return

    if intent=="GOOGLE":
        open_google(cmd)
        return

    if intent=="VISION":
        vision()
        return

    if intent=="OCR":
        read_text()
        return

    mem = recall(cmd)
    if mem:
        speak(mem)
        return

    def ai_task():
        res = ask_ai(cmd)
        speak(res if res else "AI error")

    threading.Thread(target=ai_task).start()

# ================= MONITOR =================
def inactivity_monitor():
    while True:
        time.sleep(30)
        if time.time() - LAST_ACTIVITY > 300:
            trigger_safety("No response")

# ================= MAIN =================
def main():
    speak("Initializing Acharya")

    if init_ai():
        speak("AI ready")
    else:
        speak("AI failed")

    threading.Thread(target=inactivity_monitor, daemon=True).start()

    while True:
        cmd = listen()
        if cmd:
            print("YOU:",cmd)
            process(cmd)

# ================= RUN =================
if __name__=="__main__":
    main()
  
