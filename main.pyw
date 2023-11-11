import os
import json
from time import sleep

config = "settings.json"

tickDelay = 3
imageName = ""
delay = 3

for i in range(1):
    if os.path.exists(config):
        with open(config, mode="r") as file:
            data = {}
            try: data = json.loads(file.read())
            except:
                file.close()
                break
            if not "tickDelay" in data:
                file.close()
                break
            try:
                float(data["tickDelay"])
                tickDelay = float(data["tickDelay"])
                file.close()
                break
            except:
                file.close()
                break

while True:
    if not os.path.exists(config):
        sleep(tickDelay)
        continue
    break

while True:
    with open(config, mode="r") as file:
        data = {}
        try: data = json.loads(file.read())
        except:
            sleep(tickDelay)
            file.close()
            continue
        if not "imageName" in data:
            sleep(tickDelay)
            file.close()
            continue
        if not "delay" in data:
            sleep(tickDelay)
            file.close()
            continue
        try: float(data["delay"])
        except:
            sleep(tickDelay)
            file.close()
            continue
        imageName = data["imageName"]
        delay = float(data["delay"])
        file.close()
        break

while True:
    os.system("taskkill /f /im " + imageName)
    sleep(delay)