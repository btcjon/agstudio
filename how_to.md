# How to Use AutoGen

AutoGen is a powerful framework that enables the development of applications using Large Language Models (LLMs) through a multi-agent conversation framework. Here's a quick guide on how to get started:

## Setting Up Your Configuration

1. Update your `oai_config_list.json` with the correct API key and model configuration.
2. Ensure that the `model` is set to `gpt-4-1106-preview` for the latest GPT-4 model with a 128k context window.

## Creating Agents

Use the `AssistantAgent` and `UserProxyAgent` classes to create agents that can perform tasks and interact with users.

```python
from autogen import AssistantAgent, UserProxyAgent, config_list_from_json

config_list = config_list_from_json("path/to/oai_config_list.json")
assistant = AssistantAgent(name="assistant", llm_config={"config_list": config_list})
user_proxy = UserProxyAgent(name="user_proxy", code_execution_config={"work_dir": "coding"})
```

## Initiating a Conversation

Start a conversation between agents to solve tasks autonomously or with human feedback.

```python
user_proxy.initiate_chat(assistant, message="Your task description here.")
```

## Advanced Usage

Explore advanced features such as error handling, context programming, and more to enhance the capabilities of your agents.

For more detailed information, refer to the official AutoGen documentation and examples.
