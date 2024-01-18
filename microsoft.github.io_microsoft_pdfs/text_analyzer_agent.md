Referenceagentchatagentchat.contribtext_analyzer_agent On this page

## Agentchat.Contrib.Text_Analyzer_Agent Textanalyzeragent Objects Class Textanalyzeragent(Conversableagent)

(Experimental) Text Analysis agent, a subclass of ConversableAgent designed to analyze text as instructed.

## __Init__

def __init__(name="analyzer", system_message: Optional[str] = system_message, human_input_mode: Optional[str] = "NEVER", llm_config: Optional[Union[Dict, bool]] = None, **kwargs)

## Arguments:

name str - name of the agent. system_message str - system message for the ChatCompletion inference. human_input_mode str - This agent should NEVER prompt the human for input. llm_config *dict or False* - llm inference configuration. Please refer to OpenAIWrapper.create for available options. To disable llmbased auto reply, set to False.

**kwargs *dict* - other kwargs in ConversableAgent.

## Analyze_Text Def Analyze_Text(Text_To_Analyze, Analysis_Instructions)

Analyzes the given text as instructed, and returns the analysis.

Edit this page Previous « retrieve_user_proxy_agent Next agent »
Community Discord