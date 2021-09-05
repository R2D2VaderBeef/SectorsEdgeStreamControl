import time
import asyncio
import os

# import every movement file
from actions import walk
from actions import left
from actions import right
from actions import back
from actions import crouch
from actions import jump
from actions import shoot

# Sample way to run an action
#async def test():
#    await asyncio.sleep(5)
#    await walk.act(0.5)
# asyncio.run(test())

# Decimals / Integers are durations (how long to hold the action for), fractions are probabilities (for actions that may screw you over). 
# Some have one, some have neither.

async def handleMessage(message):
    print("Handling Message: " + message)
    if message == "walk":
        await walk.act(0.5)
    elif message == "left":
        await left.act(0.2)
    elif message == "right":
        await right.act(0.2)
    elif message == "back":
        await back.act(1)
    elif message == "crouch":
        await crouch.act(0.8)
    elif message == "jump":
        await jump.act()    
    elif message == "shoot":
        await shoot.act(1/4)
    else:
        print("Not a command.")

# garbo i wrote to test this code
async def testFunc():
    task1 = asyncio.create_task(handleMessage("shoot"))
    await task1

asyncio.run(testFunc())

