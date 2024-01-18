Referencemath_utils

## Math_Utils

solve_problem

## Def Solve_Problem(Problem: Str, **Config) -> Str

(openai<1) Solve the math problem. Arguments:
problem str - The problem statement.

config *Optional, dict* - The configuration for the API call.

## Returns:

str - The solution to the problem.

remove_boxed

## Def Remove_Boxed(String: Str) -> Optional[Str]

Source: https://github.com/hendrycks/math Extract the text within a \boxed{...} environment. Example: > remove_boxed("\boxed{\frac{2}{3}}") \frac{2}{3} last_boxed_only_string

## Def Last_Boxed_Only_String(String: Str) -> Optional[Str]

Source: https://github.com/hendrycks/math Extract the last \boxed{...} or \fbox{...} element from a string. is_equiv

## Def Is_Equiv(Str1: Optional[Str], Str2: Optional[Str]) -> Float

Returns (as a float) whether two strings containing math are equivalent up to differences of formatting in

units
fractions
square roots
superfluous LaTeX. Source: https://github.com/hendrycks/math

is_equiv_chain_of_thought

## Def Is_Equiv_Chain_Of_Thought(Str1: Str, Str2: Str) -> Float

Strips the solution first before calling is_equiv.

## Eval_Math_Responses Def Eval_Math_Responses(Responses, Solution=None, **Args)

Select a response for a math problem using voting, and check if the response is correct if the solution is provided. Arguments:
responses *list* - The list of responses.

solution str - The canonical solution.

## Returns:

dict - The success metrics.

Edit this page Previous « function_utils Community Discord Twitter Copyright © 2024 AutoGen Authors | Privacy and Cookies Next retrieve_utils »