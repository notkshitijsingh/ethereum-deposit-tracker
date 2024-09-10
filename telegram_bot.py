import telegram
import asyncio

async def send_telegram_message(id, text):
    bot_token = '7257733503:AAEiWTik1bxViV0HmbgO5Oo4o9xpsSBWOGs'
    chat_id = id
    bot = telegram.Bot(token=bot_token)
    await bot.send_message(chat_id=chat_id, text=text)

def notify_user(id, text):
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(send_telegram_message(id, text))
    finally:
        if not loop.is_closed():
            loop.close()
