# Copyright (C) 2022 Unknown <https://github.com/unknownkz/universe>
# All Rights Reserved
#
# Credits : @unknownkz (axel)
# This file is a part of < https://github.com/unknownkz/universe/ >
# PLease read the GNU Affero General Public License in;
# < https://www.github.com/unknownkz/universe/main/LICENSE/ >

from telethon import events

from .. import univ
from ..EquipmentTools import deleted

category = "fun"


@univ.universe_cloud(
    pattern=r"qy(?:\s|$)([\s\S]*)",
    command=("qy <Text/Reply>", category),
)
async def _(incident):
    KENTZY = True
    point = incident.pattern_match.group(1)
    if incident.fwd_from:
        return
    reply = await incident.get_reply_message()
    if point:
        quote = point
    elif reply:
        quote = reply
    else:
        return
    bot = "@QuotLyBot"
    xx = await incident.reply("⚡️")

    async with univ.conversation(bot) as bot_conv:
        if KENTZY:
            if point:
                response = await __qy__(bot_conv, quote)
            elif reply:
                response = bot_conv.wait_event(
                    events.NewMessage(incoming=True, from_users=1031952739)
                )
                await univ.forward_messages(bot, quote)
                response = await response
                response = response.message
            if response.text.startswith("Command"):
                await incident.edit("Invalid message type.")
                return
            await xx.reply(response)

    await xx.delete()
    return await deleted(incident)


async def __qy__(conv, text):
    await conv.send_message(text)
    response = await conv.get_response()
    await conv.mark_read(message=response)
    return response
