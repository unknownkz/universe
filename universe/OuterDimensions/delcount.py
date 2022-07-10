# Copyright (C) 2022 Unknown <https://github.com/unknownkz/universe>
# All Rights Reserved
#
# Credits : @unknownkz (axel)
# This file is a part of < https://github.com/unknownkz/universe/ >
# PLease read the GNU Affero General Public License in;
# < https://www.github.com/unknownkz/universe/main/LICENSE/ >

from time import sleep
from telethon.errors import (
    UserAdminInvalidError,
    ChannelInvalidError,
    ChannelPrivateError,
    ChannelPublicGroupNaError,
)
from telethon.tl.functions.channels import (
    EditBannedRequest,
    GetFullChannelRequest,
)
from telethon.tl.types import ChatBannedRights
from telethon.tl.functions.messages import GetFullChatRequest

from .. import univ
from ..EquipmentTools import deleted
from ..Configuration import MultiVerse

category = "admins"

i = MultiVerse.Trigger


async def remove_users(byt1, byt2):
    try:
        await univ.kick_participant(byt1, byt2)
        return True, None
    except Exception as excp:
        return False, str(excp)


async def __getchat(incident):
    chat = incident.pattern_match.group(1)
    chat_info = None
    if chat:
        try:
            chat = int(chat)
        except ValueError:
            pass
    if not chat:
        if incident.reply_to_msg_id:
            replied_msg = await incident.get_reply_message()
            if (
                replied_msg.fwd_from
                and replied_msg.fwd_from.channel_id is not None
            ):
                chat = replied_msg.fwd_from.channel_id
        else:
            chat = incident.chat_id
    try:
        chat_info = await incident.client(GetFullChatRequest(chat))
    except BaseException:
        try:
            chat_info = await incident.client(GetFullChannelRequest(chat))
        except ChannelInvalidError:
            await incident.edit("`Invalid channel/group`")
            return None
        except ChannelPrivateError:
            await incident.reply(
                "`This is a private channel/group or I am banned from there`"
            )
            return None
        except ChannelPublicGroupNaError:
            await incident.reply("`Channel or supergroup doesn't exist`")
            return None
        except (TypeError, ValueError):
            await incident.reply("`Invalid channel/group`")
            return None
    return chat_info


@univ.universe_cloud(
    pattern="delcount(?: |$)(-clean)?(?: |$)(.*)",
    command=("delcount", category),
    groups_only=True,
)
async def _(incident):
    cleaning = incident.pattern_match.group(1)
    cleaning_text = "Your group is already clean."
    amount_user = 0
    kicked = 0
    failed = 0
    chats = await incident.get_chat()

    if not chats.admin_rights and not chats.creator:
        await incident.reply("You aren't an admin.")
        return False

    if cleaning != "-clean":
        shx = await incident.reply("`Searching...`")
        sleep(5)
        chat = await __getchat(incident)
        chat_obj_info = await incident.client.get_entity(chat.full_chat.id)
        read = (
            chat.full_chat.participants_count
            if hasattr(chat.full_chat, "participants_count")
            else chat_obj_info.participants_count
        )
        async for gets in incident.client.iter_participants(incident.chat_id):
            if gets.deleted:
                amount_user += 1
                sleep(1)
        if amount_user > 0:
            cleaning_text = (
                f"**Finding** `{amount_user}` **Deleted Account from** `{read}` **member in this Group."
                f"\nRun ›_** `{i}delcount -clean`"
            )
        return await shx.edit(cleaning_text)

    searching = await incident.reply("Clean-up...")
    async for gets in incident.client.iter_participants(incident.chat_id):
        if gets.deleted:
            amount_user += 1
            if amount_user >= 0:
                byt1 = incident.chat_id
                byt2 = gets.id
                try:
                    await remove_users(byt1, byt2)
                    kicked += 1

                except UserAdminInvalidError as excp:
                    if excp:
                        failed += 1
                    return

                sleep(3)  # Flood Wait
                await univ(
                    EditBannedRequest(
                        incident.chat_id,
                        byt2,
                        ChatBannedRights(
                            until_date=None,
                            send_messages=None,
                            send_media=None,
                            send_stickers=None,
                            send_gifs=None,
                            send_games=None,
                            send_inline=None,
                            embed_links=None,
                        ),
                    ),
                )

    sans = f"""
**Information :**

`The number of deleted accounts users exists {amount_user},
Kick {kicked} Deleted Account.
Failed {failed} Account, coz user is admin.
I didn't get permission.`
"""
    sleep(5)
    await searching.edit(sans)
    return await deleted(incident)
