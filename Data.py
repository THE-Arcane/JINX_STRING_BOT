from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

๐ฅแดกแดสแดแดแดแด to {}
Bot..! ๐ซ แด แดสสแดษขสแดแด แดษดแด แดแดสแดแดสแดษด sแดสษชษดษข ษขแดษด สแดแด.
[โฉ](https://telegra.ph/file/9f633a7e5cfa5c91d2b9c.jpg) แดสษชแดแด แดษด ษขแดษดสแดแดแด sแดสษชษดษข าแดส ษขแดษดแดสแดแด สแดแดส sแดสษชษดษข sแดssษชแดษด..!โจ

แดษชษดx sแดสษชษดษข ษขแดษด สแดแด สส แดแดแดแด แดสแดแดษดแด
โ โ โฆ โ ๐ค โ โฆ

โ Pแดแดกแดสแดแด ๐ฅ Bส: [แดสแดแดษดแด!](https://t.me/Arcane_bots)
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("๐ฅ ๐บ๐ป๐จ๐น๐ป ๐ฎ๐ฌ๐ต๐น๐จ๐ป๐ฐ๐ต๐ฎ ๐บ๐ฌ๐บ๐บ๐ฐ๐ถ๐ต ๐ฅ", callback_data="generate")],
    ]

    generate_button = [
        [InlineKeyboardButton("๐ฅ ๐บ๐ป๐จ๐น๐ป ๐ฎ๐ฌ๐ต๐น๐จ๐ป๐ฐ๐ต๐ฎ ๐บ๐ฌ๐บ๐บ๐ฐ๐ถ๐ต ๐ฅ", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("ใ  ๐บ๐ป๐จ๐น๐ป ๐ฎ๐ฌ๐ต๐น๐จ๐ป๐ฐ๐ต๐ฎ ๐บ๐ฌ๐บ๐บ๐ฐ๐ถ๐ต ๐", callback_data="generate")],
        [InlineKeyboardButton("๐ฅ ๐ถ๐ป๐ด๐๐๐ผ๐๐บ ๐บ๐๐๐๐ โจ", url="https://t.me/Arcane_chatting")],
        [
            InlineKeyboardButton("How to Use ๐โ", callback_data="help"),
            InlineKeyboardButton("๐ About ๐", callback_data="about")
        ],
        [InlineKeyboardButton("๐ ๐๐๐๐ ๐๐๐๐ฃ๐๐๐ ๐๐๐๐ ๐", url="https://t.me/Arcane_bots")],
    ]

    # Help Message
    HELP = """
๐ฅ **๐ด๐ฃ๐๐๐๐๐๐๐ ๐ถ๐๐๐๐๐๐๐ ** ๐ฅ

/about - ๐จ๐๐๐๐ ๐ป๐๐ ๐ฉ๐๐
/help - ๐ป๐๐๐ ๐ด๐๐๐๐๐๐
/start - ๐บ๐๐๐๐ ๐๐๐ ๐ฉ๐๐
/generate - ๐บ๐๐๐๐ ๐ฎ๐๐๐๐๐๐๐๐๐ ๐บ๐๐๐๐๐๐
/cancel - ๐ช๐๐๐๐๐ ๐๐๐ ๐๐๐๐๐๐๐
/restart - ๐ช๐๐๐๐๐ ๐๐๐ ๐๐๐๐๐๐๐
"""

    # About Message
    ABOUT = """
**About This Bot** 

A แดแดสแดษขสแดแด สแดแด แดแด ษขแดษดแดสแดแดแด แดสสแดษขสแดแด แดษดแด แดแดสแดแดสแดษด sแดสษชษดษข sแดssษชแดษด สส @Arcane_bots

Source Code : [๐๐ป](https://telegra.ph/file/fb9884eb2fd19afad29d6.mp4)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @II_ZEUS_XD_II โจ๐ฅ
    """
