Referenceagent_utils On this page

## Agent_Utils Gather_Usage_Summary Def Gather_Usage_Summary( Agents: List[Agent]) -> Tuple[Dict[Str, Any], Dict[Str, Any]]

Gather usage summary from all agents.

## Arguments:

agents - (list): List of agents.

## Returns:

tuple - (total_usage_summary, actual_usage_summary)
Example return: total_usage_summary = {
'total_cost' - 0.0006090000000000001, 'gpt-35-turbo': { 'cost' - 0.0006090000000000001,
'prompt_tokens' - 242, 'completion_tokens' - 123, 'total_tokens' - 365 } } actual_usage_summary follows the same format. If none of the agents incurred any cost (not having a client), then the total_usage_summary and actual_usage_summary will be {'total_cost': 0}.

Edit this page Previous « openai_utils Next code_utils »
Community Discord