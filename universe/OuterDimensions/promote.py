# Copyright (C) 2022 Unknown <https://github.com/unknownkz/universe>
# All Rights Reserved
#
# Credits : @unknownkz (axel)
# This file is a part of < https://github.com/unknownkz/universe/ >
# PLease read the GNU Affero General Public License in;
# < https://www.github.com/unknownkz/universe/main/LICENSE/ >

from telethon.tl.types import ChatAdminRights
from telethon.tl.functions.channels import EditAdminRequest
from telethon.errors import BadRequestError

from .. import univ
from ..Configuration import MultiVerse
from ..EquipmentTools import deleted

category = "admins"

u = MultiVerse.Trigger

promote_commands = f"""
**Command Guide ›**

__Promote user as admin__

`{u}promote -admin` <reply user>
`{u}promote -staff` <reply user>


**Advantages and Deficiency**
› `-admin` :
Can Promote user as Admin, can change info group.
Auto title (Administrator)

› `-staff` :
Can't Promote user as Admin, can't change info group.
Auto title (Staff Admin)
"""


@univ.universe_cloud(
    pattern="promote(?: |$)(-admin|-staff)?(?: |$)(.*)",
    command=("promote -admin|-staff <reply>", category),
    groups_only=True,
)
async def _(incident):
    promo = incident.pattern_match.group(1)
    chats = await incident.get_chat()
    if not chats.admin_rights and not chats.creator:
        await incident.edit("You aren't an admin.")
        return False

    if promo == "-admin":
        kz = incident.reply_to_msg_id
        pr = await incident.reply("`Promoting...`")
        if kz:
            replied = await incident.get_reply_message()
            if replied.from_id:
                userid = await univ.get_entity(replied.sender_id)
                try:
                    ranked = "Administrator"
                    await univ(
                        EditAdminRequest(
                            incident.chat_id,
                            userid.id,
                            ChatAdminRights(
                                add_admins=True,
                                invite_users=True,
                                change_info=True,
                                ban_users=True,
                                manage_call=True,
                                delete_messages=True,
                                pin_messages=True,
                            ),
                            rank=str(ranked),
                        )
                    )
                    await pr.edit("`Promoted Successfully.`")
                except BadRequestError as excp:
                    await pr.edit(str(excp))
        else:
            return await pr.edit("Reply to user")

    elif promo == "-staff":
        kz = incident.reply_to_msg_id
        pr = await incident.reply("`Promoting...`")
        if kz:
            replied = await incident.get_reply_message()
            if replied.from_id:
                userid = await univ.get_entity(replied.sender_id)
                try:
                    ranked = "Staff Admin"
                    await univ(
                        EditAdminRequest(
                            incident.chat_id,
                            userid.id,
                            ChatAdminRights(
                                add_admins=False,
                                invite_users=True,
                                change_info=False,
                                ban_users=True,
                                manage_call=True,
                                delete_messages=True,
                                pin_messages=True,
                            ),
                            rank=str(ranked),
                        )
                    )
                    await pr.edit("`Promoted Successfully.`")
                except BadRequestError as excp:
                    await pr.edit(str(excp))
        else:
            return await pr.edit("Reply to user")

    else:
        await incident.reply(promote_commands)

    return await deleted(incident)
