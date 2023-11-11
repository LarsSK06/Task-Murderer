import os
import sys
import json
from time import sleep
from pathvalidate import is_valid_filename

config = "settings.json"
tickDelay = 3

installStartBatch = str.lower(input("\nDo you want to install startup batch? (y/N) > ")) == "y"
if installStartBatch:
    fileName = ""
    while True:
        fileName = input("What should the batch file be called? > ")
        if not is_valid_filename(fileName):
            print("File name is not valid!")
            continue
        break
    print("Installing startup batch file...")
    try:
        path = os.path.expanduser("~") + f"\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\{fileName}.bat"
        with open(path, mode="w") as file:
            file.write(sys.executable)
            file.close()
        print("Startup batch file was created successfully!")
    except:
        print("There was a problem with installing the startup batch file!")

os.system("@tasklist")
print("^ (examples) ^")
imageName = input("What is the image name of the task you want to murder? > ")

while True:
    delay = input("\nHow much of a delay should be between murders in seconds? > ")
    try:
        float(delay)
        delay = float(delay)
        break
    except:
        print("Invalid number input!")
        continue

if str.lower(input("\nDo you want to set a custom tick delay? (y/N) > ")) == "y":
    while True:
            tickDelayInput = input("How much of a delay should the tick have? > ")
            try:
                float(tickDelayInput)
                tickDelay = float(tickDelayInput)
                break
            except:
                print("Invalid number input!")
                continue

print(f"\nCreating \"{config}\"...")
with open(config, mode="w") as file:
    file.write(json.dumps({
        imageName: imageName,
        delay: delay,
        tickDelay: tickDelay
    }, indent=4))
    file.close()
    print(f"File \"{config}\" was created successfully! This should not be edited manually.")

runNow = not str.lower(input("\nShould the program run now? (Y/n) > ")) == "n"
if runNow:
    if os.path.exists("main.exe"):
        os.system("main.exe")
    else: print("File \"main.exe\" does not exist!")