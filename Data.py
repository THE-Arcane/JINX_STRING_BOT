from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

🥀ᴡᴇʟᴄᴏᴍᴇ to {}
Bot..! 💫 ᴀ ᴘʏʀᴏɢʀᴀᴍ ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ sᴛʀɪɴɢ ɢᴇɴ ʙᴏᴛ.
[➩](https://telegra.ph/file/9f633a7e5cfa5c91d2b9c.jpg) ᴄʟɪᴄᴋ ᴏɴ ɢᴇɴʀᴀᴛᴇ sᴛʀɪɴɢ ғᴏʀ ɢᴇɴᴇʀᴀᴛ ʏᴏᴜʀ sᴛʀɪɴɢ sᴇssɪᴏɴ..!✨

ᴊɪɴx sᴛʀɪɴɢ ɢᴇɴ ʙᴏᴛ ʙʏ ᴛᴇᴀᴍ ᴀʀᴄᴀɴᴇ
❖ ─ ✦ ─ 🖤 ─ ✦

✗ Pᴏᴡᴇʀᴇᴅ 🔥 Bʏ: [ᴀʀᴄᴀɴᴇ!](https://t.me/Arcane_bots)
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
🥀 **𝐴𝑣𝑎𝑖𝑙𝑎𝑏𝑙𝑒 𝐶𝑜𝑚𝑚𝑎𝑛𝑑𝑠** 🔥

/about - 𝑨𝒃𝒐𝒖𝒕 𝑻𝒉𝒆 𝑩𝒐𝒕
/help - 𝑻𝒉𝒊𝒔 𝑴𝒆𝒔𝒔𝒂𝒈𝒆
/start - 𝑺𝒕𝒂𝒓𝒕 𝒕𝒉𝒆 𝑩𝒐𝒕
/generate - 𝑺𝒕𝒂𝒓𝒕 𝑮𝒆𝒏𝒆𝒓𝒂𝒕𝒊𝒏𝒈 𝑺𝒆𝒔𝒔𝒊𝒐𝒏
/cancel - 𝑪𝒂𝒏𝒄𝒆𝒍 𝒕𝒉𝒆 𝒑𝒓𝒐𝒄𝒆𝒔𝒔
/restart - 𝑪𝒂𝒏𝒄𝒆𝒍 𝒕𝒉𝒆 𝒑𝒓𝒐𝒄𝒆𝒔𝒔
"""

    # About Message
    ABOUT = """
**About This Bot** 

A ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴘʏʀᴏɢʀᴀᴍ ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ sᴛʀɪɴɢ sᴇssɪᴏɴ ʙʏ @Arcane_bots

Source Code : [👉🏻](https://telegra.ph/file/fb9884eb2fd19afad29d6.mp4)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @II_ZEUS_XD_II ✨🥀
    """
