Referenceagentchatagentchat.contribllava_agent On this page

## Agentchat.Contrib.Llava_Agent Llavaagent Objects

class LLaVAAgent(MultimodalConversableAgent)
__init__
def __init__(name: str, system_message: Optional[Tuple[str, List]] = DEFAULT_LLAVA_SYS_MSG, *args, **kwargs)

## Arguments:

name str - agent name.

system_message str - system message for the ChatCompletion inference. Please override this attribute if you want to reprogram the agent.

**kwargs *dict* - Please refer to other kwargs in ConversableAgent.

## Llava_Call Def Llava_Call(Prompt: Str, Llm_Config: Dict) -> Str

Makes a call to the LLaVA service to generate text based on a given prompt Edit this page Previous « img_utils Next math_user_proxy_agent »
Community Discord