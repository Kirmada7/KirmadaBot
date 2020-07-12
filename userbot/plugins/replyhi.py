import asyncio
import datetime
from telethon import events
from telethon.tl import functions, types


@borg.on(events.NewMessage(outgoing=True))
async def ola(event):
    message_rec = event.message.message
    if "hi" in message_rec:
        try:
            await borg.send_mesage(Config.PLUGIN_CHANNEL,
             "Yo bro hello!! What's up XD")

        except:
            borg.send_message(  
                event.chat_id,"Error",
                reply_to=event.message.id,
                silent=True
            )

