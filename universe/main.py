# Copyright (C) 2022 Unknown <https://github.com/unknownkz/universe>
# All Rights Reserved
#
# Credits : @unknownkz (axel)
# This file is a part of < https://github.com/unknownkz/universe/ >
# PLease read the GNU Affero General Public License in;
# < https://www.github.com/unknownkz/universe/main/LICENSE/ >

from logging import getLogger
from sys import exit
from telethon.errors import NetworkMigrateError, RPCError
from telethon.tl.functions.channels import JoinChannelRequest

from .Configuration import MultiVerse
from .Ground.another import univ
from . import Rooters

UL = getLogger(__file__)


async def connected() -> None:
    """Bug ? 😏"""
    try:
        await univ.connect()
        univ.session.set_dc(
            MultiVerse.DC, f"{MultiVerse.MProtoServer}", MultiVerse.Port
        )
        await univ(JoinChannelRequest(channel="@kastaot"))
        UL.info("✅ Success, you are logged in.")
    except (NetworkMigrateError, RPCError) as excp:
        UL.error("Problems: {}".format(excp))
        exit(1)


def outer_dimensions():
    return sorted(
        [
            f.stem
            for f in (Rooters / "universe/OuterDimensions").rglob("*.py")
            if f.is_file() and not str(f).endswith("__init__.py")
        ]
    )


async def base_core() -> None:
    """Bug ? 😏"""
    await connected()
