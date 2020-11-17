#!/usr/bin/python3
from mattermostdriver import Driver

import json
import sys
import explorerhat
from time import sleep

mattermosturl='your.mattermost.server'
personaltoken='yourtoken'
easymode=False # easymode True= Command lasts 0.5 seconds, rover stops. easymode False = Command lasts until you give a new command, continous driving



#START CODE #


def forward():
    explorerhat.motor.forwards()
    if easymode:
       easystop()

def backwards():
    explorerhat.motor.backwards()
    if easymode:
       easystop()

def stop():
    explorerhat.motor.stop()

def left():
    explorerhat.motor.two.stop()
    explorerhat.motor.one.forwards()
    if easymode:
       easystop()

def right():
    explorerhat.motor.one.stop()
    explorerhat.motor.two.forwards()
    
    if easymode:
       easystop()


def ledon():
    print("ledon")
    explorhat.light.on()

def ledoff():
    print("ledoff")
    explorhat.light.off()

def easystop():
   sleep(0.5)
   stop()


def blink():
    print('blink')
    for x in range(10):
        explorhat.light.toggle()
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
