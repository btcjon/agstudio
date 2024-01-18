Referenceagentchatagentchat.contribagentchat.contrib.capabilitiesagent_capability On this page

## Agentchat.Contrib.Capabilities.Agent_Capability Agentcapability Objects Class Agentcapability()

Base class for composable capabilities that can be added to an agent.

## Add_To_Agent Def Add_To_Agent(Agent: Conversableagent)

Adds a particular capability to the given agent. Must be implemented by the capability subclass. An implementation will typically call agent.register_hook() one or more times. See teachability.py as an example.

Edit this page Next teachability »
Community Discord