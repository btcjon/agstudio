AutoGen Search Referenceagentchatagentchat.contribimg_utils On this page

## Agentchat.Contrib.Img_Utils Llava_Formatter Def Llava_Formatter(Prompt: Str, Order_Image_Tokens: Bool = False) -> Tuple[Str, List[Str]]

Formats the input prompt by replacing image tags and returns the new prompt along with image locations.

## Arguments:

prompt (str): The input string that may contain image tags like <img ...>. order_image_tokens (bool, optional): Whether to order the image tokens with numbers. It will be useful for GPT-4V. Defaults to False.

## Returns:

Tuple[str, List[str]]: A tuple containing the formatted string and a list of images (loaded in b64 format).

## Gpt4V_Formatter Def Gpt4V_Formatter(Prompt: Str) -> List[Union[Str, Dict]]

Formats the input prompt by replacing image tags and returns a list of text and images.

## Arguments:

prompt (str): The input string that may contain image tags like <img ...>.

## Returns:

List[Union[str, dict]]: A list of alternating text and image dictionary items.

## Extract_Img_Paths Def Extract_Img_Paths(Paragraph: Str) -> List

Extract image paths (URLs or local paths) from a text paragraph.

## Arguments:

paragraph str - The input text paragraph.

## Returns:

list - A list of extracted image paths.

Edit this page Previous « gpt_assistant_agent Copyright © 2024 AutoGen Authors | Privacy and Cookies