# Copyright (C) 2022 Unknown <https://github.com/unknownkz/universe>
# All Rights Reserved
#
# Credits : @unknownkz (axel)
# This file is a part of < https://github.com/unknownkz/universe/ >
# PLease read the GNU Affero General Public License in;
# < https://www.github.com/unknownkz/universe/main/LICENSE/ >

from datetime import datetime
from pytz import timezone

from ..Configuration import MultiVerse

tz = timezone(MultiVerse.TZ)


def UniverseTimeZone(*args):
    return datetime.now(tz).timetuple()
