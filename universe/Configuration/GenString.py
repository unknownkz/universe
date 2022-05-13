# Copyright (C) 2022 Unknown <https://github.com/unknownkz/universe>
# All Rights Reserved
#
# Credits : @unknownkz (axel)
# This file is a part of < https://github.com/unknownkz/universe/ >
# PLease read the GNU Affero General Public License in;
# < https://www.github.com/unknownkz/universe/main/LICENSE/ >

from sys import exit
from pathlib import Path
from telethon.sessions import StringSession
from telethon.sync import TelegramClient
from telethon.errors import (
    PhoneCodeInvalidError,
    SessionPasswordNeededError,
    FloodError,
)


StringCheck: Path = Path(__file__).parent.parent

dirs = ["/root/universe/universe/Configuration/configuration.py"]
for _ in dirs:
    if not (StringCheck / _).exists():
        print("| [WARNING] | File configuration.py not found !!")
        exit(1)

try:
    from configuration import UniverseConfiguration as config

except ImportError:
    exit(1)


desc = """
Thank you very much for using this script.

<code>Telethon_String</code>:

<code>{}</code>

⚠️ <b>Please be carefull to pass this value to third parties</b>

Credits : @TelethonUpdates

Managed by : @GroupTidakDiketahui
"""
print("")
print("\x1b[1;93m[ Telethon ]")
print("")
print("""Maintainer : @xelyourslurred <unknownkz@outlook.co.id>""")
print("")
print("")

api_id = config.Api_ID
api_hash = config.Api_Hash
phone_number = config.MobilePhoneNumber

FlyMeToTheMoon = True


while FlyMeToTheMoon:
    try:
        with TelegramClient(
            StringSession(), api_id=api_id, api_hash=api_hash
        ).start(phone=phone_number) as StartUniverse:
            StartUniverse.send_code_request(phone=phone_number)
            print("")
            galaxy = StartUniverse.session.save()
            messages_temp = desc.format(galaxy)
            StartUniverse.send_message("me", messages_temp, parse_mode="html")
            print(
                "Your Telethon_String value have been sent to ur Telegram <Saved Messages>"
            )
    except BaseException as excp:
        print(excp)
    except ValueError as value:
        print(value)
    except PhoneCodeInvalidError as invalid:
        print(invalid)
    except SessionPasswordNeededError as pw:
        print(pw)
    except FloodError as cx:
        print(cx)
    except ConnectionError:
        raise RuntimeError
        continue
    break
