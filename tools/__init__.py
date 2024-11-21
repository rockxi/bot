import datab
import os 
import telebot
from langchain.agents import Tool
from dotenv import load_dotenv, find_dotenv
from langchain.prompts import ChatPromptTemplate
load_dotenv(find_dotenv())


template = ChatPromptTemplate.from_template(
    "Отвечайте на следующие вопросы как можно лучше. У вас есть доступ к следующим инструментам: {tools} "
    "{tools}"
    "Используйте следующий формат: "
    "Question: вопрос, на который нужно ответить "
    "Thought: вы всегда должны думать, что делать "
    "Action: действие, которое нужно выполнить, должно быть одним из [{tool_names}] "
    "Action Input: ввод для действия "
    "Observation: результат действия "
    "... (эта Thought/Action/Action Input/Observation могут повторяться N раз) "
    "Thought: Теперь я знаю окончательный ответ "
    "Final Answer: окончательный ответ на первоначальный вопрос "
    "Начнем! "
    "Question: {input} "
    "Thought: {agent_scratchpad}"
)


def matuki(message):
    print("\n обнаружена нецензурная лексика (шутки про мамаш)")
    bot = telebot.TeleBot(os.getenv("TELEGRAM_BOT_TOKEN"))
    admin_id = os.getenv("ADMIN_CHAT_ID") 

    bot.send_message(admin_id, f"{message}")

def message_count(user_id):
    print("\n обнаружено сообщение о количестве сообщений пользователя")
    return datab.message_count(user_id)

message_count_tool = Tool(
    name="message_count",
    func = message_count,
    description= \
        """Инструмент для подсчёта количества сообщений пользователя.
        срабатывает если пользователь спрашивает о количестве сообщений пользователя.
        При этом, НЕ СРАБАТЫВАЕТ, если вопрос о количестве находится в chat_history. Только в input! 
        Ввод: числовой идентификатор пользователя (user_id). 
        Вывод: количество сообщений, отправленных данным пользователем."""
)
matuki_tool = Tool(
    name="matuki",
    func = matuki,
    description= \
        """Инструмент для определения наличия матерных выражений в запросе пользователя.
        срабатывает если в тексте пользователя есть матерные выражения.
        Ввод: id пользователя (user_id) и текст запроса пользователя.
        Вывод: повещение администрации о том, что пользователь ругается матом""" 
)
conv_tool = Tool(
    name="conv_tool",
    func = lambda x : None, 
    description= \
        """ОТВЕЧАЙ КАК ФИЛОСОВ ЕСЛИ ПОЛЬЗОВАТЕЛЬ НЕ СПРАШИВАЕТ ТЕБЯ ВЫПОЛНИТЬ КАКОЕ-ТО ДЕЙСТВИЕ
        Ввод: ввода нет, только запрос пользователя.
        Вывод: ответ на запрос пользователя в филосовском стиле (придумай сам)"""
)
all_tools = [message_count_tool, matuki_tool, conv_tool]