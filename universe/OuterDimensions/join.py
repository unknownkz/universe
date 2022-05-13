# Copyright (C) 2022 Unknown <https://github.com/unknownkz/universe>
# All Rights Reserved
#
# Credits : @unknownkz (axel)
# This file is a part of < https://github.com/unknownkz/universe/ >
# PLease read the GNU Affero General Public License in;
# < https://www.github.com/unknownkz/universe/main/LICENSE/ >

# from re import split
from contextlib import suppress
from telethon.tl.functions.channels import JoinChannelRequest as joining

from .. import univ
from ..EquipmentTools import deleted

category = "service"


@univ.universe_cloud(
    pattern="(joinme|joingroup)",
    command=("joinme|joingroup <reply link|username>", category),
)
async def _(incident):
    kz = incident.reply_to_msg_id
    if kz:
        with suppress(BaseException):
            hash_group = await incident.get_reply_message()
            get_hash = hash_group.message
            if not get_hash.startswith("@") and not get_hash.startswith(
                "https://t.me/"
            ):
                await incident.reply("Please re-check username group/channel")

            else:
                await univ(joining(get_hash))

    else:
        return False

    await deleted(incident)
