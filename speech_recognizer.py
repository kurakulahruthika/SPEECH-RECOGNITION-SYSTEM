#!/usr/bin/env python3

import time
import speech_recognition as sr

def callback(recognizer, audio):
    try:
        print("Google Speech Recognition thinks you said: " + recognizer.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

r = sr.Recognizer()
m = sr.Microphone()

with m as source:
    print("Calibrating microphone for ambient noise...")
    r.adjust_for_ambient_noise(source)
    print("Calibration complete.")

# Start listening in the background
stop_listening = r.listen_in_background(m, callback)
print("Listening in the background...")

try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Stopping background listener...")
    stop_listening(wait_for_stop=False)
