import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio).lower()
        print("You said:", query)
        return query
    except sr.UnknownValueError:
        print("Sorry, I didn't get that.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

def voice_assistant():
    speak("Hello! How can I assist you today?")
    while True:
        query = listen()

        if "hello" in query:
            speak("Hi there! How can I help you?")
        elif "what is your name" in query:
            speak("I am your Python voice assistant.")
        elif "exit" in query:
            speak("Goodbye!")
            break
        else:
            speak("I'm sorry,I didn't understand that. Can you please repeat?")

if __name__ == "__main__":
    voice_assistant()

