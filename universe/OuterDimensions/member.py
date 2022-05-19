# Copyright (C) 2022 Unknown <https://github.com/unknownkz/universe>
# All Rights Reserved
#
# Credits : @unknownkz (axel)
# This file is a part of < https://github.com/unknownkz/universe/ >
# PLease read the GNU Affero General Public License in;
# < https://www.github.com/unknownkz/universe/main/LICENSE/ >

from textwrap import indent
from telethon.tl.types import ChatAdminRights
from telethon.tl.functions.channels import EditAdminRequest
from telethon.errors import BadRequestError

from .. import univ
from ..Configuration import MultiVerse
from ..EquipmentTools import __g__, deleted

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
    pattern="promoted(?: |$)(-admin|-staff)?(?: |$)(.*)",
    command=("promoted -admin|-staff <reply>", category),
    groups_only=True,
    require_admin=True,
)
async def _(incident):
    promo = incident.pattern_match.group(1)

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


@univ.universe_cloud(
    pattern=r"demoted(?:\s|$)([\s\S]*)",
    command=("demoted <reply/username> <reason>", category),
    groups_only=True,
    require_admin=True,
)
async def _(incident):
    user, reason = await __g__(incident)
    if not user:
        return

    kz = await incident.reply("Demoting...")

    rank = "admin"
    try:
        await univ(
            EditAdminRequest(
                incident.chat_id,
                user.id,
                ChatAdminRights(
                    add_admins=None,
                    invite_users=None,
                    change_info=None,
                    ban_users=None,
                    delete_messages=None,
                    pin_messages=None,
                ),
                rank=str(rank),
            )
        )
    except BadRequestError:
        await kz.delete()
        return await incident.edit("I Don't Have Sufficient Permissions!")

    if reason:
        text_reason = (
            "#Demoted " + "#Admin " + "#Delegate \n" + "╲╲ ㊋ Released ㊋ ╱╱"
        )
        text_reason += "\n\n<b>First Name :</b> " + str(user.first_name)
        text_reason += "\n<b>User ID :</b> <code>" + str(user.id) + "</code>"
        text_reason += "\n<b>Reason :</b> " + str(reason)
        wrp = indent(text_reason, " ", lambda line: False)
        await kz.reply(wrp, parse_mode="html", silent=True)
    else:
        text_nreason = (
            "#Demoted " + "#Admin " + "#Delegate \n" + "╲╲ ㊋ Released ㊋ ╱╱"
        )
        text_nreason += "\n\n<b>First Name :</b> " + str(user.first_name)
        text_nreason += "\n<b>User ID :</b> <code>" + str(user.id) + "</code>"
        text_nreason += "\n<b>Reason :</b> <code>N/A</code>"
        wrps = indent(text_nreason, " ", lambda line: False)
        await kz.reply(wrps, parse_mode="html", silent=True)

    await kz.delete()
    return await deleted(incident)
