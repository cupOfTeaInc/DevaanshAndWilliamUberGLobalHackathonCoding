import imp
import json
from requests import post
from datetime import datetime
import asyncio

running = True

SCHEDULE_FILE_PATH  : str = "schedule.json"
HOOKS_FILE_PATH     : str = "hooks.json"
REFRESH_RATE        : int = 60

schedule            : dict = json.load(open(SCHEDULE_FILE_PATH))
hooks               : dict = json.load(open(HOOKS_FILE_PATH))

async def trigger_hook(device, turn_on : int = 1):
    if turn_on:    post(hooks["hook_base"]+hooks["devices"][device]["ON"]) #if int returs true if the value is nonzero
    else      :    post(hooks["hook_base"]+hooks["devices"][device]["OFF"])

async def execute_schedule(device : str) :
    while running:
        for i in schedule[device]:
            now = datetime.now()
            increments_since_midnight = int((now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()/3000) #300 = 60seconds/minute * 5minutes/increment
            if increments_since_midnight == i:
                await trigger_hook(device, schedule["device"][i])
    await asyncio.sleep(REFRESH_RATE)

async def execute_all():
    for device in hooks["devices"].keys():
        await execute_schedule(device)

def main():
    asyncio.run(execute_schedule("AC"))

if __name__ == "__main__":
    main()