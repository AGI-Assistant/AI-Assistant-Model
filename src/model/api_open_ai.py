"""
Module Name: api_open_ai.py

Description:
    This module accesses openAi models via the openAi api.

Functions:
    - chat_gpt(prompt, system_prompt, max_tokens, min_tokens, temperature,
    top_p, top_k, stop_sequences, seed, debug): This function takes all the data
    and generates a response, using the openAI models.
"""
import openai


def chat_gpt(prompt: str,
             system_prompt: str = None,
             max_tokens: int = None,
             min_tokens: int = None,
             temperature: float = 0.7,
             top_p: float = None,
             top_k: int = None,
             stop_sequences: list[str] = None,
             seed: int = None,
             model: str = 'gpt-3.5-turbo'
             ) -> str:
    """
    This function takes all the data and generates a response,
    using the openAI models.

    :param prompt: The user's prompt.
    :type prompt: str
    :param system_prompt: The system prompt (what the model should pretend to be).
    :type system_prompt: str
    :param max_tokens: The maximum number of tokens (given + generated).
    :type max_tokens: int
    :param min_tokens: The minimum number of tokens (given + generated).
    :type min_tokens: int
    :param temperature: Controls the randomness of the model's output.
    :type temperature: float
    :param top_p: The cumulative probability cutoff for token selection.
    :type top_p: float
    :param top_k: The number of highest-probability tokens to consider for token selection.
    :type top_k: int
    :param stop_sequences: List of sequences to stop generation at.
    :type stop_sequences: list[str]
    :param seed: Seed value for random number generation, for reproducibility.
    :type seed: int
    :param model: The model to use.
    :type model: str
    :return: Returns the generated response as a string.
    :rtype: str
    """
    if system_prompt is None or system_prompt == '':
        message_prompts = [{"role": "user", "content": prompt}]
    else:
        message_prompts = [{"role": "system", "content": system_prompt},
                           {"role": "user", "content": prompt}]
    input_parameters = {key: value for key, value in {
        "model": model,
        "messages": message_prompts,
        "temperature": temperature,
        "max_tokens": max_tokens,
        "min_tokens": min_tokens,
        "top_p": top_p,
        "top_k": top_k,
        "stop": stop_sequences,
        "seed": seed
    }.items() if value is not None}
    output = openai.ChatCompletion.create(**input_parameters)
    return output['choices'][0]['text']
