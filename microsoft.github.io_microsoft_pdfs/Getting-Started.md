AutoGen Search Getting Started On this page

## Getting Started

AutoGen is a framework that enables development of LLM applications using multiple agents that can converse with each other to solve tasks. AutoGen agents are customizable, conversable, and seamlessly allow human participation. They can operate in various modes that employ combinations of LLMs, human inputs, and tools.

## Main Features

AutoGen enables building next-gen LLM applications based on multi-agent conversations with minimal effort. It simplifies the orchestration, automation, and optimization of a complex LLM workflow. It maximizes the performance of LLM models and overcomes their weaknesses. It supports diverse conversation patterns for complex workflows. With customizable and conversable agents, developers can use AutoGen to build a wide range of conversation patterns concerning conversation autonomy, the number of agents, and agent conversation topology. It provides a collection of working systems with different complexities. These systems span a wide range of applications from various domains and complexities. This demonstrates how AutoGen can easily support diverse conversation patterns. AutoGen provides enhanced LLM inference. It offers utilities like API unification and caching, and advanced usage patterns, such as error handling, multi-config inference, context programming, etc.

AutoGen is powered by collaborative research studies from Microsoft, Penn State University, and University of Washington.

## Quickstart

Install from pip: pip install pyautogen. Find more options in Installation. For code execution, we strongly recommend installing the python docker package, and using docker.

## Multi-Agent Conversation Framework

Autogen enables the next-gen LLM applications with a generic multi-agent conversation framework. It offers customizable and conversable agents which integrate LLMs, tools, and humans. By automating chat among multiple capable agents, one can easily make them collectively perform tasks autonomously or with human feedback, including tasks that require using tools via code. For example,
# Load LLM inference endpoints from an env variable or a file
# See https://microsoft.github.io/autogen/docs/FAQ#set-your-api-endpoints
# and OAI_CONFIG_LIST_sample.json config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST") assistant = AssistantAgent("assistant", llm_config={"config_list": config_list}) user_proxy = UserProxyAgent("user_proxy", code_execution_config={"work_dir": "coding"}) user_proxy.initiate_chat(assistant, message="Plot a chart of NVDA and TESLA stock price change YTD.") # This initiates an automated chat between the two agents to solve the task The figure below shows an example conversation flow with AutoGen. 

Code examples. Documentation.

## Enhanced Llm Inferences

Autogen also helps maximize the utility out of the expensive LLMs such as ChatGPT and GPT-4. It offers enhanced LLM inference with powerful functionalities like tuning, caching, error handling, templating. For example, you can optimize generations by LLM with your own tuning data, success metrics and budgets.

# perform tuning for openai<1 config, analysis = autogen.Completion.tune( data=tune_data, metric="success", mode="max", eval_func=eval_func, inference_budget=0.05, optimization_budget=3, num_samples=-1, ) # perform inference for a test instance response = autogen.Completion.create(context=test_instance, **config)
Code examples. Documentation.

## Where To Go Next ?

Understand the use cases for multi-agent conversation and enhanced LLM inference.
Find code examples.
Read SDK.
Learn about research around AutoGen.
Roadmap
Chat on Discord.
Follow on Twitter.

If you like our project, please give it a star on GitHub. If you are interested in contributing, please read Contributor's Guide.

Edit this page Next Installation »
Community Discord Copyright © 2024 AutoGen Authors | Privacy and Cookies