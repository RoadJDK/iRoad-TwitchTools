from screen_search import *
import pyautogui as py
import time
import random
import sys

with open('names.txt') as f:
    names = f.read().splitlines()

def sleep():
    time.sleep(0.7)

def type(text):
    py.write(text)

def getRandomName(aprefix):
    return aprefix + random.choice(names) + str(random.randint(0,100000))

def getRandomPass():
    return str(random.randint(1000,100000000)) + "asdazasgdhjasdhgasdhgasdghjadiuasjudhsd"

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

def run(aprefix):
    search = Search("../captcha.png")
    nr = 1
    #sign up
    py.click(1839,90)
    sleep()
    #username (check if username already exists)
    while(True):
        username = getRandomName(aprefix)
        with open('accounts.txt') as f:
            if username in f.read():
                print("assign new name")
            else:
                f.close()
                break
    password = getRandomPass()
    type(username)
    sleep()
    #password
    py.click(800,500)
    sleep()
    type(password)
    sleep()
    #password confirm
    py.click(800,560)
    sleep()
    type(password)
    sleep()
    #month
    py.click(834,628)
    sleep()
    py.click(834,674)
    sleep()
    #day
    py.click(980,618)
    type('3')
    sleep()
    #year
    py.click(1100,618)
    type('2000')
    sleep()

    #GET EMAIL
    #browser2
    py.click(344,13)
    sleep()
    py.click(950,600)
    sleep()
    py.click(1033,444)
    sleep()

    #browser1
    py.click(150,10)
    sleep()
    #email
    py.click(800,700)
    sleep()
    #right click
    py.click(button='right')
    py.click(860,850)
    sleep()
    #submit
    py.click(860,817)
    time.sleep(5)

    #confirm email
    #browser2
    py.click(344,13)
    time.sleep(18)
    py.click(500,500)
    sleep()
    py.click(710,510)
    py.click(710,510)
    sleep()
    #right click
    py.click(button='right')
    py.click(725,520)
    sleep()
    py.click(555,420)
    time.sleep(2)

    #browser1
    py.click(150,10)
    sleep()
    #check if captcha is here
    if py.locateOnScreen('src/captcha.png') != None:
        py.click(85,45)
        print("captcha found, try again")
        cooldownLong(600)
        return
    py.click(828,551)
    py.click(button='right') 
    sleep()
    py.click(850,700)
    time.sleep(10)

    #reset
    py.click(1900,100)
    time.sleep(2)
    py.click(1750,600)
    time.sleep(5)

    #end
    print("made account: " + str(nr) + " - " + str(username))
    nr += 1
    #write in file
    f = open('accounts.txt',"a")
    f.write(username + ':' + password + '\n')
    f.close()

    cooldownLong(600)
    print("done")

def create(aprefix,count):
    if count == 0:
        while (True):
            run(aprefix)
    else:
        cur = 0
        while cur <= count:
            run(aprefix)
            cur += 1
        print("All done!")
