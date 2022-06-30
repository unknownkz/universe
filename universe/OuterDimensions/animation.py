# Copyright (C) 2022 Unknown <https://github.com/unknownkz/universe>
# All Rights Reserved
#
# Credits : @unknownkz (axel)
# This file is a part of < https://github.com/unknownkz/universe/ >
# PLease read the GNU Affero General Public License in;
# < https://www.github.com/unknownkz/universe/main/LICENSE/ >


from .. import univ

category = "fun"


DCK = """
⣠⡶⠚⠛⠲⢄⡀
⣼⠁ ⠀⠀⠀ ⠳⢤⣄
⢿⠀⢧⡀⠀⠀⠀⠀⠀⢈⡇
⠈⠳⣼⡙⠒⠶⠶⠖⠚⠉⠳⣄
⠀⠀⠈⣇⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄
⠀⠀⠀⠘⣆ ⠀⠀⠀⠀ ⠀⠈⠓⢦⣀
⠀⠀⠀⠀⠈⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠲⢤
⠀⠀⠀⠀⠀⠀⠙⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧
⠀⠀⠀⠀⠀⠀⠀⡴⠋⠓⠦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠈⣇
⠀⠀⠀⠀⠀⠀⣸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡄
⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇
⠀⠀⠀⠀⠀⠀⢹⡄⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃
⠀⠀⠀⠀⠀⠀⠀⠙⢦⣀⣳⡀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⢦⣀⣀⣀⣀⣠⡴⠚⠁⠉⠉⠉
"""


@univ.universe_cloud(
    pattern=r"(?:penis|dick)\s?(.)?",
    command=("dick", category),
)
async def _(incident):
    ascii_ = incident.pattern_match.group(1)
    dck = DCK
    if ascii_:
        dck = dck.replace("🤤", ascii_)
    await incident.edit(dck)


@univ.universe_cloud(
    pattern=r"colay",
    command=("colay", category),
)
async def _(incident):
    if not incident.text[0].isalpha() and incident.text[0] not in (
        "/",
        "@",
        "!",
    ):
        await incident.edit("8✊===D")
        await incident.edit("8=✊==D")
        await incident.edit("8==✊=D")
        await incident.edit("8===✊D")
        await incident.edit("8==✊=D")
        await incident.edit("8=✊==D")
        await incident.edit("8✊===D")
        await incident.edit("8=✊==D")
        await incident.edit("8==✊=D")
        await incident.edit("8===✊D")
        await incident.edit("8==✊=D")
        await incident.edit("8=✊==D")
        await incident.edit("8✊===D")
        await incident.edit("8=✊==D")
        await incident.edit("8==✊=D")
        await incident.edit("8===✊D")
        await incident.edit("8==✊=D")
        await incident.edit("8=✊==D")
        await incident.edit("8===✊D💦")
        await incident.edit("8==✊=D💦💦")
        await incident.edit("8=✊==D💦💦💦")
        await incident.edit("8✊===D💦💦💦💦")
        await incident.edit("8===✊D💦💦💦💦💦")
        await incident.edit("8==✊=D💦💦💦💦💦💦")
        await incident.edit("8=✊==D💦💦💦💦💦💦💦")
        await incident.edit("8✊===D💦💦💦💦💦💦💦💦")
        await incident.edit("8===✊D💦💦💦💦💦💦💦💦💦")
        await incident.edit("8==✊=D💦💦💦💦💦💦💦💦💦💦")
        await incident.edit("8=✊==D AHHHHH UDAH CROTTT!!")
        await incident.edit("😰🤤😰🤤🤤🤤")
