# Copyright (C) 2022 Unknown <https://github.com/unknownkz/universe>
# All Rights Reserved
#
# Credits : @unknownkz (axel)
# This file is a part of < https://github.com/unknownkz/universe/ >
# PLease read the GNU Affero General Public License in;
# < https://www.github.com/unknownkz/universe/main/LICENSE/ >

from re import split
from carbon import Carbon, CarbonOptions
from contextlib import suppress
from io import BytesIO, StringIO
from time import sleep

from .. import univ, Rooters
from ..EquipmentTools import RunningCommand, deleted, mtt
from ..Configuration import MultiVerse
from ..Ground import Rotation

category = "core"

u = MultiVerse.Trigger

bash_command = f"""
**Command Guide ›**

__Running the bash command from the
telegram message to your terminal.__

`{u}term -run <bla bla bla>`

**Example:**
Run › `{u}term -run ping -c 1 127.0.0.1`
Run › `{u}term -run cd universe && ls`
Run › `{u}term -run pip3 install telethon`
Run › `{u}term -run git pull origin main`
Run › `{u}term -run git config -l`
Run › `{u}term -run echo "Hello World"`
Run › `{u}term -run echo "Iam nuub" | base64`
Run › `{u}term -run echo "Z2l0IGZldGNoIG9yaWdpbiBtYWluCg==" | base64 -d`

**Depends on you**
"""


@univ.universe_cloud(
    pattern=r"term(?: |$)(-run)?(?: |$)(.*)",
    command=("term -run <cmd>", category),
)
async def _(incident):
    point = incident.pattern_match.group(1)
    commander = incident.pattern_match.group(2)
    options = split("√π÷×¶∆•!?", commander)  # <- Filter text
    if len(options) <= 0:
        return False

    elif point and point == "-run" and commander:
        stdout, stderr = await RunningCommand(str(options[0]))
        inform = stdout + stderr
        textt = inform
        if len(textt) <= 0:
            bmt = "✅ Successfuly"
            sleep(5)
            return await univ.send_message(incident.chat_id, bmt, silent=True)

        elif len(textt) >= 4096:
            with suppress(BaseException):
                textt = mtt(textt)
                with BytesIO(textt.encode()) as files:
                    files.name = "Bash.txt"
                    await univ.send_file(
                        incident.chat_id,
                        file=files,
                        caption="Message Large",
                        force_document=True,
                        allow_cache=False,
                    )

        else:
            with suppress(BaseException):
                xx = await incident.reply("`Execute...`")
                textt = mtt(textt)
                with BytesIO(textt.encode("utf-8")) as byts_io:
                    byts_io.name = "bash.txt"
                    byts_str = byts_io.read()
                    with StringIO(byts_str.decode("utf-8")) as conv:
                        schdl = conv.read()
                        languag = "auto"
                        cb_options = CarbonOptions(
                            code=schdl, language=languag
                        )
                        cb = Carbon()
                        img = Rotation.run_until_complete(
                            cb.generate(cb_options)
                        )
                        Rotation.run_until_complete(img.save("bash"))
                        bs = "bash.png"
                        await univ.send_file(
                            incident.chat_id,
                            file=bs,
                            force_document=True,
                            silent=True,
                        )

                    (Rooters / bs).unlink(missing_ok=True)

                (Rooters / "bash.txt").unlink(missing_ok=True)
                await xx.delete()

    else:
        await incident.reply(bash_command)

    return await deleted(incident)
