import asyncio
import datetime
from telethon import events
from telethon.tl import functions, types


@borg.on(events.NewMessage(outgoing=True))
async def ola(event):
    await borg.send_mesage(Config.PLUGIN_CHANNEL,
             "Yo bro hello!! What's up XD")
            

    
