import os
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
import datab

load_dotenv(find_dotenv())
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE"),
)

def log(message):
    print(f"{message.from_user.username} {message.from_user.id}:\t {message.text}")
    datab.save_message(message.from_user.id, 
                       message.from_user.username,
                       message.text, 
                       message.date
                       )

def to_llm(message):
    pre_msgs = datab.get_user_messages(message.chat.id)
    
    pre_msgs = [("human", msg[0]) for msg in pre_msgs]
    pre_msgs.insert(0, ("system", "Ты филофос-помощник. Ты отвечаешь на вопросы людей по-филосовски."))
    response = llm.generate(pre_msgs).llm_output
    return response
    

