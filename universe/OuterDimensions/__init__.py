# Copyright (C) 2022 Unknown <https://github.com/unknownkz/universe>
# All Rights Reserved
#
# Credits : @unknownkz (axel)
# This file is a part of < https://github.com/unknownkz/universe/ >
# PLease read the GNU Affero General Public License in;
# < https://www.github.com/unknownkz/universe/main/LICENSE/ >

from ..UniverseLogger import UniverseLogger as UL
from ..Configuration import MultiVerse
from ..ClassFundamental import (
    Information_Group,
    Information_Command,
    Information_OuterDimensions,
)
from ..EquipmentTools import deleted

_emoticon_ = {"admins": "👤", "tools": "🛠️", "service": "🔰", "core": "💽", "fun": "🎮"}
_command_prompt_as_trigger = MultiVerse.Trigger


def retriever_data(li):
    for _, _i in Information_Group.items():
        for dimensions in _i:
            if li == dimensions:
                return _
    return None


async def information_group() -> None:
    эжд = "**Module in Universe :**\n\n"
    various_group = ["admins", "service", "tools", "core", "fun"]
    for _ in various_group:
        OuterDimensions = Information_Group[_]
        эжд += f"**{_emoticon_[_]} {_.title()} **({len(OuterDimensions)}) :\n"
        for galaxy in OuterDimensions:
            эжд += f" `{galaxy}` "
        эжд += "\n\n"
    эжд += f"**Example:** `{_command_prompt_as_trigger}module -see <name>`"
    return эжд


def retrieve_data(li):
    for _, _i in Information_OuterDimensions.items():
        for _l in _i:
            if li == _l:
                return _
    return None


async def information_command(integritas, incident, dimensions=False):
    if integritas[0] == _command_prompt_as_trigger:
        integritas = integritas[1:]
    try:
        integritas = integritas[1:]
    except BaseException:
        pass


async def information_module(integritas, incident, point):
    try:
        эжд = Information_OuterDimensions[integritas]
    except KeyError:
        юдщблш = await information_command(
            integritas, incident, dimensions=True
        )
        return юдщблш
    except BaseException:
        await deleted(incident)
        return False
    if len(эжд) == 1 and (point is None or (point != "-see")):
        юдщблш = await information_command(эжд[0], incident, dimensions=True)
        return юдщблш
    юдщблш = f"**Section : **`{integritas}`\n"
    юдщблш += f"**Amount :** `{len(эжд)}`\n"
    category = retriever_data(integritas)
    if category is not None:
        юдщблш += f"**Category :** `{category}`\n\n"
    for йцш in sorted(эжд):
        юдщблш += f"• **Run ›_**   `{_command_prompt_as_trigger}{йцш}`\n"
    юдщблш += f"\n`Depends on your understanding.`"
    return юдщблш


async def outer_lists() -> None:
    """Bug ? 😏"""
    юдщблш = "**Total of Commands ›_**\n\n"
    รนยบล = ["admins", "service", "tools", "core", "fun"]
    for йялд in รนยบล:
        ฟหกดเ = Information_Group[йялд]
        юдщблш += f"**{_emoticon_[йялд]} {йялд.title()} ** - {len(ฟหกดเ)}\n\n"
        for ㅂㅈㄷㄱ in ฟหกดเ:
            ㅎㅗㅓㅏ = Information_OuterDimensions[ㅂㅈㄷㄱ]
            юдщблш += f"• **{ㅂㅈㄷㄱ.title()} has {len(ㅎㅗㅓㅏ)} commands**\n"
            for ー in sorted(ㅎㅗㅓㅏ):
                юдщблш += f" - `{_command_prompt_as_trigger}{ー}`\n"
            юдщблш += "\n"
    return юдщблш
