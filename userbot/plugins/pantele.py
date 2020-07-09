import asyncio
import random
import string
from asyncio import wait
from userbot.events import register

@register(outgoing=True, pattern="^.pan")
async def generate(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        name = str(message[5:])
        space_fnd = name.find(" ")
        space_fnd = space_fnd + 1
        sr_wrd = str(name[space_fnd:space_fnd + 1]).upper()

        mid = random.randint(1111, 9999)

        letter = string.ascii_letters
        start = ''.join(random.choice(letter) for i in range(3)).upper()

        letterlst = string.ascii_letters
        last = random.choice(letterlst).upper()

        date = random.randint(1, 31)
        month = random.randint(1, 12)
        year = random.randint(1950, 2000)
        p = "P"

        pan = "❤️ PAN DETAIL ❤️\n" + "\nName: " + name + "\nDate of Birth: " + str(date) + "/" + str(month) + "/" + str(
            year) + "\nPAN Number: " + "{one}{p}{two}{three}{four}".format(one=start, two=sr_wrd, three=mid, four=last, p=p)
        # print("Name: " + name)
        # print("Date of Birth: " + str(date) + "/" + str(month) + "/" + str(year))
        # print("PAN Number: " + "{one}{two}{three}{four}".format(one=start, two=sr_wrd, three=mid, four=last))

        await e.respond(pan)
        await e.delete()
        if LOGGER:
            await e.client.send_message(
                LOGGER_GROUP,
                "#PAN \n\n"
                "PAN generated succesfully"
                )

