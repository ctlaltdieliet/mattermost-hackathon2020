# Mattermost/Jitsi hackathon2020
We control a rover through Mattermost and its webcam in Jitsi in Mattermost.

## Goal
Working remotely has an impact on the social connections between your teammembers.
There is a lot of attention how to work remotely in a productive way. 
But humans are not robots yet, We are still social animals. ;)
With this project teams can make some fun and get to know each other better.
You can have races with one or multiple rover sand even start a competition.
Or you let it drive through empty workspace from your team.
Or you can organise your own internal hacakthon on modifying the rover.
Or you can use it in STEM-education

## Video
[![Video](http://img.youtube.com/vi/1a9z1G-1u7s/1.jpg)](http://www.youtube.com/watch?v=1a9z1G-1u7s "Video")

## Requirements
-  Raspberry Pi 3 or 4
-  Micro SD Card (>=8GB)
-  Powerbank
-  Webcam or Pi-cam
-  a Mattermost-instance with the Jitsi Plugin installed
-  a Mattermost Personal Access Token 
-  or a [Kookye Rover Tank](https://www.amazon.com/KOOKYE-Platform-Stainless-Raspberry-Electronic/dp/B08G4HMW89/) and a L298n dual motor bridge, 9v battery, small breadboard, 330 ohm resistor
-  or a [Pimoroni sts roving robot kit and an explorer hat pro expansion](https://www.amazon.com/Pimoroni-STS-Build-Raspberry-Roving/dp/B01HZFRROE)


## How does it work
You open Mattermost and start a video meeting in Jitsi. 
The raspberry pi boots and opens automaticly the Jitsi videochannel a chromium browser. We specify that the prejoin page is disabled.
The raspberry pi starts up a python scripts that listens to the Mattermost API.
If you react to a post with arrow_down,arrow_up,arrow_left,arrow_right, stop_sign emoticons the rover reacts.
If you send up,down,left,right,stop the rover reacts.
If you have leds, you also have on,off,blink to control the leds.

## Installation
### Python script rover.py
-  Install python 3
-  Install the Mattermost Driver (pip3 install mattermostdriver)

### Python script pimoroni.py
-  Install python 3
-  Install the Mattermost Driver (pip3 install mattermostdriver)


### Kookye Tank
- L298N Motor left: GPIO Pin 17 = in1, GPIO Pin22 in2, GPIO Pin 27= len
- L298N Motor right: GPIO Pin 24 = in1, GPIO Pin23 in2, GPIO Pin 25= len
- Leds GPIO Pin 21

### Kookye Tank


### Autostart Chromium
See file autostart
Add the content /home/pi/.config/lxsession/LXDE-pi/autostart


