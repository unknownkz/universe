# Copyright (C) 2022 Unknown <https://github.com/unknownkz/universe>
# All Rights Reserved
#
# Credits : @unknownkz (axel)
# This file is a part of < https://github.com/unknownkz/universe/ >
# PLease read the GNU Affero General Public License in;
# < https://www.github.com/unknownkz/universe/main/LICENSE/ >

from .. import univ
from ..EquipmentTools import etd, deleted, __parse, __yaml

category = "tools"


@univ.universe_cloud(
    pattern="(json|raw|js)",
    command=("json|raw|js <reply>", category),
)
async def _(incident):
    replied = (
        await incident.get_reply_message()
        if incident.reply_to_msg_id
        else incident
    )
    reps = incident.reply_to_msg_id
    if not reps:
        return False

    __json = replied.stringify()
    await etd(incident, __json, parse_mode=__parse)
    await deleted(incident)


@univ.universe_cloud(
    pattern="(yaml|yml)",
    command=("yaml|yml <reply>", category),
)
async def _(incident):
    replied = (
        await incident.get_reply_message()
        if incident.reply_to_msg_id
        else incident
    )
    reps = incident.reply_to_msg_id
    __yml = __yaml(replied)
    if not reps:
        return False

    await etd(incident, __yml, parse_mode=__parse)
    await deleted(incident)
