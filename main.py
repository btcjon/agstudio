from autogen import config_list_from_json, AgentBuilder, GroupChat, GroupChatManager

# Setup `config_list`
config_list = config_list_from_json("OAI_CONFIG_LIST")

# Define agent configurations
agent_configs = [
    {
        "name": "Data_scientist",
        "model": "gpt-4-1106-preview",
        "system_message": "As a Data Scientist, you are tasked with automating the retrieval and analysis of academic papers from arXiv. Utilize your Python programming acumen to develop scripts for gathering necessary information such as searching for relevant papers, downloading them, and processing their contents. Apply your analytical and language skills to interpret the data and deduce the applications of the research within specific domains."
    },
    # Add more agent configurations as needed
]

# Build agents
builder = AgentBuilder(agent_configs=agent_configs)
agent_list = builder.build()

# Execute the task
def start_task(execution_task: str, agent_list: list, llm_config: dict):
    group_chat = GroupChat(agents=agent_list, messages=[], max_round=12)
    manager = GroupChatManager(
        groupchat=group_chat, llm_config={"config_list": config_list, **llm_config}
    )
    agent_list[0].initiate_chat(manager, message=execution_task)
