from telethon import events 
from asyncio import wait 
# import re, bs4, requests


from userbot.events import register 

# def gang(input_text)
#     params = {"translatetext": input_text}
#     target_url = "http://www.gizoogle.net/textilizer.php"
#     resp = requests.post(target_url, data=params)
#     soup_input = re.sub("/name=translatetext[^>]*>/", 'name="translatetext" >', resp.text)
#     soup = bs4.BeautifulSoup(soup_input, "lxml")
#     giz = soup.find_all(text=True)
#     giz_text = giz[37].strip("\r\n")
#     return giz_text

@client.on(events.NewMessage(pattern='(?i)hello.+'))
async def handler(event):
    rep = gang("hey what's up?")
    await event.reply(rep)
