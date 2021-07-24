

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


if (selection == 1):
    print()

if (selection == 2):
    print()
    
if (selection == 3):
    print()
