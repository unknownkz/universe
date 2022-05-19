# Copyright (C) 2022 Unknown <https://github.com/unknownkz/universe>
# All Rights Reserved
#
# Credits : @unknownkz (axel)
# This file is a part of < https://github.com/unknownkz/universe/ >
# PLease read the GNU Affero General Public License in;
# < https://www.github.com/unknownkz/universe/main/LICENSE/ >

from textwrap import dedent, indent
from asyncio.exceptions import TimeoutError as AsyncTimeout
from os import listdir
from re import split
from contextlib import suppress
from youtube_dl import YoutubeDL
from telethon.tl.types import DocumentAttributeAudio
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest
from youtubesearchpython import SearchVideos

from .. import univ, Rooters
from ..EquipmentTools import deleted, attributes_media
from ..UniverseLogger import UniverseLogger as UL

category = "tools"


@univ.universe_cloud(
    pattern=r"ytdl(?: |$)(-audio)?(?: |$)(.*)",
    command=("ytdl -audio <url/search>", category),
)
async def _(incident):
    point = incident.pattern_match.group(1)
    options = incident.pattern_match.group(2)
    exhibition = split(",}{@√π÷×¶∆•", options)  # <- Filter text

    if point != "-audio" and not exhibition:
        return False

    elif len(exhibition) <= 0:
        return False

    else:
        exhibition = split(",}{@", options)
        kz = await incident.reply(f"Getting audio: `{str(exhibition[0])}`")

        searching = SearchVideos(
            "{}".format(str(exhibition[0])),
            offset=1,
            mode="dict",
            max_results=1,
        )
        links = searching.result()
        get_audio = links["search_result"]
        loots = get_audio[0]["link"]
        get_audio[0]["duration"]
        thumbn = get_audio[0]["title"]
        ch = get_audio[0]["channel"]
        url = loots

        opsi = {
            "format": "bestaudio",
            "addmetadata": True,
            "key": "FFmpegMetadata",
            "writethumbnail": True,
            "prefer_ffmpeg": True,
            "geo_bypass": True,
            "nocheckcertificate": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "720",
                }
            ],
            "outtmpl": "%(id)s.mp3",
            "quiet": True,
            "logtostderr": False,
        }
        try:
            with YoutubeDL(opsi) as yt_download:
                informat = yt_download.extract_info(url, False)
                audio_duration = round(informat["duration"] / 90)

            if audio_duration > 90:
                megazine = "90"
                incident.edit(
                    "Audio longer than `{} min` aren't allowed.\nMust be < `{} min`".format(
                        audio_duration, megazine
                    )
                )
                return False
            download_data = yt_download.extract_info(url, download=True)

        except BaseException as excp:
            UL.error(str(excp))
            return False

        cops = dedent(f"**Title :** `{thumbn}` \n**Channel :** `{ch}`")

        xa = listdir()
        if f"{download_data['id']}.mp3.jpg" in xa:
            thumbname = f"{download_data['id']}.mp3.jpg"

        elif f"{download_data['id']}.mp3.webp" in xa:
            thumbname = f"{download_data['id']}.mp3.webp"

        elif f"{download_data['id']}.mp3.part" in xa:
            thumbname = f"{download_data['id']}.mp3.part"

        elif f"{download_data['id']}.mp3" in xa:
            audiof = f"{download_data['id']}.mp3"

        else:
            thumbname = None
            audiof = None

        audiof = f"{download_data['id']}.mp3"
        mz = await kz.edit("Download successful\nPlease wait...")

        with open(audiof, mode="rb") as file:
            file.read()
        with suppress(BaseException):
            await incident.client.send_file(
                incident.chat_id,
                audiof,
                thumb=thumbname,
                supports_streaming=True,
                caption=cops,
                attributes=[
                    DocumentAttributeAudio(
                        duration=int(download_data["duration"]),
                        title=str(download_data["title"]),
                        performer=str(download_data["uploader"]),
                    )
                ],
                reply_to=mz,
            )
            await mz.delete()
            (Rooters / audiof).unlink(missing_ok=True)
            (Rooters / thumbname).unlink(missing_ok=True)
        return await deleted(incident)


@univ.universe_cloud(
    pattern=r"ytdl(?: |$)(-video)?(?: |$)(.*)",
    command=("ytdl -video <url/search>", category),
)
async def _(incident):
    point = incident.pattern_match.group(1)
    options = incident.pattern_match.group(2)
    exhibition = split(",}{@", options)

    if point != "-video" and not exhibition:
        return False

    elif len(exhibition) <= 0:
        return False

    else:
        exhibition = split(",@", options)
        kz = await incident.reply(f"Getting video: `{str(exhibition[0])}`")

        searching = SearchVideos(
            "{}".format(str(exhibition[0])),
            offset=1,
            mode="dict",
            max_results=1,
        )
        links = searching.result()
        get_video = links["search_result"]
        loots = get_video[0]["link"]
        get_video[0]["duration"]
        thumbn = get_video[0]["title"]
        ch = get_video[0]["channel"]
        url = loots

        opsi = {
            "format": "best",
            "addmetadata": True,
            "key": "FFmpegMetadata",
            "prefer_ffmpeg": True,
            "geo_bypass": True,
            "nocheckcertificate": True,
            "postprocessors": [
                {"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}
            ],
            "outtmpl": "%(id)s.mp4",
            "logtostderr": False,
            "quiet": True,
        }
        try:
            with YoutubeDL(opsi) as yt_download:
                informat = yt_download.extract_info(url, False)
                video_duration = round(informat["duration"] / 90)

            if video_duration > 90:
                megazine = "90"
                incident.edit(
                    "Video longer than `{} min` aren't allowed.\nMust be < `{} min`".format(
                        video_duration, megazine
                    )
                )
                return False
            download_data = yt_download.extract_info(url, download=True)

        except BaseException as excp:
            UL.error(str(excp))
            return False

        cps = dedent(f"**Title :** `{thumbn}` \n**Channel :** `{ch}`")

        xv = listdir()
        if f"{download_data['id']}.mp4" in xv:
            videof = f"{download_data['id']}.mp4"

        else:
            videof = None

        videof = f"{download_data['id']}.mp4"
        mz = await kz.edit("Download successful\nPlease wait...")

        with open(videof, mode="rb") as fille:
            fille.read()
        with suppress(BaseException):
            await incident.client.send_file(
                incident.chat_id,
                videof,
                supports_streaming=True,
                caption=cps,
                attributes=[
                    DocumentAttributeAudio(
                        duration=int(download_data["duration"]),
                    )
                ],
                reply_to=mz,
            )
            await mz.delete()
        (Rooters / videof).unlink(missing_ok=True)
        return await deleted(incident)


@univ.universe_cloud(
    pattern=r"pinterest(?: |$)(-dl)?(?: |$)(.*)",
    command=("pinterest -dl <url>", category),
)
async def _(incident):
    mkz = incident.chat_id
    PDOWNLOADER = True
    point = incident.pattern_match.group(1)
    options = incident.pattern_match.group(2)

    if not point:
        return False

    if not options.startswith("https://pin.it/") and not options.startswith(
        "https://id.pinterest.com/pin/"
    ):
        await incident.edit("Link not supported.")

    else:
        kz = await incident.reply("Process...", silent=True)

    conversation_ = "@HK_pinterest_BOT"
    async with univ.conversation(conversation_) as __conv:
        try:
            __start__ = await __conv.send_message("/start")
            __response__ = await __conv.get_response(timeout=2)
            __messages__ = await __conv.send_message(options)
            __vorp__ = await __conv.get_response(timeout=2)
            __vorp1__ = await __conv.get_response(timeout=2)
            await univ.send_read_acknowledge(__conv.chat_id)
        except YouBlockedUserError:
            await univ(UnblockRequest(conversation_))
            __start__ = await __conv.send_message("/start")
            __response__ = await __conv.get_response(timeout=2)
            __messages__ = await __conv.send_message(options)
            __vorp__ = await __conv.get_response(timeout=2)
            __vorp1__ = await __conv.get_response(timeout=2)
            await univ.send_read_acknowledge(__conv.chat_id)

        while PDOWNLOADER:
            try:
                await univ.send_read_acknowledge(__conv.chat_id)
                __vorp__ = await __conv.get_response(timeout=2)
                attributes_media(__vorp__.media)
                files_down = await univ.download_media(__vorp__, "cache")

                if files_down.endswith(".mp4"):
                    data_f = files_down

                elif files_down.endswith(".jpg"):
                    data_f = files_down

                else:
                    data_f = None
                    await univ.send_message(
                        mkz,
                        "Search not found, can't download from that link.",
                        reply_to=kz,
                        silent=True,
                    )

                data_f = files_down
                text_source = "<b>Pinterest Downloader</b>\n"
                text_source += (
                    "<b>Link Source:</b> "
                    + "<a href='"
                    + str(options)
                    + "'>Click Here</a>"
                )
                wrp = indent(text_source, " ", lambda line: False)
                mz = await kz.edit("Please wait...")

                with open(data_f, mode="rb") as fille:
                    fille.read()
                with suppress(BaseException):
                    await univ.send_file(
                        mkz,
                        data_f,
                        caption=wrp,
                        parse_mode="html",
                        reply_to=mz,
                        silent=True,
                    )
                    await univ.delete_messages(
                        __conv.chat_id,
                        [
                            __start__.id,
                            __response__.id,
                            __messages__.id,
                            __vorp__.id,
                            __vorp1__.id,
                        ],
                    )
                    await mz.delete()

                (Rooters / data_f).unlink(missing_ok=True)
                return await deleted(incident)

            except AsyncTimeout:
                break


@univ.universe_cloud(
    pattern=r"twitter(?: |$)(-dl)?(?: |$)(.*)",
    command=("twitter -dl <url>", category),
)
async def _(incident):
    mkz = incident.chat_id
    TDOWNLOADER = True
    point = incident.pattern_match.group(1)
    options = incident.pattern_match.group(2)

    if not point:
        return False

    if not options.startswith("https://twitter.com/"):
        await incident.edit("Link not supported.")

    else:
        kz = await incident.reply("Process...", silent=True)

    conversation_ = "@DownloadTwitbot"
    async with univ.conversation(conversation_) as __conv:
        try:
            __start__ = await __conv.send_message("/start")
            __response__ = await __conv.get_response(timeout=5)
            __messages__ = await __conv.send_message(options)
            __vorp__ = await __conv.get_response(timeout=5)
            await univ.send_read_acknowledge(__conv.chat_id)
        except YouBlockedUserError:
            await univ(UnblockRequest(conversation_))
            __start__ = await __conv.send_message("/start")
            __response__ = await __conv.get_response(timeout=5)
            __messages__ = await __conv.send_message(options)
            __vorp__ = await __conv.get_response(timeout=5)
            await univ.send_read_acknowledge(__conv.chat_id)

        while TDOWNLOADER:
            try:
                await univ.send_read_acknowledge(__conv.chat_id)
                __vorp__ = await __conv.get_response(timeout=5)
                attributes_media(__vorp__.media)
                files_down = await univ.download_media(__vorp__, "cache")

                if files_down.endswith(".mp4"):
                    data_f = files_down

                elif files_down.endswith(".mkv"):
                    data_f = files_down

                elif files_down.endswith(".jpg"):
                    data_f = files_down

                else:
                    data_f = None

                data_f = files_down
                text_source = "<b>Twitter Downloader</b>\n"
                text_source += (
                    "<b>Link Source:</b> "
                    + "<a href='"
                    + str(options)
                    + "'>Click Here</a>"
                )
                wrp = indent(text_source, " ", lambda line: False)
                mz = await kz.edit("Please wait...")

                with open(data_f, mode="rb") as fille:
                    fille.read()
                with suppress(BaseException):
                    await univ.send_file(
                        mkz,
                        data_f,
                        caption=wrp,
                        parse_mode="html",
                        reply_to=mz,
                        silent=True,
                    )
                    await univ.delete_messages(
                        __conv.chat_id,
                        [
                            __start__.id,
                            __response__.id,
                            __messages__.id,
                            __vorp__.id,
                        ],
                    )
                    await mz.delete()

                (Rooters / data_f).unlink(missing_ok=True)
                return await deleted(incident)
            except AsyncTimeout:
                break
