import asyncio
from ahk import AHK
ahk = AHK()

async def act(duration):
    ahk.key_down('s')
    await asyncio.sleep(duration)
    ahk.key_up('s')
