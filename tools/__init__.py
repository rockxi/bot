from langchain.agents import Tool
import datab
import os 
import telebot
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())



def matuki(message):
    print(123)
    bot = telebot.TeleBot(os.getenv("TELEGRAM_BOT_TOKEN"))
    admin_id = os.getenv("ADMIN_CHAT_ID") 

    bot.send_message(admin_id, message)

message_count_tool = Tool(
    name="message_count",
    func = datab.message_count,
    description= \
        """Инструмент для подсчёта количества сообщений пользователя.
        Ввод: числовой идентификатор пользователя (user_id). 
        Вывод: количество сообщений, отправленных данным пользователем."""
)
matuki_tool = Tool(
    name="matuki",
    func = matuki,
    description= \
    """
    Инструмент для определения наличия матерных выражений в запросе пользователя.
    срабатывает если в тексте пользователя есть матерные выражения.
    Ввод: текст запроса пользователя.
    Вывод: оповещение администрации о том, что пользователь ругается матом
    """ 
)
all_tools = [message_count_tool]