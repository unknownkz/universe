# Copyright (C) 2022 Unknown <https://github.com/unknownkz/universe>
# All Rights Reserved
#
# Credits : @unknownkz (axel)
# This file is a part of < https://github.com/unknownkz/universe/ >
# PLease read the GNU Affero General Public License in;
# < https://www.github.com/unknownkz/universe/main/LICENSE/ >

from telethon.tl.functions.channels import GetFullChannelRequest as a
from telethon.tl.functions.phone import GetGroupCallRequest as b
from telethon.tl.functions.phone import (
    CreateGroupCallRequest,
    DiscardGroupCallRequest,
)

from .. import univ
from ..EquipmentTools import deleted
from ..Configuration import MultiVerse

i = MultiVerse.Trigger

category = "admins"

vcg_example = f"""
**Command Guide ›**

__Voice Call Group__

`{i}vcg -start` : to start voice call group.
`{i}vcg -end` : to end voice call group.
"""


async def voice_call_group(incident):
    c = await univ(a(incident.chat_id))
    d = await univ(b(c.full_chat.call, limit=1))
    return d.call


@univ.universe_cloud(
    pattern=r"vcg(?: |$)(-start|-end)?(?: |$)(.*)",
    command=("vcg -start|-end", category),
    groups_only=True,
)
async def _(incident):
    point = incident.pattern_match.group(1)
    chats = await incident.get_chat()
    if not chats.admin_rights and not chats.creator:
        await incident.edit("You aren't an admin.")
        return False

    if point == "-start":
        try:
            await univ(CreateGroupCallRequest(incident.chat_id))
        except BaseException as excp:
            await incident.edit(str(excp))

    elif point == "-end":
        try:
            await univ(
                DiscardGroupCallRequest(await voice_call_group(incident))
            )
        except BaseException as excp:
            await incident.edit(str(excp))

    else:
        await incident.reply(vcg_example)

    return await deleted(incident)
