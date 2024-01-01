'''
from replit.ai.modelfarm import ChatExample, ChatMessage, ChatModel, ChatSession


def vertex_chat(prompt):
  model = ChatModel("chat-bison")
  response = model.chat([
    ChatSession(
      context="You are philosophy bot.",
      examples=[
        ChatExample(
          input=ChatMessage(content="1 + 1"),
          output=ChatMessage(content="2")
        )
      ],
      messages=[
        ChatMessage(author="USER", content=prompt),
      ],
    )
  ], temperature=0.2)
  
  return response.responses[0].candidates[0].message.content

print(vertex_chat("What is the capital of France?"))

import os
from autogen import get_config_list
from autogen.agentchat.contrib.gpt_assistant_agent import GPTAssistantAgent
from autogen import UserProxyAgent


api_key = os.environ['OPENAI_API_KEY']

config_list = get_config_list(
    [api_key]
)

# creates new assistant using Assistant API
gpt_assistant = GPTAssistantAgent(
    name="assistant",
    llm_config={
        "config_list": config_list,
        "assistant_id": None
    })

user_proxy = UserProxyAgent(name="user_proxy",
    code_execution_config={
        "work_dir": "coding"
    },
    human_input_mode="NEVER")

user_proxy.initiate_chat(gpt_assistant, message="Print hello world")
'''

import asyncio
from metagpt.roles import (Architect, Engineer, ProductManager, ProjectManager)
from metagpt.team import Team


async def startup(idea: str):
  company = Team()
  company.hire([
      ProductManager(),
      Architect(),
      ProjectManager(),
      Engineer(),
  ])
  company.invest(investment=3.0)
  company.run_project(idea=idea)
  await company.run(n_round=5)


async def main():
  history = await startup(
      idea=
      "create a single page website to display live data from a google sheet")
  print(history)


# Run the main function using asyncio.run() if the script is the main program
if __name__ == "__main__":
  asyncio.run(main())
'''
import asyncio

from metagpt.roles.researcher import Researcher
from metagpt.logs import logger


async def main():
  msg = "Research about trending skills in the job market"
  role = Researcher()
  result = await role.run(msg)
  logger.info(result.content[:100])


if __name__ == '__main__':
  asyncio.run(main())
'''
