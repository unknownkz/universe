# Copyright (C) 2022 Unknown <https://github.com/unknownkz/universe>
# All Rights Reserved
#
# Credits : @unknownkz (axel)
# This file is a part of < https://github.com/unknownkz/universe/ >
# PLease read the GNU Affero General Public License in;
# < https://www.github.com/unknownkz/universe/main/LICENSE/ >

import logging
from tglogging import TelegramLogHandler

from ..Configuration import MultiVerse
from .fmt_tm_universe import UniverseTimeZone

UniverseLogger = logging
UniverseLogger.Formatter.converter = UniverseTimeZone
UniverseLogger.basicConfig(
    level=UniverseLogger.INFO,
    format="[%(asctime)s | %(levelname)s | File: %(filename)s | Name: %(name)s | Func: %(funcName)s | Message: %(message)s]",
    datefmt="%d/%b/%y | %I:%M:%S %p",
    handlers=[
        TelegramLogHandler(
            token=MultiVerse.Token_Bot,
            log_chat_id=MultiVerse.Logger_ID,
            update_interval=5,
            minimum_lines=5,
            pending_logs=200000,
        ),
        UniverseLogger.StreamHandler(),
    ],
)

UniverseLogger.getLogger(__file__)
UniverseLogger.getLevelName(UniverseLogger.DEBUG)
UniverseLogger.getLevelName(UniverseLogger.INFO)
UniverseLogger.getLevelName(UniverseLogger.WARN)
UniverseLogger.getLevelName(UniverseLogger.ERROR)
UniverseLogger.getLevelName(UniverseLogger.CRITICAL)
UniverseLogger.getLevelName(UniverseLogger.FATAL)
UniverseLogger.getLevelName(UniverseLogger.NOTSET)
