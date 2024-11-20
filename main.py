import telebot
import os
from dotenv import load_dotenv

import messages
import datab

load_dotenv()
datab.init_db()

bot = telebot.TeleBot(os.getenv("TELEGRAM_BOT_TOKEN"))

@bot.message_handler()
def start(message):
    messages.log(message)
    responce = messages.to_llm(message)
    bot.send_message(message.chat.id, responce)
        

bot.infinity_polling(20, True)

