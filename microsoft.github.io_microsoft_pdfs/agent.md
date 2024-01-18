AutoGen Search Referenceagentchatagent On this page

## Agentchat.Agent Agent Objects Class Agent()

(In preview) An abstract class for AI agent.

An agent can communicate with other agents and perform actions. Different agents can differ in what actions they perform in the receive method.

## __Init__ Def __Init__(Name: Str) Arguments:

name str - name of the agent.

## Name

@property def name()
Get the name of the agent.

## Send

def send(message: Union[Dict, str], recipient: "Agent", request_reply: Optional[bool] = None)
(Abstract method) Send a message to another agent.

## A_Send

async def a_send(message: Union[Dict, str], recipient: "Agent", request_reply: Optional[bool] = None)
(Abstract async method) Send a message to another agent.

## Receive

def receive(message: Union[Dict, str], sender: "Agent", request_reply: Optional[bool] = None)
(Abstract method) Receive a message from another agent.

## A_Receive

async def a_receive(message: Union[Dict, str], sender: "Agent", request_reply: Optional[bool] = None)
(Abstract async method) Receive a message from another agent.

## Def Reset()

(Abstract method) Reset the agent.

## Generate_Reply Def Generate_Reply(Messages: Optional[List[Dict]] = None, Sender: Optional["Agent"] = None, **Kwargs) -> Union[Str, Dict, None]

(Abstract method) Generate a reply based on the received messages.

## Arguments:

messages *list[dict]* - a list of messages received.

sender - sender of an Agent instance.

## Returns:

str or dict or None: the generated reply. If None, no reply is generated.

## A_Generate_Reply Async Def A_Generate_Reply(Messages: Optional[List[Dict]] = None, Sender: Optional["Agent"] = None, **Kwargs) -> Union[Str, Dict, None]

(Abstract async method) Generate a reply based on the received messages.

## Arguments:

messages *list[dict]* - a list of messages received. sender - sender of an Agent instance.

## Returns:

str or dict or None: the generated reply. If None, no reply is generated.

Edit this page Previous « text_analyzer_agent Next assistant_agent »
Community Discord Twitter Copyright © 2024 AutoGen Authors | Privacy and Cookies