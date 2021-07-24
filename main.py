from src.creator import create, cooldown

from colorama import Fore
from pathlib import Path
import colorama
import time
import sys
import os

os.system('cls' if os.name == 'nt' else 'clear')
colorama.init()

filename = Path('accounts.txt')
filename.touch(exist_ok=True)
filename = Path('names.txt')
filename.touch(exist_ok=True)
filename = Path('phrases.txt')
filename.touch(exist_ok=True)

print(rf"""{Fore.LIGHTGREEN_EX}
    ___                      _ 
 _ |  _`\                   ( )
(_)| (_) )   _      _ _    _| |
| || ,  /  /'_`\  /'_` ) /'_` |
| || |\ \ ( (_) )( (_| |( (_| |
(_)(_) (_)`\___/'`\__,_)`\__,_)
{Fore.LIGHTYELLOW_EX}Created by RoadJDK{Fore.RESET}
""")
print(f"{Fore.CYAN}Welcome to iRoad TwitchTools!{Fore.RESET}")
print(f"{Fore.MAGENTA}Please select one of the following options:{Fore.RESET}")
print(f"{Fore.RED}1{Fore.RESET} - Account Creator")
print(f"{Fore.RED}2{Fore.RESET} - Stream Annoyance")
print(f"{Fore.RED}3{Fore.RESET} - Follower Sender")
print(f"{Fore.RED}4{Fore.RESET} - Stream Spamer")
print(f"{Fore.RED}5{Fore.RESET} - Twitch Viewbot")
print(f"{Fore.RED}6{Fore.RESET} - Clip Maker")
print(f"{Fore.RED}7{Fore.RESET} - Points Farmer")

#check input
while(True):
    selection = input()
    try:
        val = int(selection)
        if (val in range(0,8)):
            print()
            break
        else:
            print("not a valid selection...")
    except ValueError:
        print("not a valid selection...")

if (selection == '1'):
    print(f"{Fore.LIGHTBLUE_EX}Step 1:{Fore.RESET} open your browser fullscreen 1920x1080 on your main screen")
    print(f'{Fore.LIGHTBLUE_EX}Step 2:{Fore.RESET} In the first tab open "twitch.tv", in the second "muellmail.com"')
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
    print("not implemented yet")
    
if (selection == '3'):
    print("not implemented yet")

if (selection == '4'):
    print("not implemented yet")

if (selection == '5'):
    print("not implemented yet")

if (selection == '6'):
    print("not implemented yet")

if (selection == '7'):
    print("not implemented yet")
