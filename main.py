from src.creator import create, cooldown

from pathlib import Path
import time
import sys
import os

os.system('cls' if os.name == 'nt' else 'clear')

filename = Path('accounts.txt')
filename.touch(exist_ok=True)
filename = Path('names.txt')
filename.touch(exist_ok=True)
filename = Path('phrases.txt')
filename.touch(exist_ok=True)

print(rf"""
    ___                      _ 
 _ |  _`\                   ( )
(_)| (_) )   _      _ _    _| |
| || ,  /  /'_`\  /'_` ) /'_` |
| || |\ \ ( (_) )( (_| |( (_| |
(_)(_) (_)`\___/'`\__,_)`\__,_)
""")
print("Welcome to iRoad TwitchTools!")
print("Please select one of the following options:")
print("1 - Account Creator")
print("2 - Stream Annoyance")
print("3 - Follower Sender")

#check input
while(True):
    selection = input()
    try:
        val = int(selection)
        if (val in range(0,4)):
            break
        else:
            print("not a valid selection...")
    except ValueError:
        print("not a valid selection...")

if (selection == '1'):
    print("Step 1: open your browser fullscreen 1920x1080 on your main screen")
    print('Step 2: In the first tab open "twitch.tv", in the second "muellmail.com"')
    print()
    print("After, please put some names in the generated names.txt file (one name per line) - press ENTER when ready")
    input()
    while(True):
        print("What prefix you want to have?")
        aprefix = input()
        print()
        print("How many accounts should be created? (0 is forever)")
        count = input()
        try:
            val = int(count)
            if (val in range(0,4)):
                break
            else:
                print("not a valid number...")
        except ValueError:
            print("not a valid number...")
    print("Now focus twitch and don't move your mouse from now on!!")
    cooldown(5)
    print("Let's Start!")
    create(aprefix, int(count))

if (selection == '2'):
    print(22)
    
if (selection == '3'):
    print(33)
