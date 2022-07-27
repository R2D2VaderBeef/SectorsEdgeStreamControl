# Setup
import os
import actions
import asyncio

async def handleCommand(command):
    match command:
        case "walk":
            print("walk")
        case "left":
            print("left")
        case "right":
            print("right")
        case "back":
            print("back")
        case "crouch":
            print("crouch")
        case "jump":
            print("jump")
        case "shoot":
            print("shoot")
        case "scope":
            print("scope")
        case "reload":
            print("reload")
        case "melee":
            print("melee")
        case "grenade":
            print("grenade")
        case _:
            print("Not a valid command, skipping.")
