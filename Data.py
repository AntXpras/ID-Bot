from idbot import app
from Config import Config
from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = "Hallo {}. \n\nSelamat datang{} \n\nGunakan Bot ini untuk mendapatkan id grup, pengguna, bot, channel and dan id stiker."

    if Config.OWNER_ID != 0:
        if Config.OWNER_NAME:
            START += (
                f"\n\nMy Owner :- [{Config.OWNER_NAME}](tg://user?id={Config.OWNER_ID})"
            )
        else:
            print(
                "Kamu menambahkan OWNER_ID tetapi bukan OWNER_NAME. Kamu perlu mengambil both or neithers"
            )
            print("Keluar dari Bot")
            raise SystemExit
    else:
        START += f"\n\nBot By @Cyntaxrobot 👻"
    START += "\n\nP.S ~ ID kamu adalah`{}`"

    # About Message
    ABOUT = "**Tentang Bot Ini** \n\nIni adalah bot opensource by @cyntaxrobot \n\nSource : [Click Here](https://telegram.me/cyntaxrobot) \n\nFramework : [Pyrogram](docs.pyrogram.org) \n\nLanguage : [Python](www.python.org) \n\nDeveloper : [Mყʂƚҽɾყ Bσყ] [Xpras_id](https://t.me/Xpras_id)"

    if Config.OWNER_ID != 0:
        if Config.OWNER_NAME:
            ABOUT += (
                f"\n\nMy Owner :- [{Config.OWNER_NAME}](tg://user?id={Config.OWNER_ID})"
            )
        else:
            print(
                "You added OWNER_ID but not OWNER_NAME. You need to put both or neither"
            )
            print("Quitting the bot")
            raise SystemExit

    # Help Message
    HELP = "**Help & Features** \n\n1) Kirimkan Semua Pesan Untuk mendapatkan ID. \n2) Forward semua pesan user/bot/channel or anonymous admins to get ID. \n3) Send any sticker to get sticker id. \n4) Use Inline Mode to send your ID in any chat. \n5) Add in group / channel to get ID. \n6) Use /id command: \n- in private: To get ID through username \n- in group/channel: To get ID of that chat. \n\nBy @MysteryBots ♥"

    # Home Button
    home_button = [[InlineKeyboardButton(text="HO⬜ME", callback_data="home")]]

    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("⬜ Cara Menggunakan ⬜", callback_data="help"),
            InlineKeyboardButton("⬜ Tentang Bot ini ⬜", callback_data="about"),
        ],
        
        [InlineKeyboardButton("♥ More Amazing bots ♥", url="https://t.me/cyntaxrobot")],
        [InlineKeyboardButton("🎨 Support Group 🎨", url="https://t.me/Xpras_id")],
    ]
