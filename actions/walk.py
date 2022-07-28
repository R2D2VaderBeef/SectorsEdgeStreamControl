import os
import asyncio
from ahk import AHK
ahk = AHK()
import random

async def act():
    if (os.getenv("CMD_WALK_enabled") == "false"):
        return

    prob = float(os.getenv("CMD_WALK_probability"))
    rando = random.randint(1, 100) / 100

    print("walk.act() => Prob: " + str(prob) + " Random: " + str(rando))

    if rando <= prob:
        print("Acted: walk")
        duration = float(os.getenv("CMD_WALK_duration"))
        ahk.key_down('w')
        await asyncio.sleep(duration)
        ahk.key_up('w')
