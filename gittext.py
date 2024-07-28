import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
import time

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")
        audio = recognizer.listen(source, timeout=5)
    try:
        text = recognizer.recognize_google(audio)
        print("Text:", text)
    except sr.UnknownValueError:
        print("Could not understand.")
    except sr.RequestError:
        print("Could not request results from Google.")

def text_to_speech():
    print("Enter the text you want to hear:")
    text = input()
    voice = gTTS(text, lang="en")
    voice.save("voice.mp3")
    time.sleep(2)
    playsound("voice.mp3")

def main():
    print("Hello! This is a speech-to-text and text-to-speech converter.")
    while True:
        print("Please press 1 for speech-to-text, press 2 for text-to-speech, or press 3 to exit:")
        choice = input()
        
        if choice == "1":
            speech_to_text()
        elif choice == "2":
            text_to_speech()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
