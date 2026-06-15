import speech_recognition as sr
import pyttsx3
import threading
import time
import random
import geocoder
import wave
import pyaudio
import cv2
import winsound
from twilio.rest import Client
import numpy as np
import librosa
import joblib
import os

# tkinter used only for the optional confirmation window
try:
    import tkinter as tk
    from tkinter import messagebox
    TK_AVAILABLE = True
except Exception:
    TK_AVAILABLE = False

# ================= CONFIG =================
DISTRESS_KEYWORDS = [
    "help", "save me", "danger", "emergency",
    "bachao", "madad", "madad karo",
    "bachao mujhe", "koi bachao"
]

DISTRESS_THRESHOLD = 3
SILENCE_TIMEOUT = 5
NO_INPUT_ALARM_TIME = 10
VOICE_TIMEOUT = 10
WAKE_WORD = "safeguard"
VOICE_TIMEOUT = 10

SILENT_MODE = False
STEALTH_MODE = False

# ================= TWILIO CONFIG =================
TWILIO_SID = "YOUR_SID"
TWILIO_AUTH = "YOUR_AUTH"
TWILIO_PHONE = "+1234567890"
TARGET_PHONE = "+91XXXXXXXXXX"
WHATSAPP_FROM = "whatsapp:+14155238886"
WHATSAPP_TO = "whatsapp:+91XXXXXXXXXX"

# ================= GLOBAL =================
alarm_running = False
video_running = False
gps_running = False
last_input_time = time.time()

SYSTEM_STATE = "ARMED"
distress_score = 0

# ================= INIT =================
engine = pyttsx3.init()
engine.setProperty('rate', 170)

recognizer = sr.Recognizer()

# ================= ML MODEL LOAD =================
MODEL = None
SCALER = None

try:
    if os.path.exists("distress_model.pkl") and os.path.exists("distress_scaler.pkl"):
        MODEL = joblib.load("distress_model.pkl")
        SCALER = joblib.load("distress_scaler.pkl")
        print(" Loaded distress_model.pkl and distress_scaler.pkl")
    else:
        print(" ML model files not found. Using keyword detector only.")
except Exception as e:
    print(" Error loading model:", e)
    MODEL = None
    SCALER = None

# ================= SPEAK =================
def speak(text):
    if STEALTH_MODE:
        print("AI:", text)
        return
    print("AI:", text)
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception:
        # TTS may fail on headless systems
        print("(TTS failed)")

# ================= LOCATION =================
def get_location():
    try:
        g = geocoder.ip('me')
        lat, lng = g.latlng
        return lat, lng, f"https://maps.google.com/?q={lat},{lng}"
    except Exception:
        return None, None, "Location not available"

# ================= TWILIO ALERT =================
def send_twilio_alert():
    try:
        client = Client(TWILIO_SID, TWILIO_AUTH)
        _, _, link = get_location()

        msg = f" EMERGENCY ALERT!\nLocation: {link}"

        client.messages.create(body=msg, from_=TWILIO_PHONE, to=TARGET_PHONE)
        client.messages.create(body=msg, from_=WHATSAPP_FROM, to=WHATSAPP_TO)

        print(" SMS & WhatsApp sent")

    except Exception as e:
        print(" Twilio error:", e)

# ================= ALARM =================
def play_alarm():
    global alarm_running
    alarm_running = True
    while alarm_running:
        try:
            winsound.Beep(1000, 400)
            winsound.Beep(2000, 400)
        except Exception:
            time.sleep(0.8)


def stop_alarm():
    global alarm_running
    alarm_running = False

# ================= GPS =================
def live_gps():
    global gps_running
    gps_running = True
    while gps_running:
        _, _, link = get_location()
        print("📍", link)
        time.sleep(5)


def stop_gps():
    global gps_running
    gps_running = False

# ================= AUDIO RECORD (general) =================
def record_audio(duration=10, filename="evidence.wav", rate=22050):
    chunk = 1024
    p = pyaudio.PyAudio()

    try:
        stream = p.open(format=pyaudio.paInt16, channels=1,
                        rate=rate, input=True,
                        frames_per_buffer=chunk)
    except Exception as e:
        print(" Microphone not available:", e)
        return

    frames = []
    for _ in range(int(rate / chunk * duration)):
        frames.append(stream.read(chunk))

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(filename, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()

    print(" Audio saved:", filename)

# ================= CAMERA =================
def get_camera():
    for i in range(3):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            print(f" Camera opened at index {i}")
            return cap
    return None


def record_video(duration=15, filename="evidence.avi"):
    global video_running
    video_running = True

    cap = get_camera()

    if cap is None:
        print(" Camera not accessible")
        return

    cap.set(3, 640)
    cap.set(4, 480)

    out = cv2.VideoWriter(filename,
                          cv2.VideoWriter_fourcc(*'XVID'),
                          20.0, (640, 480))

    print(" Recording video...")

    start = time.time()

    while video_running and time.time() - start < duration:
        ret, frame = cap.read()

        if not ret:
            break

        out.write(frame)
        cv2.imshow("Recording", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

    video_running = False
    print(" Video saved")


def stop_video():
    global video_running
    video_running = False

# ================= FAKE CALL =================
def fake_call():
    speak("Incoming call from family")

    for _ in range(5):
        try:
            winsound.Beep(1500, 500)
        except Exception:
            pass
        time.sleep(0.5)

    speak("Hello, where are you? Come home quickly.")

# ================= AUDIO FEATURE EXTRACTION + ML PREDICTION =================
def extract_features(filename, sr_target=22050):
    try:
        y, sr = librosa.load(filename, sr=sr_target)
        mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
        mfcc_means = np.mean(mfcc, axis=1)
        zcr = np.mean(librosa.feature.zero_crossing_rate(y=y))
        # compute RMS manually for compatibility across librosa versions
        try:
            rmse = np.mean(librosa.feature.rms(y=y))
        except Exception:
            rmse = float(np.sqrt(np.mean(y.astype(float) ** 2)))
        feats = np.hstack([mfcc_means, zcr, rmse])
        return feats
    except Exception as e:
        print(" Feature extraction failed:", e)
        return None


def detect_distress_ml(wavfile="last_input.wav"):
    if MODEL is None or SCALER is None:
        return 0.0

    if not os.path.exists(wavfile):
        return 0.0

    feats = extract_features(wavfile)
    if feats is None:
        return 0.0

    try:
        X = SCALER.transform(feats.reshape(1, -1))
        proba = MODEL.predict_proba(X)[0]
        # proba[0] is distress (label 0), proba[1] is normal (label 1)
        return float(proba[0])
    except Exception as e:
        print(" ML predict failed:", e)
        return 0.0

# ================= INPUT & LISTEN FALLBACKS =================
def input_with_timeout(prompt="", timeout=5):
    # If timeout is None, block until user input (no typing timer)
    if timeout is None:
        try:
            return input(prompt).lower()
        except Exception:
            return ""

    user_input = {"value": ""}

    def get_input():
        try:
            user_input["value"] = input(prompt)
        except Exception:
            user_input["value"] = ""

    thread = threading.Thread(target=get_input)
    thread.daemon = True
    thread.start()
    thread.join(timeout)

    if thread.is_alive():
        return ""
    else:
        return user_input["value"].lower()


def listen_once(timeout=5):
    try:
        with sr.Microphone() as source:
            # Calibrate for ambient noise (longer for noisy rooms)
            try:
                print("Calibrating microphone for ambient noise...")
                recognizer.adjust_for_ambient_noise(source, duration=1.0)
            except Exception:
                pass

            print(f" Listening (will wait up to {timeout}s for phrase start)...")
            try:
                audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=6)
            except sr.WaitTimeoutError:
                print(" No speech detected (start timeout)")
                return ""

            # Save audio for ML
            try:
                wav_data = audio.get_wav_data()
                with open("last_input.wav", "wb") as f:
                    f.write(wav_data)
            except Exception:
                pass

            try:
                text = recognizer.recognize_google(audio)
                return text.lower()
            except sr.UnknownValueError:
                print(" Speech not understood")
                return ""
            except sr.RequestError as e:
                print(" Speech recognition request failed:", e)
                return ""
    except Exception as e:
        print(" Microphone/listen error:", e)
        return ""


def listen_with_fallback(timeout=5):
    start = time.time()

    # Keep attempting short listens until the overall timeout elapses
    while time.time() - start < timeout:
        remaining = max(1, int(timeout - (time.time() - start)))
        text = listen_once(timeout=remaining)
        if text:
            return text

    # If not captured by voice, ask for typed input with a short timeout
    print(" No voice input detected. Type input (or wait to continue):")
    typed = input_with_timeout(prompt="> ", timeout=20)
    return typed.lower() if typed else ""

# ================= OTHER HELPERS =================
def detect_shake():
    motion = random.uniform(0, 30)
    print("Motion:", motion)
    return motion > 20


def wait_for_wake(timeout=None):
    """Block until the wake word is heard. If timeout is provided, return None after timeout seconds."""
    start = time.time()
    print(f"Waiting for wake word: '{WAKE_WORD}'")
    while True:
        if timeout and (time.time() - start) > timeout:
            return None
        text = listen_once(timeout=VOICE_TIMEOUT)
        if not text:
            continue
        print("Heard:", text)
        if WAKE_WORD in text.lower():
            return text


def stop_all():
    stop_alarm()
    stop_video()
    stop_gps()
    speak("All emergency actions stopped.")

# ================= DISTRESS DETECTION (combine keywords + ML) =================
def detect_distress(text):
    text = (text or "").lower()
    score = 0

    for word in DISTRESS_KEYWORDS:
        if word in text:
            score += 2

    if len(text.split()) <= 2 and text != "":
        score += 1

    ml_prob = detect_distress_ml()
    if ml_prob >= 0.75:
        score += 4
    elif ml_prob >= 0.5:
        score += 2
    elif ml_prob > 0:
        score += 1

    if ml_prob > 0:
        print(f"ML distress probability: {ml_prob:.2f}")

    return score

# ================= VERIFY / CONFIRMATION =================
def verify_emergency():
    speak("Are you safe? Say yes or no.")

    start = time.time()
    while time.time() - start < SILENCE_TIMEOUT:
        response = listen_with_fallback(timeout=3)
        if response == "":
            continue

        print("Response:", response)
        if "no" in response or "help" in response:
            return True
        if "yes" in response:
            speak("Okay, staying alert.")
            return False

    speak("No response detected. Triggering emergency.")
    return True


def confirm_window():
    """Show a simple GUI confirmation dialog. Returns True (confirm), False (deny), or None (not available)."""
    if not TK_AVAILABLE:
        return None

    try:
        root = tk.Tk()
        root.withdraw()
        root.attributes('-topmost', True)
        result = messagebox.askyesno("Confirm Emergency", "Possible emergency detected. Are you in danger?")
        root.destroy()
        return bool(result)
    except Exception as e:
        print(" Confirmation window failed:", e)
        return None


def play_confirmation_beep():
    """Play a short beep sequence to draw attention before showing confirmation."""
    try:
        # 3 short beeps
        for _ in range(3):
            winsound.Beep(800, 250)
            time.sleep(0.15)
    except Exception:
        # Non-Windows or winsound failure: fallback to console notice
        print("*** BEEP ***")

# ================= ALERT & EMERGENCY =================
def send_alert():
    _, _, link = get_location()
    speak("Sending emergency alerts")
    print(" Location:", link)
    send_twilio_alert()


def trigger_emergency():
    global SYSTEM_STATE
    SYSTEM_STATE = "EMERGENCY"
    speak("Emergency detected")

    if not SILENT_MODE:
        threading.Thread(target=play_alarm, daemon=True).start()

    threading.Thread(target=record_audio, daemon=True).start()
    threading.Thread(target=record_video, daemon=True).start()
    threading.Thread(target=live_gps, daemon=True).start()

    send_alert()

# ================= COMMANDS =================
def handle_commands(text):
    global SYSTEM_STATE, distress_score
    t = (text or "").lower()

    if "i am safe" in t or "safe" in t:
        SYSTEM_STATE = "SAFE"
        distress_score = 0
        stop_alarm()
        stop_video()
        stop_gps()
        speak("System safe")
        return True

    if "activate" in t:
        SYSTEM_STATE = "ARMED"
        speak("System armed")
        return True

    if "fake call" in t:
        threading.Thread(target=fake_call, daemon=True).start()
        return True

    if "help" in t or "emergency" in t:
        trigger_emergency()
        return True

    return False

# ================= MAIN =================
def main():
    global distress_score

    speak("ACHARYA SAFE system activated")
    distress_score = 0

    while True:
        # Wait for the wake word before entering active detection
        wake = wait_for_wake()
        if wake is None:
            # timed out waiting for wake (unlikely with no timeout) — loop again
            continue

        speak("Listening for commands")
        # Active detection loop; will stop when user says "i am safe" (handled in handle_commands)
        while True:
            text = listen_with_fallback(timeout=VOICE_TIMEOUT)

            if text == "":
                distress_score += 1
                print(" No input detected")
            else:
                speak(f"You said {text}")

            # If user explicitly says they're safe, stop detection and return to wake-wait
            if handle_commands(text):
                # handle_commands sets SYSTEM_STATE to SAFE when hearing "i am safe"
                speak("Stopping detection until wake word is heard")
                distress_score = 0
                break

            if SYSTEM_STATE == "SAFE":
                speak("System is SAFE — awaiting wake word")
                distress_score = 0
                break

            score = detect_distress(text)
            distress_score += score

            print("Score:", distress_score)

            if detect_shake():
                distress_score += 1
                speak("Sudden movement detected.")

            if distress_score >= DISTRESS_THRESHOLD:
                speak("Possible emergency detected")

                # Play a short attention beep, then show GUI confirmation (or fallback)
                play_confirmation_beep()
                gui_result = confirm_window()
                if gui_result is True:
                    # send alerts to everyone after confirmation
                    send_alert()
                    speak("Alerts sent")
                elif gui_result is False:
                    speak("Emergency cancelled by user")
                else:
                    # GUI not available or failed — use voice verification
                    if verify_emergency():
                        send_alert()
                        speak("Alerts sent")

                distress_score = 0

            time.sleep(1)


if __name__ == "__main__":
    main()
   