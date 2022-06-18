from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

🥀ᴡᴇʟᴄᴏᴍᴇ to {}
Bot..! 💫 ᴀ ᴘʏʀᴏɢʀᴀᴍ ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ sᴛʀɪɴɢ ɢᴇɴ ʙᴏᴛ.
[➼](https://telegra.ph/file/244a1d5f862b0991d13b6.jpg) ᴄʟɪᴄᴋ ᴏɴ ɢᴇɴʀᴀᴛᴇ sᴛʀɪɴɢ ғᴏʀ ɢᴇɴᴇʀᴀᴛ ʏᴏᴜʀ sᴛʀɪɴɢ sᴇssɪᴏɴ..!✨
────────────────────────
ᴊɪɴx sᴛʀɪɴɢ ɢᴇɴ ʙᴏᴛ ʙʏ ᴛᴇᴀᴍ ᴀʀᴄᴀɴᴇ
────────────────────────
Still reading?
You can use me to generate pyrogram and telethon string session. Use below buttons to learn more !

✗ Pᴏᴡᴇʀᴇᴅ 🔥 Bʏ: [ᴀʀᴄᴀɴᴇ!](https://t.me/Team_Arcane)
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🔥 sᴛᴀʀᴛ Generating Session ⚡", callback_data="generate")],
    ]

    generate_button = [
        [InlineKeyboardButton(" sᴛᴀʀᴛ Generating Session ⚡", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("☂️ Start Generating Session ☔", callback_data="generate")],
        [InlineKeyboardButton("🌝 Bot Status and More Bots 💕", url="https://t.me/kigo_omfo")],
        [
            InlineKeyboardButton("How to Use 📖❔", callback_data="help"),
            InlineKeyboardButton("📜 About 👀", callback_data="about")
        ],
        [InlineKeyboardButton("💜 More Amazing bots 💜", url="https://t.me/")],
    ]

    # Help Message
    HELP = """
🥀 **Available Commands** 🔥

/about - About The Bot
/help - This Message
/start - Start the Bot
/generate - Start Generating Session
/cancel - Cancel the process
/restart - Cancel the process
"""

    # About Message
    ABOUT = """
**About This Bot** 

A telegram bot to Manage group and generate pyrogram and telethon string session by @TeamDeeCode

Source Code : [😙Click Here💫]()

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @II_ZEUS_XD_II ✨🥀
    """
