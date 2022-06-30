# Copyright (C) 2022 Unknown <https://github.com/unknownkz/universe>
# All Rights Reserved
#
# Credits : @unknownkz (axel)
# This file is a part of < https://github.com/unknownkz/universe/ >
# PLease read the GNU Affero General Public License in;
# < https://www.github.com/unknownkz/universe/main/LICENSE/ >


from telethon.tl import types
from geopy.geocoders import Nominatim as GPS

from .. import univ
from ..EquipmentTools import deleted

category = "tools"


@univ.universe_cloud(
    pattern=r"gps ([\s\S]*)",
    command=("gps <Location/Cordinate>", category),
)
async def _(incident):
    if incident.fwd_from:
        return
    reply_to_id = incident.message
    if incident.reply_to_msg_id:
        reply_to_id = await incident.get_reply_message()
    str = incident.pattern_match.group(1)

    if not str:
        await incident.reply("U're Stupid")

    await incident.edit("Search location...")

    x = GPS(user_agent="Universe")
    gps_loc = x.geocode(str)

    if gps_loc:
        longitude1 = gps_loc.longitude
        latitude1 = gps_loc.latitude
        await reply_to_id.reply(
            str,
            file=types.InputMediaGeoPoint(
                types.InputGeoPoint(latitude1, longitude1)
            ),
        )
        await incident.delete()
    else:
        await incident.reply("Location Not Found.")

    return await deleted(incident)
