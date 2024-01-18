Search Referencetoken_count_utils On this page

## Token_Count_Utils Token_Left Def Token_Left(Input: Union[Str, List, Dict], Model="Gpt-3.5-Turbo-0613") -> Int

Count number of tokens left for an OpenAI model.

## Arguments:

input - (str, list, dict): Input to the model. model - (str): Model name.

## Returns:

int - Number of tokens left that the model can use for completion.

## Count_Token Def Count_Token(Input: Union[Str, List, Dict], Model: Str = "Gpt-3.5-Turbo-0613") -> Int

Count number of tokens used by an OpenAI model.

## Arguments:

input - (str, list, dict): Input to the model.

model - (str): Model name.

## Returns:

int - Number of tokens from the input.

## Num_Tokens_From_Functions Def Num_Tokens_From_Functions(Functions, Model="Gpt-3.5-Turbo-0613") -> Int

Return the number of tokens used by a list of functions.

## Arguments:

functions - (list): List of function descriptions that will be passed in model. model - (str): Model name.

## Returns:

int - Number of tokens from the function descriptions.

Edit this page Copyright © 2024 AutoGen Authors | Privacy and Cookies