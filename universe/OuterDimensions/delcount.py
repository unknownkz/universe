# Copyright (C) 2022 Unknown <https://github.com/unknownkz/universe>
# All Rights Reserved
#
# Credits : @unknownkz (axel)
# This file is a part of < https://github.com/unknownkz/universe/ >
# PLease read the GNU Affero General Public License in;
# < https://www.github.com/unknownkz/universe/main/LICENSE/ >

from time import sleep
from telethon.errors import UserAdminInvalidError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights

from .. import univ
from ..EquipmentTools import deleted
from ..UniverseLogger import UniverseLogger as UL

category = "admins"


async def remove_users(byt1, byt2):
    try:
        await univ.kick_participant(byt1, byt2)
        return True, None
    except Exception as excp:
        return False, str(excp)


@univ.universe_cloud(
    pattern="delcount(?: |$)(-clean)?(?: |$)(.*)",
    command=("delcount -clean", category),
    groups_only=True,
)
async def _(incident):
    cleaning = incident.pattern_match.group(1)
    amount_user = 0
    read = 0
    kicked = 0
    failed = 0
    chats = await incident.get_chat()
    if not chats.admin_rights and not chats.creator:
        await incident.reply("You aren't an admin.")
        return False

    if cleaning == "-clean":
        searching = await incident.reply("Clean-up...")

        async for gets in incident.client.iter_participants(incident.chat_id):
            read += 1

            if gets.deleted:
                amount_user += 1
                sleep(1)
                if amount_user >= 0:
                    byt1 = incident.chat_id
                    byt2 = gets.id
                    try:
                        await remove_users(byt1, byt2)
                        sleep(5)
                        kicked += 1
                        failed += 1
                    except UserAdminInvalidError:
                        failed += 1
                        kicked -= 1
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
                    kicked += 1

            elif not gets.deleted:
                cleaning_text = "Your group is already clean."
                sleep(1)
                await searching.edit(cleaning_text)

    else:
        return False

    sans = f"""
**Information :**

`The number of deleted accounts users exists {amount_user},
Kick {kicked} to {read} members.
Failed {failed} account, coz user is admin.
I didn't get permission.`
"""
    sleep(5)
    await searching.reply(sans)
    await searching.delete()
    return await deleted(incident)
