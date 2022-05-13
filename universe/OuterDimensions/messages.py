# Copyright (C) 2022 Unknown <https://github.com/unknownkz/universe>
# All Rights Reserved
#
# Credits : @unknownkz (axel)
# This file is a part of < https://github.com/unknownkz/universe/ >
# PLease read the GNU Affero General Public License in;
# < https://www.github.com/unknownkz/universe/main/LICENSE/ >

from contextlib import suppress

from .. import univ
from ..EquipmentTools import deleted

category = "service"


@univ.universe_cloud(
    pattern="(del|Del|delete)",
    command=("del|Del|delete <reply messages>", category),
)
async def _(incident):
    typo_no_reply = incident.pattern_match.group(0)
    replied = await incident.get_reply_message()
    kz = incident.reply_to_msg_id
    if typo_no_reply:
        with suppress(BaseException):
            await incident.delete()
    else:
        return False

    if kz:
        await deleted(incident)
        await replied.delete()

    else:
        return False
