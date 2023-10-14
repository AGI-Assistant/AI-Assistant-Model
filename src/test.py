"""
https://github.com/replicate/replicate-python#readme
"""
import replicate
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# Generate a response
llama_completion = replicate.run(
    "meta/llama-2-13b-chat:f4e2de70d66816a838a89eeeb621910adffb0dd0baba3976c96980970978018d",
    input={"prompt": "Hello, how are you?"}
    )

for item in llama_completion:
    # https://replicate.com/meta/llama-2-13b-chat/versions/f4e2de70d66816a838a89eeeb621910adffb0dd0baba3976c96980970978018d/api#output-schema
    print(item, end="")
