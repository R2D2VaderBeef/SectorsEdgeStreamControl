import asyncio
from ahk import AHK
ahk = AHK()
import random

async def act(prob):
    rando = random.randint(1, 100) / 100
    print("grenade.act() => Prob: " + str(prob) + " Random: " + str(rando))
    if rando <= prob:
        print("Threw a grenade.")
        ahk.key_down('g')
        ahk.key_up('g')