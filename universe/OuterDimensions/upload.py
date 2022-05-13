# Copyright (C) 2022 Unknown <https://github.com/unknownkz/universe>
# All Rights Reserved
#
# Credits : @unknownkz (axel)
# This file is a part of < https://github.com/unknownkz/universe/ >
# PLease read the GNU Affero General Public License in;
# < https://www.github.com/unknownkz/universe/main/LICENSE/ >

from os import remove, rename
from contextlib import suppress
from datetime import datetime
from telegraph import upload_file as tgph
from telegraph import Telegraph
from telegraph.exceptions import TelegraphException
from PIL import Image

from .. import univ
from ..EquipmentTools import deleted, etd, attributes_media
from ..Configuration import MultiVerse
from ..UniverseLogger import UniverseLogger as UL
from ..UniverseLogger import tz

category = "tools"

i = MultiVerse.Trigger

information_command = f"""
**Command Guide ›**

__Upload to telegra.ph__

**Example:**
› `{i}tgraph -post <reply media|text>`

Title:
Default › `universe`

Media Support:
File › .webp | .jpg | .mp4 | .png

Unsupported:
File › .tgs | stickers
"""


def save_images(the_attributes):
    try:
        ur_image = Image.open(the_attributes)
        ur_image.save(the_attributes, formats=None)
    except OSError as excp:
        UL.error(str(excp))


@univ.universe_cloud(
    pattern=r"tgraph(?: |$)(-post)?(?: |$)(.*)",
    command=("tgraph -post <reply>", category),
)
async def _(incident):
    point = incident.pattern_match.group(1)
    rply = await incident.get_reply_message()
    if not rply:
        await incident.reply(information_command)
        return await deleted(incident)

    if not rply.media and rply.message:
        content = rply.message

    elif point != "-post":
        return False

    else:
        start = datetime.now()
        kenz = await incident.reply("Posting...")
        the_times = datetime.now(tz).isoformat("_", "seconds")
        type_of_file = attributes_media(rply.media)
        files_down = await univ.download_media(rply, "cache")

        if type_of_file == "sticker animated" and files_down.endswith(".tgs"):
            return await etd(incident, "Animated stickers not supported.")

        if type_of_file == "sticker" and files_down.endswith(".webp"):
            save_images(files_down)
            the_times = "sticker_" + the_times + ".png"
            rename(files_down, the_times)
            files_down = the_times

        if type_of_file == "pic" and files_down.endswith(".jpg"):
            the_times = "photo_" + the_times + ".jpg"
            rename(files_down, the_times)
            files_down = the_times

        if "document" not in type_of_file:
            try:
                link = "https://telegra.ph" + tgph(files_down)[0]
                uploaded = f"Uploaded to [Telegraph]({link})"
            except TelegraphException as excp:
                uploaded = f"Message : {excp}"
            end = datetime.now()
            ms = (end - start).seconds
            remove(files_down)
            await kenz.edit(uploaded + f" in `{ms}` seconds.")
            return await deleted(incident)

        try:
            with open(files_down, "rb") as file:
                with suppress(OSError):
                    rply = file.read()
                    remove(files_down)
        except OSError as excp:
            await univ.send_message(str(excp))

    kenz = await incident.reply("Posting...")
    users_names = await univ.get_entity(rply.from_id)
    my_names = users_names.first_name
    univ.me = await univ.get_me()
    my_usrnm = f"https://t.me/{univ.me.username}"
    universal = Telegraph()
    universal.create_account(short_name=my_names, author_url=my_usrnm)

    pushed = universal.create_page(title=my_names, content=[content])
    output = pushed["url"]

    await kenz.edit(f"Telegraph: [Telegraph]({output})")
    await deleted(incident)
