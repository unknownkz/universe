# Copyright (C) 2022 Unknown <https://github.com/unknownkz/universe>
# All Rights Reserved
#
# Credits : @unknownkz (axel)
# This file is a part of < https://github.com/unknownkz/universe/ >
# PLease read the GNU Affero General Public License in;
# < https://www.github.com/unknownkz/universe/main/LICENSE/ >

from time import sleep
from datetime import datetime

from .. import univ
from ..EquipmentTools import deleted

category = "tools"


@univ.universe_cloud(
    pattern=r"ping",
    command=("ping", category),
)
async def ping(incident):
    start = datetime.now()
    unbelieve = await incident.reply("...🏇")
    sleep(0.3)
    await unbelieve.edit("..🏇.")
    sleep(0.3)
    await unbelieve.edit(".🏇..")
    sleep(0.3)
    await unbelieve.edit("🏇...")
    end = datetime.now()
    time_millisecond = (end - start).microseconds / 1000
    millisecond = round((time_millisecond - 0.9) / 3, 4)
    info_latency = f"📡 Latency : `{millisecond}` ms"
    await unbelieve.edit(info_latency)
    await deleted(incident)
