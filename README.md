Hybrid Voice and Vision Automation System

Hello and welcome to my automation project. I built this system to bridge the gap between physical hardware and smart software. Instead of using a regular switch, this project turns a Raspberry Pi 4 into an intelligent room controller that reacts to ambient light and human voice commands. I developed this during my Embedded Systems internship at Ignite Innovation Techno Solutions.


What it Does

Auto Mode. It uses your webcam as a light sensor. If you turn off the room lights, it instantly turns on your LED.
Manual Mode. When you speak a command like Turn on, it stops listening to the camera and obeys your voice.


What You Need to Build This

A Raspberry Pi 4 connected to the internet.

A USB Webcam with a microphone.

An LED.

A 220 ohm or 330 ohm resistor.

A breadboard and jumper wires.


Step by Step Setup Guide


Step 1. Wire it up.
Connect the longer leg of your LED to GPIO 17, which is Physical Pin 11. Connect the shorter leg of your LED to your resistor, and plug the other end of the resistor into a Ground pin, like Physical Pin 6. Plug your USB Webcam into the Pi.


Step 2. Grab the Code.
Open your Raspberry Pi terminal and clone this repository to your machine using your git clone link, then navigate into the downloaded folder.


Step 3. Install the software.
Update your system and install the audio and vision tools by typing sudo apt update, and then type sudo apt install python3-pyaudio flac python3-opencv. Next, install the Python libraries by typing pip3 install SpeechRecognition gpiozero opencv-python numpy.


Step 4. Run the project.
Run the main script by typing python3 hybrid_controller.py. When you hit enter, stay quiet for two seconds so the microphone can calibrate to the background noise in your room.


How to Talk to It

Command 1. Say Turn on to override the camera and force the light on.

Command 2. Say Turn off to override the camera and force the light off.

Command 3. Say Auto to give control back to the camera light sensor.
