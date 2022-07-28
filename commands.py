# Setup
import actions
import os

# Set all the command variables
walk = os.getenv("CMD_WALK_command")

# Check if the command matches any of the actions, and if so, run it. 
async def handleCommand(command):
        if command == walk:
            await actions.walk.act()
        elif command == "left":
            await left.act(0.2)
        elif command == "right":
            await right.act(0.2)
        elif command == "back":
            await back.act(1)
        elif command == "crouch":
            await crouch.act(0.8)
        elif command == "jump":
            await jump.act()    
        elif command == "shoot":
            await shoot.act(1/2)
        elif command == "scope":
            await scope.act(1.5)
        elif command == "reload":
            await reload.act(1/4)
        elif command == "melee":
            await melee.act()
        elif command == "grenade":
            await grenade.act(1/5)
        else:
            print("Not a valid command, skipping.")
