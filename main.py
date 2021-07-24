from src.creator import create

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

print("Hi")
print()
print("Welcome to TwitchTools!")
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
    print("please put some names in the generated names.txt file (one name per line) - press keyboard when ready")
    input()
    while(True):
        print("how many accounts should be created? (0 is forever)")
        count = input()
        try:
            val = int(count)
            if (val in range(0,4)):
                break
            else:
                print("not a valid number...")
        except ValueError:
            print("not a valid number...")
    for remaining in range(5,0,-1):
        sys.stdout.write("\r{:2d} seconds remaining...".format(remaining))
        sys.stdout.flush()
        time.sleep(1)
    print("Let's Start!")
    create(int(count))

if (selection == '2'):
    print(22)
    
if (selection == '3'):
    print(33)
