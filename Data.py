from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

🥀ᴡᴇʟᴄᴏᴍᴇ to {}
Bot..! 💫 ᴀ ᴘʏʀᴏɢʀᴀᴍ ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ sᴛʀɪɴɢ ɢᴇɴ ʙᴏᴛ.
[➩](https://telegra.ph/file/9f633a7e5cfa5c91d2b9c.jpg) ᴄʟɪᴄᴋ ᴏɴ ɢᴇɴʀᴀᴛᴇ sᴛʀɪɴɢ ғᴏʀ ɢᴇɴᴇʀᴀᴛ ʏᴏᴜʀ sᴛʀɪɴɢ sᴇssɪᴏɴ..!✨
❖ ── ✦ ──『❤️』── ✦♡ 
ᴊɪɴx sᴛʀɪɴɢ ɢᴇɴ ʙᴏᴛ ʙʏ ᴛᴇᴀᴍ ᴀʀᴄᴀɴᴇ
❖ ── ✦ ──『🖤』── ✦♡
Still reading?
You can use me to generate pyrogram and telethon string session. Use below buttons to learn more !

✗ Pᴏᴡᴇʀᴇᴅ 🔥 Bʏ: [ᴀʀᴄᴀɴᴇ!](https://t.me/Team_Arcane)
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🥀 𝑺𝑻𝑨𝑹𝑻 𝑮𝑬𝑵𝑹𝑨𝑻𝑰𝑵𝑮 𝑺𝑬𝑺𝑺𝑰𝑶𝑵 🥀", callback_data="generate")],
    ]

    generate_button = [
        [InlineKeyboardButton("🥀 𝑺𝑻𝑨𝑹𝑻 𝑮𝑬𝑵𝑹𝑨𝑻𝑰𝑵𝑮 𝑺𝑬𝑺𝑺𝑰𝑶𝑵 🥀", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("㊍  𝑺𝑻𝑨𝑹𝑻 𝑮𝑬𝑵𝑹𝑨𝑻𝑰𝑵𝑮 𝑺𝑬𝑺𝑺𝑰𝑶𝑵 🌙", callback_data="generate")],
        [InlineKeyboardButton("🥀 𝐶𝐻𝐴𝑇𝑇𝐼𝑁𝐺 𝐺𝑅𝑂𝑈𝑃 ✨", url="https://t.me/Arcane_chatting")],
        [
            InlineKeyboardButton("How to Use 📖❔", callback_data="help"),
            InlineKeyboardButton("📜 About 👀", callback_data="about")
        ],
        [InlineKeyboardButton("🀄 𝖒𝖔𝖗𝖊 𝖆𝖒𝖆𝚣𝖎𝖓𝖌 𝖇𝖔𝖙𝖘 💜", url="https://t.me/Arcane_bots")],
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

Source Code : [😙 Click Here 💫]()

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @II_ZEUS_XD_II ✨🥀
    """
