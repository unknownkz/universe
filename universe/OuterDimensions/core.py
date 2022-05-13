# Copyright (C) 2022 Unknown <https://github.com/unknownkz/universe>
# All Rights Reserved
#
# Credits : @unknownkz (axel)
# This file is a part of < https://github.com/unknownkz/universe/ >
# PLease read the GNU Affero General Public License in;
# < https://www.github.com/unknownkz/universe/main/LICENSE/ >

from psutil import swap_memory, virtual_memory
from platform import uname
from sys import version
from telethon import __version__
from carbon import Carbon, CarbonOptions

from ..Ground import Rotation
from .. import univ, Rooters
from ..EquipmentTools import etd, gts, deleted, RunningCommand
from ..Configuration import MultiVerse

category = "core"

i = MultiVerse.Trigger


@univ.universe_cloud(
    pattern="repository",
    command=("repository", category),
)
async def _(incident):
    await etd(
        incident,
        "Click [Here](https://github.com/unknownkz/universe) to open source code.",
    )
    await deleted(incident)


@univ.universe_cloud(
    pattern="core(?: |$)(-i)?(?: |$)(.*)",
    command=("core -i", category),
)
async def _(incident):
    point = incident.pattern_match.group(1)
    unam = uname()
    if point != "-i":
        return False

    else:
        core_text = f"""
**[ System Info ]**
--------------------------------
› System: {unam.system}
› Machine: {unam.machine}
› Kernel: {unam.system} {unam.release}
› Version Release: {unam.version}
--------------------------------
**Engine & Library :**
› Python : {version}
› Telethon : {__version__}
--------------------------------
"""
        await etd(incident, core_text)
        await deleted(incident)


@univ.universe_cloud(
    pattern="memory(?: |$)(-i)?(?: |$)(.*)",
    command=("memory -i", category),
)
async def _(incident):
    point = incident.pattern_match.group(1)

    v_used = virtual_memory().used
    v_total = virtual_memory().total
    v_available = virtual_memory().available
    v_free = virtual_memory().free
    v_cached = virtual_memory().cached
    v_percent = virtual_memory().percent

    s_used = swap_memory().used
    s_total = swap_memory().total
    s_free = swap_memory().free
    s_percent = swap_memory().percent

    if point != "-i":
        return False

    else:
        memory_text = f"""
**[ Memory Info ]**
-------------------------------
**Virtual Memory :**
› Used: {gts(v_used)}
› Total: {gts(v_total)}
› Available: {gts(v_available)}
› Free: {gts(v_free)}
› Cached: {gts(v_cached)}
› Percentage: {v_percent}%
--------------------------------
**Swap Memory :**
› Used: {gts(s_used)}
› Total: {gts(s_total)}
› Free: {gts(s_free)}
› Percentage: {s_percent}%
"""
        await etd(incident, memory_text)
        await deleted(incident)


@univ.universe_cloud(
    pattern="neofetch",
    command=("neofetch", category),
)
async def _(incident):
    nart = incident.chat_id
    xx = await incident.reply("`Getting...`")
    x, y = await RunningCommand(
        "neofetch|sed 's/\x1B\\[[0-9;\\?]*[a-zA-Z]//g' >> neofetch.txt"
    )
    fx = "neofetch.txt"
    with open(fx, "r") as nf:
        code = (nf.read()).replace("\n\n", "")
        language = "auto"
        options = CarbonOptions(code=code, language=language)
        cb = Carbon()
        users_names = await univ.get_entity("me")
        my_names = users_names.first_name
        image = Rotation.run_until_complete(cb.generate(options))
        Rotation.run_until_complete(image.save(f"{str(my_names)}"))
        fz = f"{str(my_names)}.png"
        await univ.send_file(
            nart,
            file=fz,
            force_document=True,
            silent=True,
        )

    (Rooters / "neofetch.txt").unlink(missing_ok=True)
    (Rooters / fz).unlink(missing_ok=True)
    await xx.delete()
    return await deleted(incident)
