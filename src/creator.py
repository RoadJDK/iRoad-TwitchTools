from pathlib import Path
import pyautogui as py
import time
import random
import sys

names = ['Noob', 'Pleb', 'Anfaenger', 'Kaninchen', 'Hund', 'Kek', 'Vogel', 'Lappen', 'Ehrenmann', 'Katze', 'Hund', 'Labertasche', 'Drache', 'Frechdachs', 'Pferd']

def sleep():
    time.sleep(0.7)

def type(text):
    py.write(text)

def getRandomName():
    return 'KumbaiDu' + random.choice(names) + str(random.randint(0,100000000))

def getRandomPass():
    return str(random.randint(1000,100000000)) + "asdazasgdhjasdhgasdhgasdghjadiuasjudhsd"

filename = Path('accounts.txt')
filename.touch(exist_ok=True)

#wait 5 seconds
time.sleep(5)

nr = 1

while(True):
    #sign up
    py.click(1839,90)
    sleep()
    #username (check if username already exists)
    while(True):
        username = getRandomName()
        with open('accounts.txt') as f:
            if username in f.read():
                print("assign new name")
            else:
                f.close()
                break
    password = getRandomPass()
    f = open('accounts.txt',"a")
    f.write(username + ':' + password + '\n')
    f.close()
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
    py.click(860,817)
    time.sleep(2)

    #confirm email
    #browser2
    py.click(344,13)
    time.sleep(20)
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
    state = 1
    for remaining in range(600,0,-1):
        if(state == 1):
            sys.stdout.write("\r {:2d} seconds remaining.".format(remaining))
            state += 1
        elif(state == 2):
            sys.stdout.write("\r {:2d} seconds remaining..".format(remaining))
            state += 1
        elif(state == 3):
            sys.stdout.write("\r {:2d} seconds remaining...".format(remaining))
            state = 1
        sys.stdout.flush()
        time.sleep(1)
    print("done")