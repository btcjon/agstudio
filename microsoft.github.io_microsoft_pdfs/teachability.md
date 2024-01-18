
## Autogen

Search Referenceagentchatagentchat.contribagentchat.contrib.capabilitiesteachability On this page

## Agentchat.Contrib.Capabilities.Teachability Teachability Objects Class Teachability(Agentcapability)

Teachability uses a vector database to give an agent the ability to remember user teachings, where the user is any caller (human or not) sending messages to the teachable agent. Teachability is designed to be composable with other agent capabilities. To make any conversable agent teachable, instantiate both the agent and the Teachability class, then pass the agent to teachability.add_to_agent(agent). Note that teachable agents in a group chat must be given unique path_to_db_dir values.

## __Init__

def __init__(verbosity: Optional[int] = 0, reset_db: Optional[bool] = False, path_to_db_dir: Optional[str] = "./tmp/teachable_agent_db", recall_threshold: Optional[float] = 1.5, max_num_retrievals: Optional[int] = 10, llm_config: Optional[Union[Dict, bool]] = None)

## Arguments:

verbosity *Optional, int* - # 0 (default) for basic info, 1 to add memory operations, 2 for analyzer messages, 3 for memo lists.

reset_db *Optional, bool* - True to clear the DB before starting. Default False. path_to_db_dir *Optional, str* - path to the directory where this particular agent's DB is stored. Default "./tmp/teachable_agent_db" recall_threshold *Optional, float* - The maximum distance for retrieved memos, where 0.0 is exact match. Default 1.5. Larger values allow more (but less relevant) memos to be recalled.

max_num_retrievals *Optional, int* - The maximum number of memos to retrieve from the DB. Default 10. llm_config *dict or False* - llm inference configuration passed to TextAnalyzerAgent. If None, TextAnalyzerAgent uses llm_config from the teachable agent.

## Add_To_Agent Def Add_To_Agent(Agent: Conversableagent)

Adds teachability to the given agent.

## Prepopulate_Db Def Prepopulate_Db()

Adds a few arbitrary memos to the DB.

## Process_Last_Message Def Process_Last_Message(Text)

Appends any relevant memos to the message text, and stores any apparent teachings in new memos. Uses TextAnalyzerAgent to make decisions about memo storage and retrieval.

## Memostore Objects Class Memostore()

Provides memory storage and retrieval for a teachable agent, using a vector database. Each DB entry (called a memo) is a pair of strings: an input text and an output text. The input text might be a question, or a task to perform. The output text might be an answer to the question, or advice on how to perform the task. Vector embeddings are currently supplied by Chroma's default Sentence Transformers.

## Def (Verbosity, Reset, Path_To_Db_Dir)

Arguments:
verbosity (Optional, int): 1 to print memory operations, 0 to omit them. 3+ to print memo lists. path_to_db_dir (Optional, str): path to the directory where the DB is stored.

## List_Memos Def List_Memos()

Prints the contents of MemoStore. reset_db

## Def Reset_Db()

Forces immediate deletion of the DB's contents, in memory and on disk.

## Add_Input_Output_Pair Def Add_Input_Output_Pair(Input_Text, Output_Text)

Adds an input-output pair to the vector DB.

## Get_Nearest_Memo Def Get_Nearest_Memo(Query_Text)

Retrieves the nearest memo to the given query text. get_related_memos

## Def Get_Related_Memos(Query_Text, N_Results, Threshold)

Retrieves memos that are related to the given query text within the specified distance threshold.

## Prepopulate Def Prepopulate()

Adds a few arbitrary examples to the vector DB, just to make retrieval less trivial.

Edit this page Previous « agent_capability Next agent_builder »
Community Discord Twitter