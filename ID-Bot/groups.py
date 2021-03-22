from pyrogram import Client, filters


# Groups Welcome
@Client.on_message(filters.new_chat_members)
async def welcome(idbot, msg):
    bot_id = (await idbot.get_me())["id"]
    if msg.new_chat_members[0].id == bot_id:
        await msg.reply(
            f"➡Terimakasih sudah menambahkan saya kedalam grup! \n\n➡Grup ID is `{msg.chat.id}`"
        )
    else:
        pass
