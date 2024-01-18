import autogen
from autogen.agentchat.contrib.agent_builder import AgentBuilder
from autogen import config_list_from_json

config_path = "OAI_CONFIG_LIST"

config_list = config_list_from_json(
    env_or_file="OAI_CONFIG_LIST", 
    filter_dict={
        "model": [
            "gpt-4-1106-preview",
        ]
    }
)

cache_seed = None  # Use an int to seed the response cache. Use None to disable caching.

default_llm_config = {
    "config_list": config_list, 
    "temperature": 0,
    "cache_seed": cache_seed
}

# builder = AgentBuilder(config_path=config_path, builder_model="gpt-4-1106-preview", agent_model="gpt-4-1106-preview")
builder = AgentBuilder(config_file_or_env=config_path, builder_model="gpt-4-1106-preview", agent_model="gpt-4-1106-preview")

building_task = """Find open source weather data, and use it to make predictions. 
For example, find a recent forecast on open-meteo and predict the next day's forecast."""

#The following line does not use OAI assistants.  Comment out the following line to use OAI assistants below.
agent_list, agent_configs = builder.build(building_task, default_llm_config, coding=True)

#Uncomment the following line to use the OAI assistant to help you build the agent.
#agent_list, agent_configs = builder.build(building_task, default_llm_config, coding=True, use_oai_assistant=True)

execution_task = """Find a recent forecast on open-meteo and predict the next day's forecast."""

group_chat = autogen.GroupChat(agents=agent_list, messages=[], max_round=12)
manager = autogen.GroupChatManager(groupchat=group_chat, llm_config=default_llm_config)
agent_list[0].initiate_chat(manager, message=execution_task)

#Uncomment the following line to save the agent configs to a specified file
#builder.save("my_saved_configs.json")

#Uncomment the following line to load the agent configs from a specified file
#builder.load("my_saved_configs.json")