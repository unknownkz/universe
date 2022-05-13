# Copyright (C) 2022 Unknown <https://github.com/unknownkz/universe>
# All Rights Reserved
#
# Credits : @catuserbot
# This file is a part of < https://github.com/unknownkz/universe/ >
# PLease read the GNU Affero General Public License in;
# < https://www.github.com/unknownkz/universe/main/LICENSE/ >

from sys import exit
from asyncio import get_event_loop as All_Star
from telethon import connection
from telethon.sessions import StringSession

from ..UniverseLogger import UniverseLogger
from ..Configuration import MultiVerse
from ..ClassFundamental import StartUniverse

UniverseVersion = "Infinity"
Rotation = All_Star()


if MultiVerse.Telethon_String:
    flexible = StringSession(str(MultiVerse.Telethon_String))
else:
    flexible = "universal"

try:
    univ = StartUniverse(
        session=flexible,
        api_id=MultiVerse.Api_ID,
        api_hash=MultiVerse.Api_Hash,
        loop=Rotation,
        app_version=UniverseVersion,
        connection=connection.ConnectionTcpAbridged,
        auto_reconnect=True,
        base_logger=UniverseLogger,
        retry_delay=5,
        flood_sleep_threshold=17,
        connection_retries=None,
        system_lang_code="lang_code",
        use_ipv6=False,
    )
except Exception as excp:
    UniverseLogger(f"{excp}")
    exit()
