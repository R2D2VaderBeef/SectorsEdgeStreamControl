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
from actions import scope

# Sample way to run an action
#async def test():
#    await asyncio.sleep(5)
#    await walk.act(0.5)
# asyncio.run(test())

# Decimals / Integers are durations (how long to hold the action for), Fractions are probabilities (for actions that may screw you over). 
# Some have one, some have neither. 
# This is just done to tell the difference between them. You can input any type of number into all of these fields. 
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
    elif message == "scope":
        await scope.act(1.5)
    else:
        print("Not a command.")

# garbo i wrote to test this code
async def testFunc():
    task1 = asyncio.create_task(handleMessage("scope"))
    task2 = asyncio.create_task(handleMessage("shoot"))
    await task1
    await task2

asyncio.run(testFunc())

