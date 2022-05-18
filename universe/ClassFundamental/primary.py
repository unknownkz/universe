# Copyright (C) 2022 Unknown <https://github.com/unknownkz/universe>
# All Rights Reserved
#
# Credits : @unknownkz (axel)
# This file is a part of < https://github.com/unknownkz/universe/ >
# PLease read the GNU Affero General Public License in;
# < https://www.github.com/unknownkz/universe/main/LICENSE/ >

import sys
import re
import inspect
from datetime import datetime
from asyncio import get_event_loop as All_Star
from asyncio import sleep, CancelledError
from io import BytesIO
from pathlib import Path
from traceback import format_exc as fmex
from contextlib import suppress
from telethon.events import StopPropagation
from telethon import TelegramClient as McQ
from telethon import events, types
from telethon.errors import (
    AuthKeyDuplicatedError,
    ChatSendGifsForbiddenError,
    ChatSendInlineForbiddenError,
    ChatSendMediaForbiddenError,
    ChatSendStickersForbiddenError,
    ChatWriteForbiddenError,
    FloodWaitError,
    MessageDeleteForbiddenError,
    MessageIdInvalidError,
    MessageNotModifiedError,
)

from ..UniverseLogger import tz
from ..UniverseLogger import UniverseLogger as UL
from ..EquipmentTools import etd, tf, dn, mtt, eor, RunningCommand
from ..Configuration import MultiVerse
from .globals import (
    Reloaded_Command,
    Information_OuterDimensions,
    Information_Group,
    Information_Command,
)

Rotation = All_Star()


def instance(regular_expression, anomaly):
    if regular_expression.startswith(("^", ".")):
        regular_expression = regular_expression[1:]
    if anomaly == "\\ ":
        return re.compile("^" + regular_expression)

    return re.compile(anomaly + regular_expression)


@events.common.name_inner_event
class NewMessage(events.NewMessage):
    def __init__(self, require_admin: bool = None, **kwargs):
        super().__init__(**kwargs)

        self.require_admin = require_admin

    def filter(self, incident):
        checker = super().filter(incident)
        if not checker:
            return

        if self.require_admin and not isinstance(
            incident.chat_id, types.PeerUser
        ):
            is_creator = False
            is_admin = False
            creator = hasattr(incident.chat, "creator")
            admin_rights = hasattr(incident.chat, "admin_rights")
            flag = None
            if not creator and not admin_rights:
                try:
                    incident.chat = Rotation.create_task(incident.get_chat())
                except AttributeError:
                    flag = "Null"

            if self.incoming:
                try:
                    p = Rotation.create_task(
                        incident.client.get_permissions(
                            incident.chat_id, incident.sender_id
                        )
                    )
                    participant = p.participant
                except Exception:
                    participant = None
                if isinstance(participant, types.ChannelParticipantCreator):
                    is_creator = True
                if isinstance(participant, types.ChannelParticipantAdmin):
                    is_admin = True
            elif flag:
                is_admin = True
                is_creator = False
            else:
                is_creator = incident.chat.creator
                is_admin = incident.chat.admin_rights

            if not is_creator and not is_admin:
                text = "I need admin rights to be able to use this command!"

                Rotation.create_task(eor(incident, text))
                return
        return incident


@events.common.name_inner_event
class MessageEdited(NewMessage):
    @classmethod
    def build(cls, update, others=None, self_id=None):
        if isinstance(update, types.UpdateEditMessage):
            return cls.Event(update.message)
        if isinstance(update, types.UpdateEditChannelMessage):
            if (
                update.message.edit_date
                and update.message.is_channel
                and not update.message.is_group
            ):
                return
            return cls.Event(update.message)

    class Event(NewMessage.Event):
        pass


class StartUniverse(McQ):
    def universe_cloud(
        self: McQ,
        pattern: str or tuple = None,
        groups_only: bool = False,
        private_only: bool = False,
        edited: bool = True,
        disable_errors: bool = False,
        command: str or tuple = None,
        senders: bool = None,
        **kwargs,
    ) -> callable:
        kwargs["func"] = kwargs.get(
            "func", lambda anonym: anonym.via_bot_id is None
        )
        kwargs["blacklist_chats"] = kwargs.get("blacklist_chats", False)
        kwargs["forwards"] = kwargs.get("forwards", False)
        stack = inspect.stack()
        previous_stack_frame = stack[1]
        outer_dimensions = Path(previous_stack_frame.filename)
        outer_dimensions = outer_dimensions.stem.replace(".py", "")

        if command is not None:
            command = list(command)
            if not command[1] in Information_Command:
                Information_Command.append(command[1])
        try:
            if outer_dimensions not in Information_Group[command[1]]:
                Information_Group[command[1]].append(outer_dimensions)
        except BaseException:
            Information_Group.update({command[1]: [outer_dimensions]})

        try:
            if command[0] not in Information_OuterDimensions[outer_dimensions]:
                Information_OuterDimensions[outer_dimensions].append(
                    command[0]
                )
        except BaseException:
            Information_OuterDimensions.update(
                {outer_dimensions: [command[0]]}
            )

        make_sense = True if senders else False
        if pattern is not None:
            high_and_low = "$" if make_sense else MultiVerse.Trigger
            instance(pattern, "\\" + high_and_low)

        def decorator(func):
            async def wrapper(check):
                chat = check.chat
                chat_id = check.chat_id or check.from_id

                if groups_only and not check.is_group:
                    return await etd(check, "Sorry this is not a Group.")

                if private_only and not check.is_private:
                    return await etd(
                        check, "Sorry, this is not a Personal Chat."
                    )

                try:
                    await func(check)
                except StopPropagation:
                    raise StopPropagation

                except FloodWaitError as excp:
                    FLOOD_WAIT = excp.seconds
                    FLOOD_WAIT_HUMAN = tf((FLOOD_WAIT + 5) * 1000)
                    UL.error(
                        f"A Flood Wait of {FLOOD_WAIT} and Sleep for {FLOOD_WAIT_HUMAN} !!"
                    )
                    with suppress(BaseException):
                        await check.delete()
                    await sleep(FLOOD_WAIT + 5)
                    return
                except (
                    MessageIdInvalidError,
                    MessageNotModifiedError,
                    MessageDeleteForbiddenError,
                    ChatWriteForbiddenError,
                    ChatSendMediaForbiddenError,
                    ChatSendGifsForbiddenError,
                    ChatSendStickersForbiddenError,
                    ChatSendInlineForbiddenError,
                    CancelledError,
                    ConnectionError,
                    KeyboardInterrupt,
                    SystemExit,
                ):
                    pass
                except AuthKeyDuplicatedError:
                    UL.error(
                        "Your Telethon_String has been expired.Please create new again."
                    )
                    sys.exit(0)
                except Exception as excp:
                    UL.exception(f"Message: {excp}")
                    if not disable_errors:
                        date = datetime.now(tz).strftime(
                            "%d/%m/%Y %I:%M:%S %p"
                        )
                        group_name = dn(chat)
                        format_text = "==== ⚠️ Attention ⚠️ ===="
                        format_text += "\nUniverse is having Problems."
                        format_text += "\n(Please report issue to @kastaot)"
                        format_text += "\n\n• Datetime: " + date
                        format_text += "\n• Group ID: " + str(chat_id)
                        format_text += "\n• Group Name: " + str(group_name)
                        format_text += "\n• User ID: " + str(check.sender_id)
                        format_text += "\n\nEvidence ⬇️"
                        format_text += "\n\n🚨 Replied: " + str(check.is_reply)
                        format_text += "\n🚨 Event Trigger: " + str(check.text)
                        format_text += "\n🚨 Traceback: " + str(fmex())
                        format_text += "\n🚨 Error text: " + str(
                            sys.exc_info()[1]
                        )
                        format_text += "\n\n====== History Commit ======"
                        format_text += "\n\nLast 5 Commit: \n"
                        stdout, stderr = await RunningCommand(
                            'git log --pretty=format:"%an: %s" -5'
                        )
                        result = stdout + stderr
                        format_text += result + "`"

                        with suppress(BaseException):
                            if len(format_text) > 4096:
                                format_text = mtt(format_text)
                                with BytesIO(format_text.encode()) as files:
                                    files.name = "UniverseErrors.txt"
                                    await check.client.send_file(
                                        chat_id,
                                        file=files,
                                        caption="Universe has been Trouble\nPlease report issue to @kastaot",
                                        force_document=True,
                                        allow_cache=False,
                                    )
                            else:
                                await check.client.send_message(
                                    chat_id,
                                    format_text,
                                    link_preview=False,
                                    silent=True,
                                )

            from ..Ground import univ

            make_sense = True if senders else False
            if pattern:
                high_and_low = "$" if make_sense else MultiVerse.Trigger
                pers = instance(pattern, "\\" + high_and_low)

                if command is not None:
                    if (
                        command[0] in Reloaded_Command
                        and wrapper in Reloaded_Command[command[0]]
                    ):
                        return None

                    try:
                        Reloaded_Command[command[0]].append(wrapper)
                    except BaseException:
                        Reloaded_Command.update({command[0]: [wrapper]})

                if edited:
                    univ.add_event_handler(
                        wrapper,
                        MessageEdited(pattern=pers, outgoing=True, **kwargs),
                    )
                univ.add_event_handler(
                    wrapper,
                    NewMessage(pattern=pers, outgoing=True, **kwargs),
                )

            else:
                if (
                    outer_dimensions in Reloaded_Command
                    and func in Reloaded_Command[outer_dimensions]
                ):
                    return None
                try:
                    Reloaded_Command[outer_dimensions].append(func)
                except BaseException:
                    Reloaded_Command.update({outer_dimensions: [func]})
                if edited:
                    univ.add_event_handler(
                        func, events.MessageEdited(**kwargs)
                    )
                univ.add_event_handler(func, events.NewMessage(**kwargs))

            return wrapper

        return decorator
