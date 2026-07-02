# Hybrid Voice and Vision Automation System 🎙️👁️💡

This repository contains the source code for an intelligent, edge-computing automation system built on the Raspberry Pi 4. The project bridges the gap between hardware actuation and software processing by combining Google Speech Recognition with OpenCV for environmental monitoring.

Developed during an Embedded Systems internship at Ignite Innovation Techno Solutions (IITS).

## 🚀 Features
* **Computer Vision Integration (Auto Mode):** Utilizes a standard USB webcam and OpenCV to calculate ambient room brightness. The system automatically triggers the GPIO (LED/Relay) when darkness is detected.
* **Voice Control Override (Manual Mode):** Runs a background thread using Google's Speech-to-Text API to continuously listen for vocal commands (e.g., "Turn on," "Turn off").
* **Hybrid State Management:** Seamlessly switches between autonomous environmental sensing and manual user overrides without blocking the camera feed.

## 🛠️ Hardware Requirements
* Raspberry Pi 4
* USB Webcam (Microphone & Camera)
* LED (or 5V Relay Module for larger appliances)
* 220Ω / 330Ω Resistor
* Breadboard & Jumper Wires

## 🔌 Circuit Connection
* **LED Anode (+):** Connect to **BCM GPIO 17** (Physical Pin 11)
* **LED Cathode (-):** Connect to resistor, then to **GND** (Physical Pin 6)

## 💻 Software Dependencies
Ensure your Raspberry Pi is updated and has the required system libraries:
`sudo apt update`
`sudo apt install python3-pyaudio flac python3-opencv`

Install the required Python packages:
`pip3 install SpeechRecognition gpiozero opencv-python numpy`

## ⚙️ How to Run
1. Clone this repository to your device.
2. Navigate to the project directory.
3. Run the hybrid controller:
`python3 hybrid_controller.py`

**Voice Commands:**
* Say *"Turn on"* to manually trigger the GPIO.
* Say *"Turn off"* to manually turn off the GPIO.
* Say *"Auto"* to hand control back to the OpenCV ambient light sensor.

## 👨‍💻 Project Team
* Salai Kameswaran S
* Iniyan P
* Mukundan L
* Hari Krishnan A

*Special thanks to the team at Ignite Innovation Techno Solutions (IITS) for their guidance during this internship.*
