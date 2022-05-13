# Copyright (C) 2022 Unknown <https://github.com/unknownkz/universe>
# All Rights Reserved
#
# Credits : @unknownkz (axel)
# This file is a part of < https://github.com/unknownkz/universe/ >
# PLease read the GNU Affero General Public License in;
# < https://www.github.com/unknownkz/universe/main/LICENSE/ >

from sys import exit
from pathlib import Path

Checker: Path = Path(__file__).parent.parent

dirs = ["/root/universe/universe/Configuration/configuration.py"]
for _ in dirs:
    if not (Checker / _).exists():
        print("| [WARNING] | File configuration.py not found !!")
        exit(1)

try:
    from .configuration import UniverseConfiguration as MultiVerse

except ImportError:
    exit(1)
