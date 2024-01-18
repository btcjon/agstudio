Referenceagentchatagentchat.contribmultimodal_conversable_agent On this page

## Agentchat.Contrib.Multimodal_Conversable_Agent Multimodalconversableagent Objects

class MultimodalConversableAgent(ConversableAgent)
__init__
def __init__(name: str, system_message: Optional[Union[str, List]] = DEFAULT_LMM_SYS_MSG, is_termination_msg: str = None, *args, **kwargs)

## Arguments:

name str - agent name.

system_message str - system message for the OpenAIWrapper inference. Please override this attribute if you want to reprogram the agent.

**kwargs *dict* - Please refer to other kwargs in ConversableAgent.

update_system_message def update_system_message(system_message: Union[Dict, List, str])
Update the system message.

## Arguments:

system_message str - system message for the OpenAIWrapper inference.

Edit this page Previous « math_user_proxy_agent Next qdrant_retrieve_user_proxy_agent »
Community Discord