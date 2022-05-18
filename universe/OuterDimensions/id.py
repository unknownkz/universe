# Copyright (C) 2022 Unknown <https://github.com/unknownkz/universe>
# All Rights Reserved
#
# Credits : @unknownkz (axel)
# This file is a part of < https://github.com/unknownkz/universe/ >
# PLease read the GNU Affero General Public License in;
# < https://www.github.com/unknownkz/universe/main/LICENSE/ >

from textwrap import indent

from .. import univ
from ..EquipmentTools import deleted

category = "service"


@univ.universe_cloud(
    pattern="id",
    command=("id", category),
    groups_only=True,
)
async def _(incident):
    replied = await incident.get_reply_message()
    if replied:
        if not replied.forward:
            user_id = replied.sender.id
            if replied.sender.username:
                name = "@" + replied.sender.username
            else:
                name = "<b>" + replied.sender.first_name + "</b>"
        else:
            user_id = replied.forward.sender.id
            if replied.forward.sender.username:
                name = "@" + replied.forward.sender.username
            else:
                name = "<b>" + replied.forward.sender.first_name + "</b>"

        text_id = "<b>Name:</b> " + str(name)
        text_id += "\n<b>User ID:</b> <code>" + str(user_id) + "</code>"
        text_id += "\n<b>Message ID:</b> <code>" + str(replied.id) + "</code>"
        text_id += (
            "\n<b>Chat ID:</b> <code>" + str(incident.chat_id) + "</code>"
        )
        text_id += "\n<b>Date:</b> <code>" + str(replied.date) + "</code>"
        text_id += "\n<b>TimeZone:</b> <i>(UTC+0)</i>"
        text_id += "\n<b>Out:</b> <code>" + str(replied.out) + "</code>"
        text_id += "\n<b>Silent:</b> <code>" + str(replied.silent) + "</code>"
        text_id += (
            "\n<b>Scheduled:</b> <code>"
            + str(replied.from_scheduled)
            + "</code>"
        )
        gsw = indent(text_id, " ", lambda line: False)

        await incident.reply(gsw, parse_mode="html", silent=True)

    else:
        await incident.reply(
            f"**Chat ID:** `{str(incident.chat_id)}`", silent=True
        )

    return await deleted(incident)
