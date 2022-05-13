# Copyright (C) 2022 Unknown <https://github.com/unknownkz/universe>
# All Rights Reserved
#
# Credits : @unknownkz (axel)
# This file is a part of < https://github.com/unknownkz/universe/ >
# PLease read the GNU Affero General Public License in;
# < https://www.github.com/unknownkz/universe/main/LICENSE/ >

from contextlib import suppress
from time import sleep

from .ProgramAndTime import md_to_text as mtt


async def deleted(incident):
    with suppress(BaseException):
        sleep(5)
        return await incident.delete()


async def edits_then_delete(
    incident, text, parse_mode=None, link_preview=None, **args
):
    parse_mode = parse_mode or "md" or "html"
    link_preview = False if parse_mode == "html" else True
    if incident.sender_id:
        await incident.reply(
            text, link_preview=link_preview, parse_mode=parse_mode
        )
        return None

        reply_to_msg = await incident.get_reply_message()
        if reply_to_msg:
            await incident.reply(
                text, link_preview=link_preview, parse_mode=parse_mode
            )
            return None

    else:
        await incident.edit(
            text, link_preview=link_preview, parse_mode=parse_mode
        )


async def edits_or_reply(
    incident, text, link_preview=None, parse_mode=None, **args
):
    parse_mode = parse_mode or "md" or "html"
    link_preview = False if parse_mode == "html" else True
    reply_to = await incident.get_reply_message()
    if len(text) <= 4096:
        if reply_to:
            from .. import univ

            await univ.send_message(
                incident.chat_id,
                text,
                parse_mode=parse_mode,
                reply_to=reply_to,
                link_preview=link_preview,
            )
            await deleted(incident)
        await incident.edit(
            text, parse_mode=parse_mode, link_preview=link_preview
        )
        return incident

    else:
        from universe import Rooters

        text = mtt(text)
        files = "MessageOutput.txt"
        with open(files, "w+") as paradox:
            paradox.write(text)
        with suppress(BaseException):
            await incident.client.send_file(
                incident.chat_id,
                file=files,
                caption="Message too long or large size.",
                force_document=True,
                allow_cache=False,
                parse_mode="md",
                reply_to=reply_to,
            )
        (Rooters / files).unlink(missing_ok=True)
        return await deleted(incident)
