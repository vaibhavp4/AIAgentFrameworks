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

'''

from autogen import AssistantAgent, UserProxyAgent, config_list_from_json
import os

# Load LLM inference endpoints from an env variable or a file
# See https://microsoft.github.io/autogen/docs/FAQ#set-your-api-endpoints
# and OAI_CONFIG_LIST_sample.json
config_list = config_list_from_json(env_or_file=os.environ["OAI_CONFIG_LIST"])
assistant = AssistantAgent("assistant", llm_config={"config_list": config_list})
user_proxy = UserProxyAgent("user_proxy", code_execution_config={"work_dir": "coding"})
user_proxy.initiate_chat(assistant, message="Plot a chart of NVDA and TESLA stock price change YTD.")