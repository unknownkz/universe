### Configuration
> Note :
>> for sample-configuration.py u must be create new or copy file. Don't rename file!!!
>>> create file ›› configuration.py ‹‹

### For Description
> Note :
>> For details, have a look and read at sample-configuration.py, we have provided descriptions on each of the configuration.

### Get Telehon String ›_

```sh
# clone repository
git clone https://github.com/unknownkz/universe

# change directory
cd universe/universe/Configuration

# execute program [ to get string sessions ]
python3 -m GenString

# Don't forget to fill your api id, api hash and phone number in configuration.py
# see sample-configuration.py
```

### Example Filling Configuration
<kbd> Create a new file with the name configuration.py </kbd>
<kbd> ( Don't rename file from sample ) </kbd>
```python
### Required for Telegram Api
# get it at my.telegram.org | api development tools | then fill
Api_ID = int(then_get("Api_ID", "182838181")) # <- fill in here " "
Api_Hash = str(then_get("Api_Hash", "57c7822bw02dE")) # <- fill in here " "
# Mobile Phone Number... Don't forget your country code
# this is for your telethon string in local data, so you don't refill it again
# later you just need a verification code from telegram
MobilePhoneNumber = str(then_get("MobilePhoneNumber", "+621234566")) # <- fill in here

### Logger Information
# add @MissRose_Bot to ur chat and write /id to get ur chat id
Logger_ID = then_get("Logger_ID", "-10083828272") # <- fill here " "
# Go to @BotFather on Telegram, type /newbots | then follow the steps | If finished then take the Bot Token.
Token_Bot = str(then_get("Token_Bot", "173637:H7joKL28483")) # <- fill here " "
```
<kbd> Don't forget to add your bot to the group. </kbd>
