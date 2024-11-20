import telebot
import os
from dotenv import load_dotenv, find_dotenv
import messages
import datab
from pprint import pprint

load_dotenv(find_dotenv())
datab.init_db()

bot = telebot.TeleBot(os.getenv("TELEGRAM_BOT_TOKEN"))

@bot.message_handler()
def start(message):
    messages.log(message)
    response = messages.to_llm(message)
    bot.send_message(message.chat.id, response)
        

bot.infinity_polling(20, True)

