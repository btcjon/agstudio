Referenceagentchatassistant_agent On this page

## Agentchat.Assistant_Agent Assistantagent Objects Class Assistantagent(Conversableagent)

(In preview) Assistant agent, designed to solve a task with LLM. AssistantAgent is a subclass of ConversableAgent configured with a default system message. The default system message is designed to solve a task with LLM, including suggesting python code blocks and debugging. human_input_mode is default to "NEVER" and code_execution_config is default to False. This agent doesn't execute code by default, and expects the user to execute the code.

## __Init__

def __init__(name: str, system_message: Optional[str] = DEFAULT_SYSTEM_MESSAGE, llm_config: Optional[Union[Dict, Literal[False]]] = None, is_termination_msg: Optional[Callable[[Dict], bool]] = None, max_consecutive_auto_reply: Optional[int] = None, human_input_mode: Optional[str] = "NEVER", code_execution_config: Optional[Union[Dict, Literal[False]]] = False, description: Optional[str] = None, **kwargs)

## Arguments:

name str - agent name. system_message str - system message for the ChatCompletion inference. Please override this attribute if you want to reprogram the agent.

llm_config *dict* - llm inference configuration. Please refer to OpenAIWrapper.create for available options. is_termination_msg *function* - a function that takes a message in the form of a dictionary and returns a boolean value indicating if this received message is a termination message. The dict can contain the following keys: "content", "role", "name", "function_call".

max_consecutive_auto_reply int - the maximum number of consecutive auto replies. default to None (no limit provided, class attribute MAX_CONSECUTIVE_AUTO_REPLY will be used as the limit in this case). The limit only plays a role when human_input_mode is not "ALWAYS".

**kwargs *dict* - Please refer to other kwargs in ConversableAgent.

Edit this page Previous « agent Community Discord Next conversable_agent »