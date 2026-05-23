import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_ID = 123456789   #الايدي من موقع my telegram 
API_HASH = "اكتب الهاش اي دي حقك" #من موقع my teledram
BOT_TOKEN = "اكتب التوكن حق البوت" 
app = Client("restricted_downloader", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start(client, message):
    welcome_text = (
        "👋 أهلاً بك في بوت كسر قيود المحتوى!\n\n"
        "🚀 أرسل لي رابط أي منشور من قناة مقيدة أو خاصة\n"
        "وسأقوم بسحب المحتوى وإرساله لك هنا فوراً وبدون قيود."
    )
    await message.reply(
        welcome_text, 
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("دعم المطور 👨‍💻", url="https://t.me/qorsantaez73")]
        ])
    )

@app.on_message(filters.text & filters.regex(r"t.me/"))
async def download_restricted(client, message):
    url = message.text
    status_msg = await message.reply("🔍 جاري تحليل الرابط واستخراج المحتوى... انتظر قليلاً 😊")

    try:
        parts = url.split('/')
        if 'c/' in url: 
            chat_id = int("-100" + parts[-2])
            msg_id = int(parts[-1])
        else: 
            chat_id = parts[-2]
            msg_id = int(parts[-1])

        restricted_msg = await app.get_messages(chat_id, msg_id)

        await status_msg.edit("✅ تم العثور على المحتوى! جاري التحميل والإرسال الآن... ⚡")

        if restricted_msg.text:
            await message.reply_text(f"📄 **المحتوى النصي:**\n\n{restricted_msg.text}")
        
        if restricted_msg.photo:
            await message.reply_photo(restricted_msg.photo.file_id, caption=restricted_msg.caption)
            
        if restricted_msg.video:
            await message.reply_video(restricted_msg.video.file_id, caption=restricted_msg.caption)
            
        if restricted_msg.document:
            await message.reply_document(restricted_msg.document.file_id, caption=restricted_msg.caption)

        await status_msg.delete()

    except Exception as e:
        await status_msg.edit(f"❌ تاكد انك موجود في نفس القناة او المجموعة الذي اعطيتني الرابط حقها.\n\n`Error: {str(e)}`")

print("🚀 telehacker Bot is running... Happy Hacking! 😊")
app.run()
