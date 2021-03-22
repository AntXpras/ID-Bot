from pyrogram import Client, filters


# Sticker ID
@Client.on_message(
    filters.private
    & ~filters.forwarded
    & ~filters.command(["start", "about", "help", "id"])
)
async def stickers(idbot, msg):
    if msg.sticker:
        await msg.reply(f"✳ID stiker ini`{msg.sticker.file_id}`", quote=True)
    else:
        await msg.reply(f"✳ID telegram kamu: `{msg.from_user.id}`")
