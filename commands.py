# Setup
import os
import asyncio
from ahk import AHK
ahk = AHK()
import random

# Set all the command variables
walk = os.getenv("CMD_WALK_command")
left = os.getenv("CMD_LEFT_command")
right = os.getenv("CMD_RIGHT_command")
back = os.getenv("CMD_BACK_command")
crouch = os.getenv("CMD_CROUCH_command")
jump = os.getenv("CMD_JUMP_command")
shoot = os.getenv("CMD_SHOOT_command")
scope = os.getenv("CMD_SCOPE_command")
reload = os.getenv("CMD_RELOAD_command")
melee = os.getenv("CMD_MELEE_command")
grenade = os.getenv("CMD_GRENADE_command")

# Check if the command matches any of the actions, and if so, run it. 
async def handleCommand(command):
        if command == walk:
            await act("WALK")
        elif command == left:
            await act("LEFT")
        elif command == right:
            await act("RIGHT")
        elif command == back:
            await act("BACK")
        elif command == crouch:
            await act("CROUCH")
        elif command == jump:
            await act("JUMP")    
        elif command == shoot:
            await act("SHOOT")
        elif command == scope:
            await act("SCOPE")
        elif command == reload:
            await act("RELOAD")
        elif command == melee:
            await act("MELEE")
        elif command == grenade:
            await act("GRENADE")
        else:
            print("Not a valid command, skipping.")

# Simple Button Press commands
# Check if the command is enabled and check if a random number is less than or equal to the probability setting. If both are true, the command will run.
async def act(command):
    if (os.getenv("CMD_{cmd}_enabled".format(cmd = command)) == "false"):
        return

    prob = float(os.getenv("CMD_{cmd}_probability".format(cmd = command)))
    rando = random.randint(1, 100) / 100

    print("Command " + command + " => Prob: " + str(prob) + " Random: " + str(rando))

    if rando <= prob:
        print("Acted: " + command)
        duration = float(os.getenv("CMD_{cmd}_duration".format(cmd = command)))
        key = os.getenv("CMD_{cmd}_input".format(cmd = command))
        ahk.key_down(key)
        await asyncio.sleep(duration)
        ahk.key_up(key)
