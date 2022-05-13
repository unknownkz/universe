"""
Create new configuration.py, don't rename this file.
"""
# Copyright (C) 2022 Unknown <https://github.com/unknownkz/universe>
# All Rights Reserved
#
# Credits : @unknownkz (axel)
# This file is a part of < https://github.com/unknownkz/universe/ >
# PLease read the GNU Affero General Public License in;
# < https://www.github.com/unknownkz/universe/main/LICENSE/ >

from os import getenv as then_get


class UniverseConfiguration:
    ### Required for Telegram Api
    # get it at my.telegram.org | api development tools | then fill
    Api_ID = int(then_get("Api_ID", ""))
    Api_Hash = str(then_get("Api_Hash", ""))
    # Mobile Phone Number... Don't forget your country code
    # this is for your telethon string in local data, so you don't refill it again
    # later you just need a verification code from telegram
    MobilePhoneNumber = str(then_get("MobilePhoneNumber", "+62"))

    # look in README.md for a description of how to get the Telethon String.
    Telethon_String = str(then_get("Telethon_String", ""))

    # DC ID
    DC = int(then_get("DC", ""))
    # MTProto servers
    # get it at my.telegram.org | api development tools | Available MTProto servers
    # Note that port 443 might not work, so you can try with 80 instead.
    MProtoServer = then_get("MProtoServer", "")
    # Port > 80
    Port = int(then_get("Port", "80"))

    ### File for Active / Alive
    # File Support : .mp4 | .jpg ! .jpeg | .png
    # Recommended from telegra.ph
    Info_Active = then_get(
        "Info_Active", "https://telegra.ph/file/8271c781a36ccff1ee4aa.mp4"
    )

    ### Command
    # Your controller. this is the same as the command prompt.
    Trigger = "."

    ### Logger Information
    # add @MissRose_Bot to ur chat and write /id to get ur chat id
    Logger_ID = then_get("Logger_ID", "")
    # Go to @BotFather on Telegram, type /newbots | then follow the steps | If finished then take the Bot Token.
    Token_Bot = str(then_get("Token_Bot", ""))

    ### Time Zone
    # Continent/Country
    # Example : Asia/Jakarta
    # If you want to find your local area, search in https://www.timeanddate.com/time/zone/timezone/utc
    TZ = then_get("TimeZone", "Asia/Jakarta")
