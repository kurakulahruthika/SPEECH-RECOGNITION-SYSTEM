# SPEECH-RECOGNITION-SYSTEM

*company*:codtech it solutions

*NAME:KURAKULA HRUTHIKA*

*INTERN ID*:CT04DF664

*DOMAIN*: AI

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH*company*:codtech it solutions



## DESCRIPTION ABOUT MY TASK

Certainly! Here's a *500+ word detailed project description* for your *Speech Recognition System, written in a personalized and technical style — perfect for a GitHub repository. It clearly explains **how you implemented it*, the tools used, key steps, challenges, and what you learned.

---

##   Speech Recognition System – Project Description

###  Overview

This project involves building a *Speech Recognition System* that converts human voice into text using Python and machine learning tools. The system listens to spoken language via a microphone or an audio file and transcribes it into readable text, demonstrating real-world applications of *automatic speech recognition (ASR)*.

My goal was to understand how voice input can be processed, interpreted, and translated by machines, and to gain hands-on experience with real-time audio processing, NLP preprocessing, and the use of cloud-based and offline recognition engines.

---

###  Project Goals

* Record or load voice input
* Process the audio using a speech recognition engine
* Convert audio signals into textual form
* Handle noisy audio and unexpected input gracefully
* Explore both *offline* and *online* recognition methods

---

###  How I Did It – Step-by-Step

####  Step 1: Setting Up the Environment

I began by installing necessary libraries:

* speechrecognition – core library for recognizing speech
* pyaudio – to access the system’s microphone for live input
* wave – to save and replay audio
* gtts and playsound (optional) – for voice feedback

I tested microphone access and verified the sample rate and input device index to ensure smooth audio capture.

####  Step 2: Capturing or Loading Audio

There were two modes:

1. *Live Microphone Input:* Using Microphone() class from speech_recognition, I captured short audio clips using context managers. I also implemented a background listener for continuous recognition.
2. *Audio File Input:* Using pre-recorded .wav or .flac files with AudioFile().

For each audio sample:

* The system used Recognizer().listen() to capture spoken audio
* I added a timeout mechanism and exception handling for cases of silence or unexpected input

####  Step 3: Recognizing Speech

I experimented with various backends:

* *Google Web Speech API*: High accuracy, simple API call
* *Sphinx (CMU Sphinx)*: Works offline, good for basic recognition
* *Google Cloud Speech-to-Text API*: Used for higher accuracy with longer transcriptions (optional key)

Sample method:

python
recognizer.recognize_google(audio_data)


The recognized text was printed to the console or saved to a text file. I added a function to differentiate between short and long-form inputs and process them accordingly.

####  Step 4: Handling Noisy or Low-Quality Audio

To improve recognition:

* Applied ambient noise adjustment using recognizer.adjust_for_ambient_noise(source)
* Added custom exceptions for UnknownValueError and RequestError
* Used silence thresholds and pause durations to clean inputs

####  Step 5: Enhancing and Testing

I tested the system with various accents, sentence lengths, and noise environments. I also included support for basic voice commands and converted the results into text-to-speech feedback using Google Text-to-Speech (gTTS).

---

###  Tools & Libraries Used

* *Python 3*
* *SpeechRecognition*
* *PyAudio*
* *Google Speech API*
* *gTTS (Google Text-to-Speech)*
* *Wave, Playsound*
* *CMU Sphinx (for offline support)*

---

###  Challenges Faced

* Microphone sensitivity was inconsistent across devices
* Handling ambient noise and echoes required tuning
* Internet dependency for online recognizers (like Google API)
* CMU Sphinx was fast but less accurate for conversational phrases
* Managing different audio formats (.wav, .flac) and sample rates

---

###  What I Learned

* How to access system microphones and work with audio streams in real time
* The difference between offline and online speech recognition engines
* How speech is converted into digital form, parsed, and interpreted
* How to handle uncertainty and exceptions in voice-based applications
* How to preprocess audio for better ASR performance

---

###  Results and Output

The system was able to accurately transcribe short commands, complete sentences, and phrases like:

> *You said:* "Turn on the lights in the living room."

The transcription was almost real-time with Google API and acceptable offline with Sphinx for simpler inputs.

---

###  Conclusion

This Speech Recognition System gave me insight into how humans and machines can interact through voice. It demonstrated practical applications in *smart assistants, **voice-controlled devices, **chatbots, and **accessibility tools*. I now better understand the building blocks behind systems like Alexa, Siri, and Google Assistant.

In the future, I plan to integrate this system with NLP models to create a voice-controlled chatbot or extend it into a voice command interface for IoT devices.

### OUTPUT

![image](https://github.com/user-attachments/assets/2d3e4e9f-2b40-4b50-be4e-0391bf4500ef)




