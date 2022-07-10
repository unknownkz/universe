# Copyright (C) 2022 Unknown <https://github.com/unknownkz/universe>
# All Rights Reserved
#
# Credits : @unknownkz (axel)
# This file is a part of < https://github.com/unknownkz/universe/ >
# PLease read the GNU Affero General Public License in;
# < https://www.github.com/unknownkz/universe/main/LICENSE/ >

from io import BytesIO
from PIL import Image

from .. import univ, Rooters
from ..EquipmentTools import deleted

category = "tools"


@univ.universe_cloud(
    pattern=r"constick",
    command=("constick <reply stickers>", category),
)
async def _(incident):
    xid = incident.chat_id
    rep_msg = await incident.get_reply_message()
    if not incident.is_reply or not rep_msg.sticker:
        await incident.reply("Please replying to stickers")

    zx = await incident.reply("Converted...")

    foto = BytesIO()
    foto = await univ.download_media(rep_msg.sticker, foto)
    im = Image.open(foto).convert("RGB")
    im.save("sticker.png", "png")
    nm = "stickers.png"

    await univ.send_file(
        xid,
        "sticker.png",
        reply_to=rep_msg,
    )
    (Rooters / nm).unlink(missing_ok=True)

    await zx.delete()
    return await deleted(incident)
