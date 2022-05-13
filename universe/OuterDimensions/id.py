# Copyright (C) 2022 Unknown <https://github.com/unknownkz/universe>
# All Rights Reserved
#
# Credits : @unknownkz (axel)
# This file is a part of < https://github.com/unknownkz/universe/ >
# PLease read the GNU Affero General Public License in;
# < https://www.github.com/unknownkz/universe/main/LICENSE/ >

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
                name = "**" + replied.sender.first_name + "**"
        else:
            user_id = replied.forward.sender.id
            if replied.forward.sender.username:
                name = "@" + replied.forward.sender.username
            else:
                name = "*" + replied.forward.sender.first_name + "*"
        await incident.reply(
            f"**Name:** {name} \n**User ID:** `{user_id}` \n**Chat ID:** `{str(incident.chat_id)}`"
        )

    else:
        await incident.reply(f"**Chat ID:** `{str(incident.chat_id)}`")

    return await deleted(incident)
