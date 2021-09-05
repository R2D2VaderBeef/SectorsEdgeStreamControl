import asyncio
from ahk import AHK
ahk = AHK()

async def act(duration):
    ahk.key_down('a')
    await asyncio.sleep(duration)
    ahk.key_up('a')
