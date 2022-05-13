# Copyright (C) 2022 Unknown <https://github.com/unknownkz/universe>
# All Rights Reserved
#
# Credits : @unknownkz (axel)
# This file is a part of < https://github.com/unknownkz/universe/ >
# PLease read the GNU Affero General Public License in;
# < https://www.github.com/unknownkz/universe/main/LICENSE/ >

from tracemalloc import start
from sys import exit, setrecursionlimit
from aiorun import run
from asyncio import CancelledError, gather, sleep
from asyncio.base_events import BaseEventLoop
from signal import SIGINT, SIGTERM, SIGPIPE
from importlib import import_module as import_outer_dimensions

from universe.Ground import Rotation, univ
from universe.main import base_core, outer_dimensions
from universe.UniverseLogger import UniverseLogger as UL

x = 5000
setrecursionlimit(x)
start()


async def pushkov():
    try:
        OuterDimensions = outer_dimensions()
        [
            import_outer_dimensions("universe.OuterDimensions." + galaxy)
            for galaxy in OuterDimensions
        ]
        UL.info(
            "Get hold of {} : {}\n✅ File submission successful.".format(
                len(OuterDimensions), str(OuterDimensions)
            )
        )
    except (ModuleNotFoundError, ImportError) as excp:
        UL.error(f"[Dimensions] Error : {excp}")
        exit(1)


async def main():
    """Raised..."""
    try:
        await base_core()
        await univ.run_until_disconnected()
    except (
        RuntimeError,
        NotImplementedError,
        ConnectionError,
        RecursionError,
        CancelledError,
    ):
        pass
    finally:
        await univ.disconnect()


async def whatever():
    for signal_enum in [SIGINT, SIGTERM, SIGPIPE]:
        Rotation.add_signal_handler(
            signal_enum,
            BaseEventLoop.run_until_complete(Rotation, main()).stop,
        )
        Rotation.add_signal_handler(
            signal_enum,
            BaseEventLoop.run_until_complete(Rotation, pushkov()).stop,
        )
    await sleep(5)


if __name__ == "__main__":
    gather(
        *(
            BaseEventLoop.run_until_complete(Rotation, pushkov()),
            BaseEventLoop.run_until_complete(Rotation, main()),
        )
    )
    try:
        gather(
            *(
                run(pushkov(), stop_on_unhandled_errors=True),
                run(main(), stop_on_unhandled_errors=True),
                run(whatever(), stop_on_unhandled_errors=True),
            )
        )
        Rotation.close()

        raise (SystemExit(main(), pushkov(), whatever()))
    except SystemExit:
        pass
