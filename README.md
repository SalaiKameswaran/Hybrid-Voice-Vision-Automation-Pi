# Hybrid Voice and Vision Automation System 🎙️👁️💡

Hybrid Voice and Vision Automation System is an intelligent, edge-computing IoT application built for the Raspberry Pi 4. It features:

* **Hardware/OS:** Raspberry Pi 4 / Raspberry Pi OS
* **Computer Vision Integration:** OpenCV (for automated ambient light sensing)
* **Speech Recognition:** Google Speech-to-Text API (for background voice control)
* **Hardware Actuation:** GPIO Zero (for LED / 5V Relay control)

Developed during an Embedded Systems internship at Ignite Innovation Techno Solutions (IITS).

---

### 1. Prerequisites
Ensure you have the following hardware and software ready before starting:
* Raspberry Pi 4 (with internet connection)
* USB Webcam (with built-in microphone)
* LED (or 5V Relay Module for appliances) + 220Ω / 330Ω Resistor
* Breadboard & Jumper Wires
* Python 3 installed on the Raspberry Pi

### 2. Clone The Repository
Open your Raspberry Pi terminal and run:
```bash
git clone [https://github.com/YourUsername/Hybrid-Voice-Vision-Automation-Pi.git](https://github.com/YourUsername/Hybrid-Voice-Vision-Automation-Pi.git)
cd Hybrid-Voice-Vision-Automation-Pi
(Note: Replace YourUsername with your actual GitHub username).

3. Install Dependencies
Install the required system-level audio and vision libraries:

Bash
sudo apt update
sudo apt install python3-pyaudio flac python3-opencv
Install the required Python packages:

Bash
pip3 install SpeechRecognition gpiozero opencv-python numpy
4. Hardware Setup
Wire the hardware components before running the scripts:

LED Anode (+): Connect to BCM GPIO 17 (Physical Pin 11)

LED Cathode (-): Connect to resistor, then to GND (Physical Pin 6)

Webcam: Plug into any available USB port.

5. Run The System
Open the terminal inside your project folder and run the main hybrid controller:

Bash
python3 hybrid_controller.py
Note: Please remain quiet for the first 2 seconds while the system calibrates the microphone to your room's ambient noise.

6. Usage & Modes
Auto Mode (Default): The system uses OpenCV to read the room's brightness. Cover the webcam lens with your hand to simulate darkness and watch the LED turn ON automatically.

Manual Override: Speak a voice command. The system will instantly lock into a manual state, ignoring the camera feed until you reset it.

7. Voice Commands Used
Speak these commands clearly into the webcam microphone:

"Turn on" -> Overrides camera and forces the GPIO ON.

"Turn off" -> Overrides camera and forces the GPIO OFF.

"Auto" -> Returns control to the ambient light sensor.
