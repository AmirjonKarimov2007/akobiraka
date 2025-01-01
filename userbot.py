import json
from datetime import datetime, timedelta
from telethon import TelegramClient, events,Button
from config import *  # API ma'lumotlarini config fayldan olish
import pytz  # Vaqt zonasini boshqarish uchun
import asyncio
from telethon.tl.functions.messages import DeleteMessagesRequest

# Telegram API ma'lumotlari
api_id = API_ID
api_hash = API_HASH
bot_name = "<b>Evelin</b>"

bot = TelegramClient('bot', api_id, api_hash)

# Uzbekistan Time Zone (UTC+5)
uzbekistan_tz = pytz.timezone('Asia/Tashkent')

@bot.on(events.NewMessage)
async def check_last_message(event):
    if not event.is_private:
        return  
    user_id = event.sender_id
    msg = event.message.message
    msg = msg.title()
    photo_url = "https://wallpapercave.com/wp/wp5577825.jpg" 
    user = await bot.get_entity(user_id)
    first_name = user.first_name or "Foydalanuvchi"  

    caption = f"""⚡️Assalomu Aleykum,men <b>Akobir O'ktamov</b>, sizga qanday yordam bera olaman.


⏰Agarda uzoq vaqt javob bermasam +998889110051 telefon raqamiga qo'ngiroq qiling.

"""

    try:
        messages = await bot.get_messages(user_id, limit=2)
        
        if len(messages) > 1:
            second_last_message = messages[1]
            second_last_message_time = second_last_message.date
            current_time = datetime.now(uzbekistan_tz)
            second_last_message_time_uz = second_last_message_time.astimezone(uzbekistan_tz)
            time_diff = current_time - second_last_message_time_uz
            if time_diff > timedelta(days=5) or msg=="Evelin":
                await bot.send_message(user_id, caption, parse_mode='html')
        else:
            await bot.send_message(user_id, caption, parse_mode='html')
    
    except Exception as e:
        await event.respond(f"Xatolik yuz berdi: {str(e)}")



async def main():
    await bot.start()  
    print('Boti Ishga Tushdi')

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.run_forever()
