# Copyright (C) 2022 Unknown <https://github.com/unknownkz/universe>
# All Rights Reserved
#
# Credits : @unknownkz (axel)
# This file is a part of < https://github.com/unknownkz/universe/ >
# PLease read the GNU Affero General Public License in;
# < https://www.github.com/unknownkz/universe/main/LICENSE/ >

from telethon.tl.functions.channels import EditBannedRequest
from telethon.errors.rpcerrorlist import UserIdInvalidError
from telethon.tl.types import ChatBannedRights
from telethon.errors import BadRequestError
from textwrap import indent

from .. import univ
from ..EquipmentTools import __g__, deleted

category = "admins"


@univ.universe_cloud(
    pattern=r"banned(?:\s|$)([\s\S]*)",
    command=("banned <reply/id/username>", category),
    groups_only=True,
    require_admin=True,
)
async def _(incident):
    user, reason = await __g__(incident)
    if not user:
        return

    kz = await incident.reply("Forbid...", silent=True)
    try:
        await univ(
            EditBannedRequest(
                incident.chat_id,
                user.id,
                ChatBannedRights(
                    until_date=None,
                    view_messages=True,
                    send_messages=True,
                    send_media=True,
                    send_stickers=True,
                    send_gifs=True,
                    send_games=True,
                    send_inline=True,
                    embed_links=True,
                ),
            )
        )
    except BadRequestError:
        await kz.delete()
        return await incident.edit("I Don't Have Sufficient Permissions!")

    if reason:
        text_reason = (
            "#Banned " + "#User " + "#Forbid \n" + "╲╲ ㊋ Restrict ㊋ ╱╱"
        )
        text_reason += "\n\n<b>First Name :</b> " + str(user.first_name)
        text_reason += "\n<b>User ID :</b> <code>" + str(user.id) + "</code>"
        text_reason += "\n<b>Reason :</b> " + str(reason)
        wrp = indent(text_reason, " ", lambda line: False)
        await kz.reply(wrp, parse_mode="html", silent=True)
    else:
        text_nreason = (
            "#Banned " + "#User " + "#Forbid \n" + "╲╲ ㊋ Restrict ㊋ ╱╱"
        )
        text_nreason += "\n\n<b>First Name :</b> " + str(user.first_name)
        text_nreason += "\n<b>User ID :</b> <code>" + str(user.id) + "</code>"
        text_nreason += "\n<b>Reason :</b> <code>N/A</code>"
        wrps = indent(text_nreason, " ", lambda line: False)
        await kz.reply(wrps, parse_mode="html", silent=True)

    await kz.delete()
    return await deleted(incident)


@univ.universe_cloud(
    pattern=r"unbanned(?:\s|$)([\s\S]*)",
    command=("unbanned <reply/id/username>", category),
    groups_only=True,
    require_admin=True,
)
async def _(incident):
    user, reason = await __g__(incident)
    if not user:
        return

    kz = await incident.reply("Cancelled...", silent=True)
    try:
        await univ(
            EditBannedRequest(
                incident.chat_id,
                user.id,
                ChatBannedRights(
                    until_date=None,
                    view_messages=None,
                    send_messages=None,
                    send_media=None,
                    send_stickers=None,
                    send_gifs=None,
                    send_games=None,
                    send_inline=None,
                    embed_links=None,
                ),
            )
        )

        if reason:
            text_reason = (
                "#UnBanned "
                + "#User "
                + "#Cancelled \n"
                + "╲╲ ㊋ Revocation ㊋ ╱╱"
            )
            text_reason += "\n\n<b>First Name :</b> " + str(user.first_name)
            text_reason += (
                "\n<b>User ID :</b> <code>" + str(user.id) + "</code>"
            )
            text_reason += "\n<b>Reason :</b> " + str(reason)
            wrp = indent(text_reason, " ", lambda line: False)
            await kz.reply(wrp, parse_mode="html", silent=True)
        else:
            text_nreason = (
                "#UnBanned "
                + "#User "
                + "#Cancelled \n"
                + "╲╲ ㊋ Revocation ㊋ ╱╱"
            )
            text_nreason += "\n\n<b>First Name :</b> " + str(user.first_name)
            text_nreason += (
                "\n<b>User ID :</b> <code>" + str(user.id) + "</code>"
            )
            text_nreason += "\n<b>Reason :</b> <code>N/A</code>"
            wrps = indent(text_nreason, " ", lambda line: False)
            await kz.reply(wrps, parse_mode="html", silent=True)

    except UserIdInvalidError:
        await incident.edit("`Uh oh my unban logic broke!`")
    except Exception as e:
        await incident.edit(f"**Error :**\n`{e}`")

    await kz.delete()
    return await deleted(incident)
