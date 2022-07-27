import asyncio
from ahk import AHK
ahk = AHK()

async def act():
    ahk.key_down('Space')
    ahk.key_up('Space')
