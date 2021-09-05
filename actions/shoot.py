import asyncio
from ahk import AHK
ahk = AHK()
import random

async def act(prob):
    rando = random.randint(1, 100) / 100
    print("shoot.act() => Prob: " + str(prob) + " Random: " + str(rando))
    if rando <= prob:
        print("Shot.")
        ahk.key_down('LButton')
        ahk.key_up('LButton')