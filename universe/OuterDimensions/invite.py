# Copyright (C) 2022 Unknown <https://github.com/unknownkz/universe>
# All Rights Reserved
#
# Credits : @unknownkz (axel)
# This file is a part of < https://github.com/unknownkz/universe/ >
# PLease read the GNU Affero General Public License in;
# < https://www.github.com/unknownkz/universe/main/LICENSE/ >


from telethon import functions

from .. import univ
from ..EquipmentTools import deleted

category = "service"


@univ.universe_cloud(
    pattern=r"invite ([\s\S]*)",
    command=("invite <username/id>", category),
    groups_only=True,
)
async def _(incident):
    "To invite a user to chat."
    to_add_users = incident.pattern_match.group(1)
    xid = incident.chat_id
    if not incident.is_channel and incident.is_group:
        # https://lonamiwebs.github.io/Telethon/methods/messages/add_chat_user.html
        for user_id in to_add_users.split(" "):
            try:
                await incident.client(
                    functions.messages.AddChatUserRequest(
                        chat_id=xid, user_id=user_id, fwd_limit=1000000
                    )
                )
            except Exception as x:
                await incident.reply(f"`{str(x)}`")
                return await deleted(incident)
    else:
        # https://lonamiwebs.github.io/Telethon/methods/channels/invite_to_channel.html
        for user_id in to_add_users.split(" "):
            try:
                await incident.client(
                    functions.channels.InviteToChannelRequest(
                        channel=xid, users=[user_id]
                    )
                )
            except Exception as x:
                await incident.reply(f"`{x}`")
                return await deleted(incident)
