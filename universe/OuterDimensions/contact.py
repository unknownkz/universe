# All Rights Reserved
#
# Credits : @unknownkz (axel)
# This file is a part of < https://github.com/unknownkz/universe/ >
# PLease read the GNU Affero General Public License in;
# < https://www.github.com/unknownkz/universe/main/LICENSE/ >


from .. import univ
from ..EquipmentTools import deleted

category = "tools"


@univ.universe_cloud(
    pattern=r"contact",
    command=("contact", category),
)
async def _(incident):
    xx = incident.chat_id
    mutualan_text = "<b>📬 My Contacts</b> \n"
    mutualan_text += (
        "<code>Intagram:</code>"
        + '[<i> <a href="instagram.com/si_axeell"> Click Here </a></i>]\n'
    )
    mutualan_text += (
        "<code>Twitter:</code>"
        + '[<i> <a href="twitter.com/unknownkzx"> Click Here </a></i>]\n'
    )
    mutualan_text += (
        "<code>Github:</code>"
        + '[<i> <a href="github.com/Unknownkz"> Click Here </a></i>]'
    )
    await univ.send_message(xx, mutualan_text, silent=True, parse_mode="html")
    return await deleted(incident)
