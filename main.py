from autogen import AssistantAgent, UserProxyAgent, config_list_from_json
from dotenv import load_dotenv
import os

load_dotenv()

config_list = config_list_from_json("/path/to/your/oai_config_list.json")

# Create an AssistantAgent instance
assistant = AssistantAgent(
    name="assistant",
    llm_config={"config_list": config_list}
)

# Create a UserProxyAgent instance
user_proxy = UserProxyAgent(
    name="user_proxy",
    code_execution_config={"work_dir": "coding"}
)

# Initiate a chat between the user_proxy and the assistant
user_proxy.initiate_chat(
    assistant,
    message="Plot a chart of NVDA and TESLA stock price change YTD."
)
