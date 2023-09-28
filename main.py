# Import the necessary libraries
import speech_recognition as sr
import pyttsx3

# Create a recognizer object
recognizer = sr.Recognizer()

# Create a text-to-speech engine
engine = pyttsx3.init()

# Continuously listen for and process speech input
while True:
    try:
        # Create a context for using the microphone as the audio source
        with sr.Microphone() as mic:
            # Adjust for ambient noise to improve recognition accuracy
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)

            # Listen for audio input from the microphone
            audio = recognizer.listen(mic)

            # Recognize the spoken words using Google Web Speech API
            text = recognizer.recognize_google(audio)
            text = text.lower()

            # Print the recognized text
            print(f"Recognized: {text}")

            # Use the text-to-speech engine to respond
            engine.say(f"You said: {text}")
            engine.runAndWait()

    except sr.UnknownValueError:
        # Handle the case where no speech was recognized
        print("Could not understand the audio")

    except sr.RequestError as e:
        # Handle errors related to the API request
        print(f"Could not request results; {e}")

    except KeyboardInterrupt:
        # Exit the program when the user presses Ctrl+C
        break
