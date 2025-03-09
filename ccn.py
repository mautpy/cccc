from pyrogram import Client, filters
from pyrogram.types import Message

BOT_TOKEN = "7693245258:AAEiWDvYd7_5Cor2xTB0nHd3fWxE1VLV_kk"
API_ID = 22625636  # Replace with your API ID
API_HASH = "f71778a6e1e102f33ccc4aee3b5cc697"

app = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

CHANNEL_ID = -1002267436984  # Replace with your channel ID

@app.on_message(filters.command("check") & filters.private)
async def check_join(client: Client, message: Message):
    user_id = message.from_user.id
    try:
        member = await client.get_chat_member(CHANNEL_ID, user_id)
        if member.status in ["member", "administrator", "creator"]:
            await message.reply_text("✅ You have joined the channel!")
        else:
            await message.reply_text("❌ You haven't joined the channel.")
    except Exception as e:
        await message.reply_text(f"❌ Error: {e}")

app.run()
