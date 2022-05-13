# Copyright (C) 2022 Unknown <https://github.com/unknownkz/universe>
# All Rights Reserved
#
# Credits : @unknownkz (axel)
# This file is a part of < https://github.com/unknownkz/universe/ >
# PLease read the GNU Affero General Public License in;
# < https://www.github.com/unknownkz/universe/main/LICENSE/ >

from telethon.errors.rpcerrorlist import UserAdminInvalidError

from .. import univ

category = "admins"


@univ.universe_cloud(
    pattern="kicked(?: |$)(-retards)?(?: |$)(.*)",
    command=("kicked -retards <reply>", category),
    groups_only=True,
)
async def _(incident):
    kicked = incident.pattern_match.group(1)
    chats = await incident.get_chat()
    kz = incident.reply_to_msg_id
    if kicked == "-retards":
        if not chats.admin_rights and not chats.creator:
            await incident.edit("You aren't an admin.")
            return False
    else:
        return False

    if kz:
        replied = await incident.get_reply_message()
        if replied.from_id:
            try:
                userid = await univ.get_entity(replied.sender_id)
                await univ.kick_participant(incident.chat_id, userid.id)
            except UserAdminInvalidError:
                await univ.send_message(
                    incident.chat_id,
                    "Either you're not an admin or you tried to ban an admin that you didn't promote",
                )
    else:
        return False

    return await replied.delete()
