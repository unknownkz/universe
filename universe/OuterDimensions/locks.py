# Copyright (C) 2022 Unknown <https://github.com/unknownkz/universe>
# All Rights Reserved
#
# Credits : @unknownkz (axel)
# This file is a part of < https://github.com/unknownkz/universe/ >
# PLease read the GNU Affero General Public License in;
# < https://www.github.com/unknownkz/universe/main/LICENSE/ >

from telethon.tl.types import ChatBannedRights
from telethon.tl.functions.messages import EditChatDefaultBannedRightsRequest

from .. import univ
from ..EquipmentTools import eor, etd, deleted
from ..Configuration import MultiVerse

category = "admins"

p = MultiVerse.Trigger


async def locks_messages(
    chat_id,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_link_previews=True,
    send_polls=True,
    change_info=True,
    invite_users=True,
    pin_messages=True,
):
    try:
        await univ.edit_permissions(
            chat_id,
            send_messages=True,
            send_media=True,
            send_stickers=True,
            send_gifs=True,
            send_games=True,
            send_inline=True,
            embed_link_previews=True,
            send_polls=True,
            change_info=True,
            invite_users=True,
            pin_messages=True,
        )
        return True, None
    except Exception as excp:
        return False, str(excp)


async def unlocks_messages(
    chat_id,
    send_messages=False,
    send_media=False,
    send_stickers=False,
    send_gifs=False,
    send_games=False,
    send_inline=False,
    embed_link_previews=False,
    send_polls=False,
    change_info=False,
    invite_users=False,
    pin_messages=False,
):
    try:
        await univ.edit_permissions(
            chat_id,
            send_messages=False,
            send_media=False,
            send_stickers=False,
            send_gifs=False,
            send_games=False,
            send_inline=False,
            embed_link_previews=False,
            send_polls=False,
            change_info=False,
            invite_users=False,
            pin_messages=False,
        )
        return True, None
    except Exception as excp:
        return False, str(excp)


@univ.universe_cloud(
    pattern=r"lock ([\s\S]*)",
    command=("lock -all", category),
    groups_only=True,
)
async def _(incident):
    locked = incident.pattern_match.group(1)
    chat_target = incident.chat_id
    if not incident.is_group:
        return False

    chats = await incident.get_chat()
    if not chats.admin_rights and not chats.creator:
        await incident.edit("You aren't an admin.")
        await deleted(incident)
        return False

    if locked == "-all":
        send_messages = True
        send_media = True
        send_stickers = True
        send_gifs = True
        send_games = True
        send_inline = True
        embed_link_previews = True
        send_polls = True
        change_info = True
        invite_users = True
        pin_messages = True
        await locks_messages(
            incident.chat_id,
            send_messages=send_messages,
            send_media=send_media,
            send_stickers=send_stickers,
            send_gifs=send_gifs,
            send_games=send_games,
            send_inline=send_inline,
            embed_link_previews=embed_link_previews,
            send_polls=send_polls,
            change_info=change_info,
            invite_users=invite_users,
            pin_messages=pin_messages,
        )
        type = "lock all"
        here_comes_the_sun = ChatBannedRights(
            until_date=None,
            send_messages=send_messages,
            send_media=send_media,
            send_stickers=send_stickers,
            send_gifs=send_gifs,
            send_games=send_games,
            send_inline=send_inline,
            embed_links=embed_link_previews,
            send_polls=send_polls,
            change_info=change_info,
            invite_users=invite_users,
            pin_messages=pin_messages,
        )
        await incident.client(
            EditChatDefaultBannedRightsRequest(
                peer=chat_target, banned_rights=here_comes_the_sun
            )
        )

    else:
        return await incident.edit(
            f"Run Command ›_\n\n**Example:**\n`{p}lock -all` : to lock all."
        )
    try:
        await eor(incident, f"{type} for this chat.")
    except BaseException as excp:
        await etd(incident, f"**Message:** `{excp}`")


@univ.universe_cloud(
    pattern=r"unlock ([\s\S]*)",
    command=("unlock -all", category),
    groups_only=True,
)
async def _(incident):
    locked = incident.pattern_match.group(1)
    chat_target = incident.chat_id
    if not incident.is_group:
        return False

    chats = await incident.get_chat()
    if not chats.admin_rights and not chats.creator:
        await incident.edit("You aren't an admin.")
        await deleted(incident)
        return False

    if locked == "-all":
        send_messages = False
        send_media = False
        send_stickers = False
        send_gifs = False
        send_games = False
        send_inline = False
        embed_link_previews = False
        send_polls = False
        change_info = False
        invite_users = False
        pin_messages = False
        await unlocks_messages(
            incident.chat_id,
            send_messages=send_messages,
            send_media=send_media,
            send_stickers=send_stickers,
            send_gifs=send_gifs,
            send_games=send_games,
            send_inline=send_inline,
            embed_link_previews=embed_link_previews,
            send_polls=send_polls,
            change_info=change_info,
            invite_users=invite_users,
            pin_messages=pin_messages,
        )
        type = "unlock all"
        comes = ChatBannedRights(
            until_date=None,
            send_messages=send_messages,
            send_media=send_media,
            send_stickers=send_stickers,
            send_gifs=send_gifs,
            send_games=send_games,
            send_inline=send_inline,
            embed_links=embed_link_previews,
            send_polls=send_polls,
            change_info=change_info,
            invite_users=invite_users,
            pin_messages=pin_messages,
        )
        await incident.client(
            EditChatDefaultBannedRightsRequest(
                peer=chat_target, banned_rights=comes
            )
        )

    else:
        return await incident.edit(
            f"Run Command ›_\n\n**Example:**\n`{p}unlock -all` : to unlock all."
        )
    try:
        await eor(incident, f"{type} for this chat.")
    except BaseException as excp:
        await etd(incident, f"**Message:** `{excp}`")
