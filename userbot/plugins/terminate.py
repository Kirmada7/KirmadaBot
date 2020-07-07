

from telethon import events
import asyncio
import os
import sys
from userbot.utils import admin_cmd


# @borg.on(admin_cmd("restart"))
# async def _(event):
#     if event.fwd_from:
#         return
#     # await asyncio.sleep(2)
#     # await event.edit("Restarting [██░] ...\n`.ping` me or `.help` to check if I am online")
#     # await asyncio.sleep(2)
#     # await event.edit("Restarting [███]...\n`.ping` me or `.help` to check if I am online")
#     # await asyncio.sleep(2)
#     await event.edit("Restarted. `.alive` me or `.help` to check if I am online")
#     await borg.disconnect()
#     # https://archive.is/im3rt
#     os.execl(sys.executable, sys.executable, *sys.argv)
#     # You probably don't need it but whatever
#     quit()


@borg.on(admin_cmd("^.stop"))
async def _(event):
    if event.fwd_from:
        return
    # await asyncio.sleep(2)
    # await event.edit("Restarting [██░] ...\n`.ping` me or `.help` to check if I am online")
    # await asyncio.sleep(2)
    # await event.edit("Restarting [███]...\n`.ping` me or `.help` to check if I am online")
    # await asyncio.sleep(2)
    await event.edit("Restarted. `.alive` me or `.help` to check if I am online")
    await borg.disconnect()
    # https://archive.is/im3rt
    os.execl(sys.executable, sys.executable, *sys.argv)
    # You probably don't need it but whatever
    quit()
