# (c) @PredatorHackerzZ || @TeleRoidGroup

import os


class Config(object):
	API_ID = 15682957
	API_HASH = "00b8b3714cee0ba2941091b7cc5578e7"
	BOT_TOKEN = "6518993985:AAGmkv68eEUw95DQ3kKN27PYVJhUnHPbtnw"
	BOT_USERNAME = "FileStoreProV3_bot"
	DB_CHANNEL = -1001542849832
	BOT_OWNER = 1098983599
	DATABASE_URL = "mongodb+srv://Tarunteja001:Tarunteja001@cluster0.yqe5n.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
	LOG_CHANNEL = -1001542849832
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", False))
	SHORTLINK_URL = environ.get('SHORTLINK_URL', 'shorturllink.in')
	SHORTLINK_API = environ.get('SHORTLINK_API', '4b4ee55w6qdn9932941d55wd4597b62')
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
 I'm [File Store V3 Bot](http://t.me/FileStoreProV3_bot)

🌠 Send Me Any Video (or) File , Then I'll Save It To My Database And I'll Give Shareable Link To You....

🌌 I Will Work In Channel Too, So Add Me To A Channel With Full Admin Rights And Check My Power...

🌉 I Can Give Direct Shareable Link And Batch Shareable Link Too...

 **My Master** Will Be Broadcasting Movies Here Often , So Make Sure You Don't Block Me And Keep SupportinG Me 🥳

"""
	ABOUT_DEV_TEXT = f"""
	☑️ BOT NAME : [FILE STORE PRO BOT](@FileStoreProV2_bot)
	🏂 OWNER : [HERE](@Nopedude123)
	📣 BACKUP CHANNEL : [Only Fans](@Only_Premium_69)
"""
	HOME_TEXT = """
Hi There 🤗, [{}](tg://user?id={})

🌟 I'm **File Store Pro Bot**

💫 Maintained By [My Master](t.me/Nopedude123)

🌻 Check Out **Help** And **About** For More Information..
"""
