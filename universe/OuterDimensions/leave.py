# Copyright (C) 2022 Unknown <https://github.com/unknownkz/universe>
# All Rights Reserved
#
# Credits : @unknownkz (axel)
# This file is a part of < https://github.com/unknownkz/universe/ >
# PLease read the GNU Affero General Public License in;
# < https://www.github.com/unknownkz/universe/main/LICENSE/ >

from time import sleep
from contextlib import suppress
from telethon.tl.functions.channels import LeaveChannelRequest as leave

from .. import univ

category = "service"


@univ.universe_cloud(
    pattern="leave",
    command=("leave", category),
    groups_only=True,
)
async def _(incident):
    with suppress(BaseException):
        await incident.delete()
        sleep(0.9)
        await univ(leave(incident.chat_id))
