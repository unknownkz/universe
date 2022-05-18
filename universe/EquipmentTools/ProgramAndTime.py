# Copyright (C) 2022 Unknown <https://github.com/unknownkz/universe>
# All Rights Reserved
#
# This file is a part of < https://github.com/unknownkz/universe/ >
# PLease read the GNU Affero General Public License in;
# < https://www.github.com/unknownkz/universe/main/LICENSE/ >

import asyncio
from time import time
from datetime import datetime
from typing import Union
from telethon.utils import get_display_name, add_surrogate
from bs4 import BeautifulSoup
from markdown import markdown
from subprocess import SubprocessError
from telethon.tl.types import MessageEntityMentionName, MessageEntityPre
from telethon.tl.tlobject import TLObject
from functools import partial

from ..UniverseLogger import UniverseLogger as UL


def md_to_text(md: str) -> str:
    html = markdown(md)
    soup = BeautifulSoup(html, features="html.parser")
    return soup.get_text()


def display_names(user) -> str:
    name = get_display_name(user)
    return name if name else "{}".format(user.first_name)


def time_formatter(ms: Union[int, str]) -> str:
    """Credits : @kastaid"""
    minutes, seconds = divmod(int(ms / 1000), 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    weeks, days = divmod(days, 7)
    tmp = (
        ((str(weeks) + "w:") if weeks else "")
        + ((str(days) + "d:") if days else "")
        + ((str(hours) + "h:") if hours else "")
        + ((str(minutes) + "m:") if minutes else "")
        + ((str(seconds) + "s") if seconds else "")
    )
    if tmp:
        return tmp[:-1] if tmp.endswith(":") else tmp
    else:
        return "0s"


async def RunningCommand(cmd: str) -> (bytes, bytes):
    try:
        process = await asyncio.create_subprocess_shell(
            cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        err = stderr.decode().strip()
        out = stdout.decode().strip()
        return out, err
    except SubprocessError as excp:
        UL.error(str(excp))


def get_data_size(size: Union[int, float]) -> str:
    if not size:
        return "0B"
    for _ in ["", "K", "M", "G", "T"]:
        if size < 1024:
            break
        size /= 1024
    if isinstance(size, int):
        size = f"{size}{_}B"
    elif isinstance(size, float):
        size = f"{size:.2f}{_}B"
    return size


def attributes_media(media):
    set_media = str((str(media)).split("(", maxsplit=1)[0])
    media_info = ""
    if set_media == "MessageMediaDocument":
        typ_mime = media.document.mime_type
        if typ_mime == "application/x-tgsticker":
            media_info = "sticker animated"
        elif "image" in typ_mime:
            if typ_mime == "image/webp":
                media_info = "sticker"
            elif typ_mime == "image/gif":
                media_info = "gif as doc"
            elif typ_mime == "image/bmp":
                media_info = "bmp as doc"
            elif typ_mime == "image/x-tga":
                media_info = "tga as doc"
            elif typ_mime == "image/tiff":
                media_info = "tiff as doc"
            elif typ_mime == "image/png":
                media_info = "png as doc"
            elif typ_mime == "image/vnd.adobe.photoshop":
                media_info = "psd as doc"
            elif typ_mime == "image/jpeg":
                media_info = "jpeg as doc"
            else:
                media_info = "pic as doc"
        elif "video" in typ_mime:
            if "DocumentAttributeAnimated" in str(media):
                media_info = "gif"
            elif "DocumentAttributeVideo" in str(media):
                m_attributes = str(media.document.attributes[0])
                if "supports_streaming=True" in m_attributes:
                    media_info = "video"
                media_info = "video as doc"
            else:
                media_info = "video"
        elif "audio" in typ_mime:
            media_info = "audio"
        else:
            media_info = "document"
    elif set_media == "MessageMediaPhoto":
        media_info = "pic"
    elif set_media == "MessageMediaWebPage":
        media_info = "web"
    return media_info


async def get_info_user(incident, group=1):
    args = incident.pattern_match.group(group).split(" ", 1)
    extra = None
    await incident.get_chat()
    try:
        if args:
            user = args[0]
            if len(args) > 1:
                extra = "".join(args[1:])
            if user.isdecimal() or (
                user.startswith("-") and user[1:].isdecimal()
            ):
                user = int(user)
            if incident.message.entities:
                probable_mention = incident.message.entities[0]
                if isinstance(probable_mention, MessageEntityMentionName):
                    user_id = probable_mention.user_id
                    user_obj = await incident.client.get_entity(user_id)
                    return user_obj, extra
            if isinstance(user, int) or user.startswith("@"):
                user_obj = await incident.client.get_entity(user)
                return user_obj, extra
    except ValueError:
        if args:
            user = args[0]
            if len(args) > 1:
                extra = "".join(args[1:])
            if user.isdecimal() or (
                user.startswith("-") and user[1:].isdecimal()
            ):
                obj = partial(type, "user", ())
                user_obj = obj({"id": int(user), "first_name": user})
                return user_obj, extra
            else:
                return None, None
        else:
            return None, None
    except Exception as e:
        UL.error(str(e))
    try:
        extra = incident.pattern_match.group(group)
        if incident.is_private:
            user_obj = await incident.get_chat()
            return user_obj, extra
        if incident.reply_to_msg_id:
            prev_msg = await incident.get_reply_message()
            if not prev_msg.from_id:
                return None, None
            user_obj = await incident.client.get_entity(prev_msg.sender_id)
            return user_obj, extra
        if not args:
            return None, None
    except Exception as e:
        UL.error(str(e))
    return None, None


def __parse(text):
    text = text.strip()
    return (
        text,
        [
            MessageEntityPre(
                offset=0, length=len(add_surrogate(text)), language=""
            )
        ],
    )


def utc_to_local(utc_datetime):
    now_timestamp = time()
    offset = datetime.fromtimestamp(now_timestamp) - datetime.utcfromtimestamp(
        now_timestamp
    )
    return utc_datetime + offset


def __yaml(obj, indent=0, max_str_len=256, max_byte_len=64):
    # sourcery no-metrics
    """
    Pretty formats the given object as a YAML string which is returned.
    (based on TLObject.pretty_format)
    """
    result = []
    if isinstance(obj, TLObject):
        obj = obj.to_dict()

    if isinstance(obj, dict):
        if not obj:
            return "dict:"

        items = obj.items()
        has_items = len(items) > 1
        has_multiple_items = len(items) > 2
        result.append(obj.get("_", "dict") + (":" if has_items else ""))

        if has_multiple_items:
            result.append("\n")
            indent += 2

        for k, v in items:
            if k == "_" or v is None:
                continue
            formatted = __yaml(v, indent)
            if not formatted.strip():
                continue
            result.append(" " * (indent if has_multiple_items else 1))
            result.append(f"{k}:")

            if not formatted[0].isspace():
                result.append(" ")
            result.append(f"{formatted}")
            result.append("\n")

        if has_items:
            result.pop()

        if has_multiple_items:
            indent -= 2

    elif isinstance(obj, str):
        # truncate long strings and display elipsis
        result = repr(obj[:max_str_len])

        if len(obj) > max_str_len:
            result += "…"
        return result

    elif isinstance(obj, bytes):
        # repr() bytes if it's printable, hex like "FF EE BB" otherwise
        if all(0x20 <= c < 0x7F for c in obj):
            return repr(obj)
        return (
            "<…>"
            if len(obj) > max_byte_len
            else " ".join(f"{b:02X}" for b in obj)
        )

    elif isinstance(obj, datetime):
        # ISO-8601 without timezone offset (telethon dates are always UTC)
        return utc_to_local(obj).strftime("%Y-%m-%d %H:%M:%S")

    elif hasattr(obj, "__iter__"):
        # display iterables one after another at the base indentation level
        result.append("\n")
        indent += 2
        for x in obj:
            result.append(f"{' ' * indent}- {__yaml(x, indent + 2)}")
            result.append("\n")
        result.pop()
        indent -= 2

    else:
        return repr(obj)

    return "".join(result)


async def __guser(
    incident,
    seconds_party=None,
    thirds_party=None,
    none_party=False,
    none_edits=False,
):  # sourcery no-metrics
    if none_party is False:
        if seconds_party:
            args = incident.pattern_match.group(2).split(" ", 1)
        elif thirds_party:
            args = incident.pattern_match.group(3).split(" ", 1)
        else:
            args = incident.pattern_match.group(1).split(" ", 1)
    extra = None
    try:
        if args:
            user = args[0]
            if len(args) > 1:
                extra = "".join(args[1:])
            if user.isnumeric() or (
                user.startswith("-") and user[1:].isnumeric()
            ):
                user = int(user)
            if incident.message.entities:
                probable_user_mention_entity = incident.message.entities[0]
                if isinstance(
                    probable_user_mention_entity, MessageEntityMentionName
                ):
                    user_id = probable_user_mention_entity.user_id
                    user_obj = await incident.client.get_entity(user_id)
                    return user_obj, extra
            if isinstance(user, int) or user.startswith("@"):
                user_obj = await incident.client.get_entity(user)
                return user_obj, extra
    except Exception as e:
        UL.error(str(e))
    try:
        if none_party is False:
            if seconds_party:
                extra = incident.pattern_match.group(2)
            else:
                extra = incident.pattern_match.group(1)
        if incident.is_private:
            user_obj = await incident.get_chat()
            return user_obj, extra
        if incident.reply_to_msg_id:
            previous_message = await incident.get_reply_message()
            if previous_message.from_id is None:
                if not none_edits:
                    await incident.edit("Well that's an Anonymous Admin !")
                return None, None
            user_obj = await incident.client.get_entity(
                previous_message.sender_id
            )
            return user_obj, extra
        if not args:
            if not none_edits:
                await incident.edit("Pass the User's Username, ID or Reply!")
            return None, None
    except Exception as e:
        UL.error(str(e))
    if not none_edits:
        await incident.edit("__Couldn't fetch user to proceed further.__")
    return None, None
