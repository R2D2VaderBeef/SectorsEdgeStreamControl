import time
import asyncio
import os

# import every movement file
from actions import walk
from actions import left
from actions import right

# Sample way to run an action
#async def test():
#    await asyncio.sleep(5)
#    await walk.act(0.5)
# asyncio.run(test())

async def handleMessage(message):
    print("Handling Message: " + message)
    if message == "walk":
        await walk.act(0.5)
    elif message == "left":
        await left.act(0.2)
    elif message == "right":
        await right.act(0.2)
    else:
        print("Not a command.")

# garbo i wrote to test this code
async def testFunc():
    task1 = asyncio.create_task(handleMessage("walk"))
    task2 = asyncio.create_task(handleMessage("left"))
    task3 = asyncio.create_task(handleMessage("right"))
    await asyncio.sleep(5)
    await task1
    await asyncio.sleep(3)
    await task2
    await asyncio.sleep(0.5)
    await task3

asyncio.run(testFunc())

