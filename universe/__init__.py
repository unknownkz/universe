# Copyright (C) 2022 Unknown <https://github.com/unknownkz/universe>
# All Rights Reserved
#
# Credits : @notudope
# This file is a part of < https://github.com/unknownkz/universe/ >
# PLease read the GNU Affero General Public License in;
# < https://www.github.com/unknownkz/universe/main/LICENSE/ >

from sys import platform, maxsize, version_info, exit
from time import time
from pathlib import Path
from platform import system, machine

from .UniverseLogger import UniverseLogger as UL
from .Ground.another import univ

start_time = time()


__version = "Infinity"
__license = "GNU GPL-3.0 License"

if platform.startswith("linux") and maxsize == 2 ** 63 - 1:
    platform = system()
    machine = machine()
    UL.info(
        "You're running universe on the system {} {}".format(
            str(platform),
            str(machine),
        )
    )
else:
    platform = system()
    architecture = "64-bit"
    UL.error(
        "You've to use {} {} system first!".format(str(platform), architecture)
    )
    exit(1)


if (
    version_info.major == 3
    and version_info.minor >= 8
    and version_info.micro >= 0
):
    major = version_info.major
    minor = version_info.minor
    micro = version_info.micro
    UL.info(
        "You're running universe on the python {}.{}.{}".format(
            str(round(major)),
            str(round(minor)),
            str(round(micro)),
        )
    )
else:
    major = 3
    minor = 8
    UL.error(
        "You've to use python version of at least >= {}.{}.x ! quitting..".format(
            str(round(major)),
            str(round(minor)),
        )
    )
    exit(1)


Rooters: Path = Path(__file__).parent.parent

dirs = ["cache"]
for _ in dirs:
    if not (Rooters / _).exists():
        (Rooters / _).mkdir(parents=True, exist_ok=True)
    else:
        for f in (Rooters / _).rglob("*.*"):
            if f.exists():
                f.unlink(missing_ok=True)
