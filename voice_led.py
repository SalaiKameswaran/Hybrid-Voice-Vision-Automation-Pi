"""
Project: Hybrid Voice and Vision Automation System
File: voice_led.py
Description: Basic voice-controlled hardware actuator using Google Speech Recognition.

"""

import speech_recognition as sr
from gpiozero import LED

# Initialize the LED on GPIO 17 (Physical Pin 11)
led = LED(17)

# Initialize the Speech Recognizer
recognizer = sr.Recognizer()

def voice_controller():
    # Use the default system microphone (your USB webcam)
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        # Listen for 1 second to calibrate the energy threshold for background noise
        recognizer.adjust_for_ambient_noise(source, duration=1)
        
        print("\nSystem Ready! Speak your command.")
        print("Examples: 'Turn on the light', 'Turn off the light', or 'Exit'")
        
        while True:
            try:
                print("\nListening...")
                # Capture the audio input
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                
                print("Processing speech...")
                # Convert speech to text using Google's API
                command = recognizer.recognize_google(audio).lower()
                print(f"Recognized Command: '{command}'")
                
                # Logic to control the LED based on keywords
                if "turn on" in command:
                    led.on()
                    print("--> Action: LED is now ON")
                elif "turn off" in command:
                    led.off()
                    print("--> Action: LED is now OFF")
                elif "exit" in command or "stop" in command:
                    print("Exiting controller...")
                    break
                else:
                    print("Command not recognized. Try saying 'Turn on' or 'Turn off'.")
                    
            except sr.WaitTimeoutError:
                # Triggers if no speech is detected within the timeout limit
                pass 
            except sr.UnknownValueError:
                print("Could not understand the audio. Please speak clearly.")
            except sr.RequestError as e:
                print(f"Network error. Could not request results from Google Speech API: {e}")

if __name__ == "__main__":
    try:
        voice_controller()
    except KeyboardInterrupt:
        # Turn off the LED safely if you hit Ctrl+C to stop the script
        led.off()
        print("\nProgram terminated manually.")
