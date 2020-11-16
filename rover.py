#!/usr/bin/python3
from mattermostdriver import Driver

import json
import sys
import RPi.GPIO as GPIO
from time import sleep

mattermosturl='your.mattermost.server'
personaltoken='yourtoken'
easymode=False # easymode True= Command lasts 0.5 seconds, rover stops. easymode False = Command lasts until you give a new command, continous driving
enginepower=100 #0=SLOW, 100=FULLSPEED

# THE GPIO PINS YOU ARE USING ON YOUR RASPBERRY
rightmotorin1 = 24
rightmotorin2 = 23
rightmotoren = 25
leftmotorin1 = 17
leftmotorin2 = 22
leftmotoren = 27
lights=21



#START CODE #
GPIO.setmode(GPIO.BCM)
GPIO.setup(lights,GPIO.OUT)
GPIO.setup(leftmotorin1,GPIO.OUT)
GPIO.setup(rightmotorin1,GPIO.OUT)
GPIO.setup(leftmotorin2,GPIO.OUT)
GPIO.setup(rightmotorin2,GPIO.OUT)
GPIO.setup(leftmotoren,GPIO.OUT)
GPIO.setup(rightmotoren,GPIO.OUT)
GPIO.output(lights,GPIO.LOW)
GPIO.output(leftmotorin1,GPIO.LOW)
GPIO.output(rightmotorin1,GPIO.LOW)
GPIO.output(leftmotorin2,GPIO.LOW)
GPIO.output(rightmotorin2,GPIO.LOW)
p1=GPIO.PWM(leftmotoren,1000)
p2=GPIO.PWM(rightmotoren,1000)
p1.start(100)
p2.start(100)


def forward():
    GPIO.output(leftmotorin1,GPIO.LOW)
    GPIO.output(leftmotorin2,GPIO.HIGH)
    GPIO.output(rightmotorin1,GPIO.LOW)
    GPIO.output(rightmotorin2,GPIO.HIGH)
    if easymode:
       easystop()

def backwards():
    GPIO.output(leftmotorin1,GPIO.HIGH)
    GPIO.output(leftmotorin2,GPIO.LOW)
    GPIO.output(rightmotorin1,GPIO.HIGH)
    GPIO.output(rightmotorin2,GPIO.LOW)
    if easymode:
       easystop()

def stop():
    GPIO.output(leftmotorin1,GPIO.LOW)
    GPIO.output(rightmotorin1,GPIO.LOW)
    GPIO.output(leftmotorin2,GPIO.LOW)
    GPIO.output(rightmotorin2,GPIO.LOW)
    print(stop)

def left():
    GPIO.output(leftmotorin1,GPIO.LOW)
    GPIO.output(leftmotorin2,GPIO.HIGH)
    GPIO.output(rightmotorin1,GPIO.HIGH)
    GPIO.output(rightmotorin2,GPIO.LOW)
    if easymode:
       easystop()

def right():
    GPIO.output(leftmotorin1,GPIO.HIGH)
    GPIO.output(leftmotorin2,GPIO.LOW)
    GPIO.output(rightmotorin1,GPIO.LOW)
    GPIO.output(rightmotorin2,GPIO.HIGH)
    if easymode:
       easystop()


def ledon():
    print("ledon")
    GPIO.output(lights,GPIO.HIGH)

def ledoff():
    print("ledoff")
    GPIO.output(lights,GPIO.LOW)

def easystop():
   sleep(0.5)
   stop()


def blink():
    print('blink')
    for x in range(10):
        GPIO.output(lights,GPIO.HIGH)
        sleep(0.5)
        GPIO.output(lights,GPIO.LOW)
        sleep(0.5)





mm = Driver({
      'url': mattermosturl,
      "token":personaltoken,
      'scheme': 'https',
      'port': 443
    })


mm.login()
async def my_event_handler(e):
    message=json.loads(e)
    if 'event' in message:
        print('----------------------------------------------')
        print(message)
        if message['event']=='reaction_added':
            reaction=json.loads(message['data']['reaction'])
            post_id=reaction['post_id']
            post=mm.posts.get_post(post_id)
            emoji=reaction['emoji_name']
            if emoji=='stop_sign':
                stop()
            if emoji=='arrow_up':
                forward()
            if emoji=='arrow_down':
                backwards()
            if emoji=='arrow_left':
                left()
            if emoji=='arrow_right':
                right()
            if emoji=='flashlight':
                ledon()
            if emoji=='sunny':
                ledoff()
            if emoji=='wink':
                 blink()
                 
        if message['event']=='posted' or message['event']=='post_edited':
            reaction=json.loads(message['data']['post'])
            post=reaction['message']
            if 'stop' in post:
                stop()
            if 'up' in post:
                print('forward')
                forward()
            if 'down' in post:
                backwards()
            if 'left' in post:
                left()
            if 'right' in post:
                right()
            if 'on' in post:
                ledon()
            if 'off' in post:
                ledoff()
            if 'blink' in post:
                 blink()


mm.init_websocket(my_event_handler)
