# Copyright (C) 2022 Unknown <https://github.com/unknownkz/universe>
# All Rights Reserved
#
# Credits : @unknownkz (axel)
# This file is a part of < https://github.com/unknownkz/universe/ >
# PLease read the GNU Affero General Public License in;
# < https://www.github.com/unknownkz/universe/main/LICENSE/ >

from calendar import month
from datetime import datetime

from .. import univ
from ..UniverseLogger import tz
from ..EquipmentTools import deleted
from ..Configuration import MultiVerse

category = "tools"

u = MultiVerse.Trigger

calendar_command = f"""
**Command Guide ›**

__Calendar for this years.__

`{u}calendar -now`
`{u}calendar -m <month>`

**Example:**
Run › `{u}calendar -m jan/januari/january`

Choose a month.
"""


@univ.universe_cloud(
    pattern=r"calendar(?: |$)(-now|-m)?(?: |$)(.*)",
    command=("calendar -now|-m", category),
)
async def _(incident):
    m1 = ["jan", "januari", "january"]
    m2 = ["feb", "februari", "february"]
    m3 = ["mar", "maret", "march"]
    m4 = ["apr", "april"]
    m5 = ["may", "mei"]
    m6 = ["jun", "juni", "june"]
    m7 = ["jul", "juli", "july"]
    m8 = ["aug", "agustus", "august"]
    m9 = ["sep", "september"]
    m10 = ["oct", "oktober", "october"]
    m11 = ["nov", "november"]
    m12 = ["dec", "desember", "december"]
    point = incident.pattern_match.group(1)
    commander = incident.pattern_match.group(2)
    if point == "-now":
        mo = datetime.now().month
        ye = datetime.now().year
        da = datetime.now(tz).strftime("Date : %d/%m/%Y\nTime : %I:%M %p")
        ca = month(ye, mo, 2, 1)
        date_and_time = (
            f"<strong><i>The calendar for this month is:</i></strong>\n\n"
            f"<code>{ca}</code>\n"
            f"Now\n<code>{da}</code>"
        )
        await incident.reply(date_and_time, parse_mode="html", silent=True)

    elif point == "-m" and commander in m1:
        mo = 1
        ye = datetime.now().year
        ca = month(ye, mo, 2, 1)
        da = datetime.now(tz).strftime("Date : %d/%m/%Y\nTime : %I:%M %p")
        date_and_time = (
            f"<strong><i>The month you requested:</i></strong>\n\n"
            f"<code>{ca}</code>\n"
            f"Now\n<code>{da}</code>"
        )
        await incident.reply(date_and_time, parse_mode="html", silent=True)

    elif point == "-m" and commander in m2:
        mo = 2
        ye = datetime.now().year
        ca = month(ye, mo, 2, 1)
        da = datetime.now(tz).strftime("Date : %d/%m/%Y\nTime : %I:%M %p")
        date_and_time = (
            f"<strong><i>The month you requested:</i></strong>\n\n"
            f"<code>{ca}</code>\n"
            f"Now\n<code>{da}</code>"
        )
        await incident.reply(date_and_time, parse_mode="html", silent=True)

    elif point == "-m" and commander in m3:
        mo = 3
        ye = datetime.now().year
        ca = month(ye, mo, 2, 1)
        da = datetime.now(tz).strftime("Date : %d/%m/%Y\nTime : %I:%M %p")
        date_and_time = (
            f"<strong><i>The month you requested:</i></strong>\n\n"
            f"<code>{ca}</code>\n"
            f"Now\n<code>{da}</code>"
        )
        await incident.reply(date_and_time, parse_mode="html", silent=True)

    elif point == "-m" and commander in m4:
        mo = 4
        ye = datetime.now().year
        ca = month(ye, mo, 2, 1)
        da = datetime.now(tz).strftime("Date : %d/%m/%Y\nTime : %I:%M %p")
        date_and_time = (
            f"<strong><i>The month you requested:</i></strong>\n\n"
            f"<code>{ca}</code>\n"
            f"Now\n<code>{da}</code>"
        )
        await incident.reply(date_and_time, parse_mode="html", silent=True)

    elif point == "-m" and commander in m5:
        mo = 5
        ye = datetime.now().year
        ca = month(ye, mo, 2, 1)
        da = datetime.now(tz).strftime("Date : %d/%m/%Y\nTime : %I:%M %p")
        date_and_time = (
            f"<strong><i>The month you requested:</i></strong>\n\n"
            f"<code>{ca}</code>\n"
            f"Now\n<code>{da}</code>"
        )
        await incident.reply(date_and_time, parse_mode="html", silent=True)

    elif point == "-m" and commander in m6:
        mo = 6
        ye = datetime.now().year
        ca = month(ye, mo, 2, 1)
        da = datetime.now(tz).strftime("Date : %d/%m/%Y\nTime : %I:%M %p")
        date_and_time = (
            f"<strong><i>The month you requested:</i></strong>\n\n"
            f"<code>{ca}</code>\n"
            f"Now\n<code>{da}</code>"
        )
        await incident.reply(date_and_time, parse_mode="html", silent=True)

    elif point == "-m" and commander in m7:
        mo = 7
        ye = datetime.now().year
        ca = month(ye, mo, 2, 1)
        da = datetime.now(tz).strftime("Date : %d/%m/%Y\nTime : %I:%M %p")
        date_and_time = (
            f"<strong><i>The month you requested:</i></strong>\n\n"
            f"<code>{ca}</code>\n"
            f"Now\n<code>{da}</code>"
        )
        await incident.reply(date_and_time, parse_mode="html", silent=True)

    elif point == "-m" and commander in m8:
        mo = 8
        ye = datetime.now().year
        ca = month(ye, mo, 2, 1)
        da = datetime.now(tz).strftime("Date : %d/%m/%Y\nTime : %I:%M %p")
        date_and_time = (
            f"<strong><i>The month you requested:</i></strong>\n\n"
            f"<code>{ca}</code>\n"
            f"Now\n<code>{da}</code>"
        )
        await incident.reply(date_and_time, parse_mode="html", silent=True)

    elif point == "-m" and commander in m9:
        mo = 9
        ye = datetime.now().year
        ca = month(ye, mo, 2, 1)
        da = datetime.now(tz).strftime("Date : %d/%m/%Y\nTime : %I:%M %p")
        date_and_time = (
            f"<strong><i>The month you requested:</i></strong>\n\n"
            f"<code>{ca}</code>\n"
            f"Now\n<code>{da}</code>"
        )
        await incident.reply(date_and_time, parse_mode="html", silent=True)

    elif point == "-m" and commander in m10:
        mo = 10
        ye = datetime.now().year
        ca = month(ye, mo, 2, 1)
        da = datetime.now(tz).strftime("Date : %d/%m/%Y\nTime : %I:%M %p")
        date_and_time = (
            f"<strong><i>The month you requested:</i></strong>\n\n"
            f"<code>{ca}</code>\n"
            f"Now\n<code>{da}</code>"
        )
        await incident.reply(date_and_time, parse_mode="html", silent=True)

    elif point == "-m" and commander in m11:
        mo = 11
        ye = datetime.now().year
        ca = month(ye, mo, 2, 1)
        da = datetime.now(tz).strftime("Date : %d/%m/%Y\nTime : %I:%M %p")
        date_and_time = (
            f"<strong><i>The month you requested:</i></strong>\n\n"
            f"<code>{ca}</code>\n"
            f"Now\n<code>{da}</code>"
        )
        await incident.reply(date_and_time, parse_mode="html", silent=True)

    elif point == "-m" and commander in m12:
        mo = 12
        ye = datetime.now().year
        ca = month(ye, mo, 2, 1)
        da = datetime.now(tz).strftime("Date : %d/%m/%Y\nTime : %I:%M %p")
        date_and_time = (
            f"<strong><i>The month you requested:</i></strong>\n\n"
            f"<code>{ca}</code>\n"
            f"Now\n<code>{da}</code>"
        )
        await incident.reply(date_and_time, parse_mode="html", silent=True)

    else:
        await incident.reply(calendar_command)

    return await deleted(incident)
