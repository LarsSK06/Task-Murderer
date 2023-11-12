# Package import

import json
from time import sleep
from os.path import exists
from subprocess import call



# Variables

config = "settings.json"
tick = 3

imageName = ""
delay = 0



# Configuration file assurance

while True:
    if not exists(config):
        sleep(tick)
        continue
    with open(config, mode="r") as file:
        try:
            data = json.loads(file.read())
            file.close()
            if not "imageName" in data:
                sleep(tick)
                continue
            if not "delay" in data:
                sleep(tick)
                continue
            try: float(data["delay"])
            except:
                sleep(tick)
                continue
            imageName = str(data["imageName"])
            delay = float(data["delay"])
            break
        except:
            sleep(tick)
            continue



# Virus murder loop

while True:
    call("taskkill /f /im " + imageName, creationflags=0x08000000)
    sleep(delay)