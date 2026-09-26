import speech_recognition as sr
import pyttsx3

# Initialize TTS Engine
engine = pyttsx3.init()
engine.setProperty('rate', 175)  # Adjust speaking speed

def speak(text: str):
    """Prints and speaks out loud."""
    print(f"Agent: {text}")
    engine.say(text)
    engine.runAndWait()

def listen() -> str:
    """Captures microphone input and converts speech to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text.strip()
        except sr.WaitTimeoutError:
            return ""
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            speak("Speech recognition service is unavailable.")
            return ""