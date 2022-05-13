# Copyright (C) 2022 Unknown <https://github.com/unknownkz/universe>
# All Rights Reserved
#
# Credits : @unknownkz (axel)
# This file is a part of < https://github.com/unknownkz/universe/ >
# PLease read the GNU Affero General Public License in;
# < https://www.github.com/unknownkz/universe/main/LICENSE/ >

from textwrap import dedent
from os import listdir
from re import split
from contextlib import suppress
from youtube_dl import YoutubeDL
from telethon.tl.types import DocumentAttributeAudio
from youtubesearchpython import SearchVideos

from .. import univ, Rooters
from ..EquipmentTools import deleted, eor
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
