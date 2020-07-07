
from telethon import events
from datetime import datetime
import asyncio
from asyncio import wait
import time


from userbot.events import register

@register(outgoing=True, pattern="^.breakspam")
async def tmeme(e):
    tspam = str(e.text[11:])
    message = tspam.replace(" ", "")
    for letter in message:
        await e.respond(letter)
    await e.delete()

@register(outgoing=True, pattern="^.start")
async def spammer(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        counter = int(message[7:9])
        spam_message = str(e.text[9:])
        await asyncio.wait([e.respond(spam_message) for i in range(counter)])
        await e.delete()
        if LOGGER:
            await e.client.send_message(
                LOGGER_GROUP,
                "#SPAM \n\n"
                "Spam was executed successfully"
                )
                               
@register(outgoing=True, pattern="^.bigstart")
async def bigspam(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        counter = int(message[10:14])
        spam_message = str(e.text[14:])
        for i in range(1, counter):
            await e.respond(spam_message)
        await e.delete()
        if LOGGER:
            await e.client.send_message(
                LOGGER_GROUP,
                "#BIGSPAM \n\n"
                "Bigspam was executed successfully"
                )
        
        
@register(outgoing=True, pattern="^.picspam")
async def tiny_pic_spam(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        text = message.split()
        counter = int(text[1])
        link = str(text[2])
        for i in range(1, counter):
            await e.client.send_file(e.chat_id, link)
        await e.delete()
        if LOGGER:
            await e.client.send_message(
                LOGGER_GROUP,
                "#PICSPAM \n\n"
                "PicSpam was executed successfully"
                )

@register(outgoing=True, pattern="^.delaystart")
async def bigspam(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        counter = int(message[12:15])
        t = int(message[15:17])
        spam_message = str(e.text[17:])
        for i in range(1, counter):
            time.sleep(t)
            await e.respond(spam_message)
        await e.delete()
        if LOGGER:
            await e.client.send_message(
                LOGGER_GROUP,
                "#BIGSPAM \n\n"
                "Bigspam was executed successfully"
                )
            
@command(pattern="^.disc")
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Turning KirmadaBot off ...Manually turn me on later. To turn on type .connect")
    await borg.disconnect()
   
@command(pattern="^.connect")
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Alright, KirmaadaBot up and running.)
    await borg.connect()
   
