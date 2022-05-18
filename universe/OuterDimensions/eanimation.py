# Copyright (C) 2022 Unknown <https://github.com/unknownkz/universe>
# All Rights Reserved
#
# Credits : @unknownkz (axel)
# This file is a part of < https://github.com/unknownkz/universe/ >
# PLease read the GNU Affero General Public License in;
# < https://www.github.com/unknownkz/universe/main/LICENSE/ >

from time import sleep
from contextlib import suppress
from collections import deque as que

from .. import univ
from ..EquipmentTools import deleted
from ..Configuration import MultiVerse

category = "fun"

u = MultiVerse.Trigger

eanimation_command = f"""
**Command Guide ›**

__Emoji's Animation.__

`{u}emoji -a <list name>`
`{u}emoji -list <see list>`

**Example:**
Run › `{u}emoji -a moon | love`

Choose ur emoji animation.
"""

list_name_emoji = f"""
**List Name Emoji**

Moon = mn | moon | mun | bulan
Love = lv | love | lov | luv | lope | cinta
Flower = fl | flower | plower | bunga
Fruit = fr | fruit | fruits | pruit | buah
Earth = et | earth | bumi
Weather = wt | weather | weathers | cuaca
Clock = ck | clock | jam
Monkey = mky | monkey | monyet

| = or ( alias )

**Example:**
Run › `{u}emoji -a et`

Choose ur emoji animation.
"""


@univ.universe_cloud(
    pattern=r"emoji(?: |$)(-a|-list)?(?: |$)(.*)",
    command=("emoji -list|-a <name>", category),
)
async def _(incident):
    with suppress(BaseException):
        list_emoji_moon = ["mn", "moon", "mun", "bulan"]
        list_emoji_love = ["lv", "love", "lov", "luv", "lope", "cinta"]
        list_emoji_flower = ["fl", "flower", "plower", "bunga"]
        list_emoji_fruit = ["fr", "fruit", "fruits", "pruit", "buah"]
        list_emoji_earth = ["et", "earth", "bumi"]
        list_emoji_weather = ["wt", "weather", "weathers", "cuaca"]
        list_emoji_clock = ["ck", "clock", "jam"]
        list_emoji_monkey = ["mky", "monkey", "monyet"]

        mn = que(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
        lv = que(list("❤️🧡💛💚💙💜🖤💕💞💓💗💖💘💝"))
        fl = que(list("🌼🌻🌺🌹🌸🌷"))
        fr = que(list("🍉🍓🍇🍎🍍🍐🍌"))
        et = que(list("🌏🌍🌎🌎🌍🌏🌍🌎"))
        wt = que(list("☀️🌤⛅️🌥☁️🌧⛈"))
        ck = que(list("🕙🕘🕗🕖🕕🕔🕓🕒🕑🕐🕛"))
        mky = que(list("🙈🙉🙈🙉🙈🙉🙈🙉"))

        point = incident.pattern_match.group(1)
        __emoji = incident.pattern_match.group(2)

        if point == "-list":
            await incident.reply(list_name_emoji)

        elif point == "-a" and __emoji in list_emoji_moon:
            for _ in range(32):
                sleep(0.1)
                await incident.edit("".join(mn))
                mn.rotate(1)

        elif point == "-a" and __emoji in list_emoji_love:
            for _ in range(32):
                sleep(0.1)
                await incident.edit("".join(lv))
                lv.rotate(1)

        elif point == "-a" and __emoji in list_emoji_flower:
            for _ in range(32):
                sleep(0.1)
                await incident.edit("".join(fl))
                fl.rotate(1)

        elif point == "-a" and __emoji in list_emoji_fruit:
            for _ in range(32):
                sleep(0.1)
                await incident.edit("".join(fr))
                fr.rotate(1)

        elif point == "-a" and __emoji in list_emoji_earth:
            for _ in range(32):
                sleep(0.1)
                await incident.edit("".join(et))
                et.rotate(1)

        elif point == "-a" and __emoji in list_emoji_weather:
            for _ in range(32):
                sleep(0.1)
                await incident.edit("".join(wt))
                wt.rotate(1)

        elif point == "-a" and __emoji in list_emoji_clock:
            for _ in range(32):
                sleep(0.1)
                await incident.edit("".join(ck))
                ck.rotate(1)

        elif point == "-a" and __emoji in list_emoji_monkey:
            for _ in range(32):
                sleep(0.1)
                await incident.edit("".join(mky))
                mky.rotate(1)

        else:
            await incident.reply(eanimation_command)

        return await deleted(incident)
