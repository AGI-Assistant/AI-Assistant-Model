"""
Module Name: api_replicate.py

Description:
    This module accesses models via the replicate api.

Functions:
    - chat_llama2_13b(prompt, system_prompt, max_new_tokens, min_new_tokens,
    temperature, top_p, top_k, stop_sequences, seed, debug): This function takes
    all the data and generates a response, using the llama 2 13b large language model.
"""
import replicate


def chat_llama2_13b(prompt: str,
                    system_prompt: str = None,
                    max_new_tokens: int = None,
                    min_new_tokens: int = None,
                    temperature: float = None,
                    top_p: float = None,
                    top_k: int = None,
                    stop_sequences: str = None,
                    seed: int = None,
                    debug: bool = None
                    ) -> str:
    """
    This function takes all the data and generates a response,
    using the llama 2 13b large language model.

    https://replicate.com/meta/llama-2-13b-chat/api

    :param prompt: The user's prompt.
    :type prompt: str
    :param system_prompt: The system prompt (what the model should pretend to be).
    :type system_prompt: str
    :param max_new_tokens: The maximum number of new tokens to be generated.
    :type max_new_tokens: int
    :param min_new_tokens: The minimum number of new tokens to be generated.
    :type min_new_tokens: int
    :param temperature: Controls the randomness of the model's output.
    :type temperature: float
    :param top_p: The cumulative probability cutoff for token selection.
    :type top_p: float
    :param top_k: The number of highest-probability tokens to consider for token selection.
    :type top_k: int
    :param stop_sequences: Comma-separated string(list) of sequences to stop generation at.
    Example: '<end>,<stop>' = stops generation at first instance of 'end' or '<stop>'.
    :type stop_sequences: str
    :param seed: Seed value for random number generation, for reproducibility.
    :type seed: int
    :param debug: Enables debugging output in logs.
    :type debug: bool
    :return: Returns the generated response as a whole string.
    :rtype: str
    """

    # Create a dictionary of input variables.
    input_parameters = {key: value for key, value in {
        "prompt": prompt,
        "system_prompt": system_prompt,
        "max_new_tokens": max_new_tokens,
        "min_new_tokens": min_new_tokens,
        "temperature": temperature,
        "top_p": top_p,
        "top_k": top_k,
        "stop_sequences": stop_sequences,
        "seed": seed,
        "debug": debug
    }.items() if value is not None}

    # Make an API call to get the webhook.
    webhook = replicate.run(
        "meta/llama-2-13b-chat:f4e2de70d66816a838a89eeeb621910adffb0dd0baba3976c96980970978018d",
        input=input_parameters)

    # Iterate over the webhook and concatenate the output.
    output = ""
    for item in webhook:
        output += item

    # Return the output.
    return output
