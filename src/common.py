from screen_search import *
import pyautogui as py
import time
import sys

def typeText(text):
    py.write(text)

def sleep():
    time.sleep(0.8)

def cooldown(t):
    for remaining in range(t,0,-1):
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} seconds remaining...".format(remaining))
        sys.stdout.flush()
        time.sleep(1)

def cooldownLong(t):
    state = 1
    for remaining in range(t,0,-1):
        sys.stdout.write("\r")
        if(state == 1):
            sys.stdout.write("{:2d} seconds remaining.".format(remaining))
            state += 1
        elif(state == 2):
            sys.stdout.write("{:2d} seconds remaining..".format(remaining))
            state += 1
        elif(state == 3):
            sys.stdout.write("{:2d} seconds remaining...".format(remaining))
            state = 1
        sys.stdout.flush()
        time.sleep(1)