# Copyright (C) 2022 Unknown <https://github.com/unknownkz/universe>
# All Rights Reserved
#
# Credits : @unknownkz (axel)
# This file is a part of < https://github.com/unknownkz/universe/ >
# PLease read the GNU Affero General Public License in;
# < https://www.github.com/unknownkz/universe/main/LICENSE/ >

import rsa
import packaging
from textwrap import indent
from platform import python_version
from datetime import datetime
from time import time as t
from telethon import __version__
from py._version import version

from .. import univ, start_time, __version, __license
from ..Configuration import MultiVerse
from ..EquipmentTools import deleted, tf
from ..UniverseLogger import tz

category = "core"


@univ.universe_cloud(
    pattern="active",
    command=("active", category),
)
async def _(incident):
    my_uptime = tf((t() - start_time) * 1000)
    time_stamp = datetime.now(tz).strftime("%I:%M:%S %p UTC%z")
    text_active = "<i>“We are connected on the inside.”</i>\n"
    text_active += "-----\n"
    text_active += (
        "|  › <code>Uptime:</code> <code>" + str(my_uptime) + "</code> \n"
    )
    text_active += "|  › <code>Py:</code> <code>" + str(version) + "</code> \n"
    text_active += (
        "|  › <code>RSA:</code> <code>" + str(rsa.__version__) + "</code> \n"
    )
    text_active += (
        "|  › <code>Python:</code> <code>"
        + str(python_version())
        + "</code> \n"
    )
    text_active += (
        "|  › <code>Packaging:</code> <code>"
        + str(packaging.__version__)
        + "</code> \n"
    )
    text_active += (
        "|  › <code>Telethon:</code> <code>" + str(__version__) + "</code> \n"
    )
    text_active += (
        "|  › <code>Version:</code> <code>" + str(__version) + "</code> \n"
    )
    text_active += (
        "|  › <code>Repository:</code> "
        + "<b><a href='https://github.com/unknownkz/universe'>click here</a></b>\n"
    )
    text_active += (
        "|  › <code>Author:</code> "
        + "<b><a href='https://t.me/joinchat/ML1yGH-is_5jYzY1'>click here</a></b>\n"
    )
    text_active += (
        "|  › <code>License:</code> "
        + "<b><a href='https://opensource.org/licenses/GPL-3.0>'>"
        + str(__license)
        + "</a></b>\n"
    )
    text_active += "-----\n"
    text_active += (
        "<code>"
        + time_stamp
        + "</code> \n<code>"
        + MultiVerse.TZ
        + "</code>\n"
    )
    text_active += "-----\n"
    text_active += (
        "<b>Powered by </b>"
        + "<b><a href='https://t.me/kastaid'>ID | カースト</a></b>\n"
    )
    wrp = indent(text_active, " ", lambda line: True)
    await deleted(incident)
    await univ.send_file(
        incident.chat_id,
        file=MultiVerse.Info_Active,
        caption=wrp,
        parse_mode="html",
    )
