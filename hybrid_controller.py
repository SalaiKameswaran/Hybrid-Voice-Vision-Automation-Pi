import cv2
import numpy as np
import speech_recognition as sr
from gpiozero import LED
import time

# 1. Hardware Initialization
led = LED(17)
cap = cv2.VideoCapture(0)
DARKNESS_THRESHOLD = 60

# 2. System State Tracking
# current_mode can be "auto", "manual_on", or "manual_off"
current_mode = "auto"  

# 3. Speech Recognition Setup
recognizer = sr.Recognizer()
microphone = sr.Microphone()

def process_voice_command(recognizer, audio):
    """This function runs in the background whenever audio is detected."""
    global current_mode
    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"\n[Voice Command Heard]: '{command}'")
        
        if "turn on" in command:
            current_mode = "manual_on"
            print("--> OVERRIDE: System is now MANUAL ON")
        elif "turn off" in command:
            current_mode = "manual_off"
            print("--> OVERRIDE: System is now MANUAL OFF")
        elif "auto" in command or "automatic" in command:
            current_mode = "auto"
            print("--> CAMERA CONTROL: System restored to AUTO MODE")
            
    except sr.UnknownValueError:
        # Silently ignore audio that isn't speech (keyboard clicks, background noise)
        pass 
    except sr.RequestError as e:
        print(f"\n[Error] Network issue with Speech API: {e}")

print("Initializing System... Please stay quiet for 2 seconds for mic calibration.")

# Calibrate the microphone before starting the background thread
with microphone as source:
    recognizer.adjust_for_ambient_noise(source, duration=2)

print("\n=== SYSTEM READY ===")
print("1. Camera is running in AUTO mode.")
print("2. Say 'Turn on' or 'Turn off' to override.")
print("3. Say 'Auto' to give control back to the camera.")
print("Press Ctrl+C to exit.\n")

# Start listening in the background. This won't block the camera loop below.
stop_listening = recognizer.listen_in_background(microphone, process_voice_command)

try:
    # Main Camera Loop
    while True:
        ret, frame = cap.read()
        
        if not ret:
            print("Error: Could not read from webcam.")
            break
            
        # Check camera brightness
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        average_brightness = np.mean(gray_frame)
        
        # Apply the logic based on the current mode
        if current_mode == "auto":
            if average_brightness < DARKNESS_THRESHOLD:
                led.on()
            else:
                led.off()
                
        elif current_mode == "manual_on":
            led.on()
            
        elif current_mode == "manual_off":
            led.off()
            
        # Give the CPU a tiny rest (0.1 seconds) to prevent overheating
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nProgram terminated manually.")

finally:
    # Safely shut down background threads and hardware
    stop_listening(wait_for_stop=False)
    led.off()
    cap.release()
