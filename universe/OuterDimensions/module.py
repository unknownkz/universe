# Copyright (C) 2022 Unknown <https://github.com/unknownkz/universe>
# All Rights Reserved
#
# Credits : @unknownkz (axel)
# This file is a part of < https://github.com/unknownkz/universe/ >
# PLease read the GNU Affero General Public License in;
# < https://www.github.com/unknownkz/universe/main/LICENSE/ >

from . import information_group as c
from . import information_module as b
from . import outer_lists as d
from .. import univ
from ..EquipmentTools import eor, deleted
from ..Configuration import MultiVerse

category = "service"

i = MultiVerse.Trigger

text_command = f"""
**Command Guide ›**
-------------------------------
__To get information module or guide,
for the command prompt.__
-------------------------------

**Examples:**
 Run › `{i}module -all`
 Run › `{i}module -list`
 Run › `{i}module -see <name>`

**Options:**
 › `-all` : to get all commands.
 › `-list` : to see list module and commands.
 › `-see` : to see commands in module.

MAINTAINER : [@xelyourslurred](https:t.me/xelyourslurred)
`<unknownkz@outlook.co.id>`

"""


@univ.universe_cloud(
    pattern=r"module(?: |$)(-all|-see|-list)?(?: |$)(.*)",
    command=("module", category),
)
async def _(incident):
    point = incident.pattern_match.group(1)
    integritas = incident.pattern_match.group(2)
    if point == "-see" and integritas:
        эжд = await b(integritas, incident, point)
        if эжд is None:
            return False
    elif point == "-list":
        эжд = await c()
    elif point == "-all":
        эжд = await d()
    else:
        await incident.reply(text_command)
        await deleted(incident)
        return False

    return await eor(incident, str(эжд))
