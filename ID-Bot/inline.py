from pyrogram import Client
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent


# Inline Mode
@Client.on_inline_query()
async def answer(idbot, inline_query):
	await inline_query.answer(
		results=[
			InlineQueryResultArticle(
				title=f"✳ID Telegram Kamu{inline_query.from_user.id}",
				input_message_content=InputTextMessageContent(
					f"✳ID Telegram saya`{inline_query.from_user.id}`"
				),
				description="✳Kirimkan Pesan Untuk Mendapatkan ID✳",
				thumb_url="https://telegra.ph/file/06234a45459a8befc04af.png",
			)
		],
		cache_time=1,
	)
