import os
import datab
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
from pprint import pprint

from langchain import hub
from langchain.agents import Tool, create_react_agent, AgentExecutor
from langchain.prompts import *

import tools

load_dotenv(find_dotenv())
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE"),
)


chat_prompt = hub.pull("hwchase17/react-chat")

agent = create_react_agent(
    tools=tools.all_tools,
    llm=llm,
    prompt=chat_prompt,
)

executor = AgentExecutor(agent = agent, tools = tools.all_tools, verbose=True)

def log(message):
    print(f"{message.from_user.username} {message.from_user.id}:\t {message.text}")
    datab.save_message(message.from_user.id, 
                       message.from_user.username,
                       message.text, 
                       message.date
                       )
    
def to_llm(message):
    pre_msgs = datab.get_user_messages(message.chat.id)
    pre_msgs = [(msg[1], msg[0]) for msg in pre_msgs]
    print("\n\n\n"); pprint(pre_msgs); print("\n\n\n")

    response = executor.invoke({
        "input": message.text,
        "chat_history": f"user_id={message.chat.id}" + "\n".join([f"role: {role}, content: {content}" for role, content in pre_msgs[:-1]])
    })

    print("\n\n\n"); pprint(response); print("\n\n\n") 
    response_text = response['output']

    datab.save_llm_message(message.chat.id, message.from_user.username, response_text, message.date)
    return response_text 
    

