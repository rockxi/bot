import telebot
import os
import messages
import datab
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
datab.init_db()

bot = telebot.TeleBot(os.getenv("TELEGRAM_BOT_TOKEN"))

@bot.message_handler()
def start(message):
    messages.log(message)
    response = messages.to_llm(message)
    bot.send_message(message.chat.id, response)
        

bot.infinity_polling(20, True)

