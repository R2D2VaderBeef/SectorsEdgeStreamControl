import asyncio
from ahk import AHK
ahk = AHK()

async def act():
    ahk.key_down('f')
    ahk.key_up('f')
