Search Referencefunction_utils On this page

## Function_Utils

get_typed_annotation

## Def Get_Typed_Annotation(Annotation: Any, Globalns: Dict[Str, Any]) -> Any

Get the type annotation of a parameter.

annotation - The annotation of the parameter globalns - The global namespace of the function

The type annotation of the parameter get_typed_signature

## Def Get_Typed_Signature(Call: Callable[..., Any]) -> Inspect.Signature

Get the signature of a function with type annotations.

call - The function to get the signature for

The signature of the function with type annotations get_typed_return_annotation

## Def Get_Typed_Return_Annotation(Call: Callable[..., Any]) -> Any

Get the return annotation of a function.

call - The function to get the return annotation for Returns: The return annotation of the function get_param_annotations def get_param_annotations( typed_signature: inspect.Signature ) -> Dict[int, Union[Annotated[Type[Any], str], Type[Any]]]
Get the type annotations of the parameters of a function

typed_signature - The signature of the function with type annotations

A dictionary of the type annotations of the parameters of the function

## Parameters Objects Class Parameters(Basemodel)

Parameters of a function as defined by the OpenAI API

## Function Objects Class Function(Basemodel)

A function as defined by the OpenAI API

## Toolfunction Objects Class Toolfunction(Basemodel)

A function under tool as defined by the OpenAI API. get_parameter_json_schema def get_parameter_json_schema( k: str, v: Union[Annotated[Type[Any], str], Type[Any]], default_values: Dict[str, Any]) -> JsonSchemaValue Get a JSON schema for a parameter as defined by the OpenAI API Arguments:

k - The name of the parameter v - The type of the parameter default_values - The default values of the parameters of the function
Returns: A Pydanitc model for the parameter get_required_params

## Def Get_Required_Params(Typed_Signature: Inspect.Signature) -> List[Str]

Get the required parameters of a function Arguments:
signature - The signature of the function as returned by inspect.signature Returns: A list of the required parameters of the function get_default_values

## Def Get_Default_Values(Typed_Signature: Inspect.Signature) -> Dict[Str, Any]

Get default values of parameters of a function Arguments:
signature - The signature of the function as returned by inspect.signature Returns: A dictionary of the default values of the parameters of the function get_parameters def get_parameters(required: List[str], param_annotations: Dict[str, Union[Annotated[Type[Any], str], Type[Any]]], default_values: Dict[str, Any]) -> Parameters

required - The required parameters of the function hints - The type hints of the function as returned by typing.get_type_hints

A Pydantic model for the parameters of the function get_missing_annotations def get_missing_annotations(typed_signature: inspect.Signature, required: List[str]) -> Tuple[Set[str], Set[str]]
Get the missing annotations of a function Ignores the parameters with default values as they are not required to be annotated, but logs a warning.

typed_signature - The signature of the function with type annotations required - The required parameters of the function

A set of the missing annotations of the function get_function_schema def get_function_schema(f: Callable[..., Any], *, name: Optional[str] = None, description: str) -> Dict[str, Any]
Get a JSON schema for a function as defined by the OpenAI API

f - The function to get the JSON schema for name - The name of the function description - The description of the function Returns: A JSON schema for the function Raises:
TypeError - If the function is not annotated Examples:
``` def f(a: Annotated[str, "Parameter a"], b: int = 2, c: Annotated[float, "Parameter c"] = 0.1) -> None: pass get_function_schema(f, description="function f") #   {'type': 'function', #    'function': {'description': 'function f', #        'name': 'f', #        'parameters': {'type': 'object', #           'properties': {'a': {'type': 'str', 'description': 'Parameter a'}, #               'b': {'type': 'int', 'description': 'b'}, #               'c': {'type': 'float', 'description': 'Parameter c'}}, #           'required': ['a']}}} ```
get_load_param_if_needed_function def get_load_param_if_needed_function( t: Any) -> Optional[Callable[[T, Type[Any]], BaseModel]]
Get a function to load a parameter if it is a Pydantic model t - The type annotation of the parameter

A function to load the parameter if it is a Pydantic model, otherwise None

## Load_Basemodels_If_Needed Def Load_Basemodels_If_Needed(Func: Callable[..., Any]) -> Callable[..., Any]

A decorator to load the parameters of a function if they are Pydantic models

func - The function with annotated parameters

A function that loads the parameters before calling the original function Edit this page Previous « code_utils Next math_utils »
Community Discord Twitter