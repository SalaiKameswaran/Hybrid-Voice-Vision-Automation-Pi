import cv2
import numpy as np
from gpiozero import LED
import time

# Initialize the LED on GPIO 17 (Physical Pin 11)
led = LED(17)

# Open the default webcam (index 0)
cap = cv2.VideoCapture(0)

# The brightness threshold (0 = pitch black, 255 = blinding white)
# If the brightness falls below this number, the LED turns ON.
DARKNESS_THRESHOLD = 60

print("Starting webcam light sensor... Press Ctrl+C to stop.")

try:
    while True:
        # Capture a single frame from the webcam
        ret, frame = cap.read()
        
        if not ret:
            print("Error: Could not read from webcam.")
            break
            
        # Convert the color frame to grayscale to make brightness calculation easier
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Calculate the average pixel brightness across the whole image
        average_brightness = np.mean(gray_frame)
        
        print(f"Current Brightness Level: {average_brightness:.2f}")
        
        # Logic to control the LED
        if average_brightness < DARKNESS_THRESHOLD:
            led.on()
        else:
            led.off()
            
        # Wait for 1 second before checking again so we don't overwork the Pi's CPU
        time.sleep(1)

except KeyboardInterrupt:
    print("\nProgram terminated manually.")

finally:
    # Clean up and turn off hardware safely
    led.off()
    cap.release()
