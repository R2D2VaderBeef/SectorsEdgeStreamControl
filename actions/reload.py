import asyncio
from ahk import AHK
ahk = AHK()
import random

async def act(prob):
    rando = random.randint(1, 100) / 100
    print("reload.act() => Prob: " + str(prob) + " Random: " + str(rando))
    if rando <= prob:
        print("Reloaded.")
        ahk.key_down('r')
        ahk.key_up('r')