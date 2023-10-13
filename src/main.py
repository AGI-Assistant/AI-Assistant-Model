"""
https://github.com/replicate/replicate-python#readme
"""

from datetime import datetime
from fastapi import FastAPI
import replicate


def package(text: str, is_user: bool = False, time: datetime = datetime.now()) -> dict:
    return {'text': text, 'isUser': is_user, 'time': int(time.timestamp())}


# Define the app
app = FastAPI()


@app.post("/api/assistant/llama/complete")
async def llama_complete(message: dict):
    # Generate a response
    llama_completion = replicate.run(
        "meta/llama-2-13b-chat:f4e2de70d66816a838a89eeeb621910adffb0dd0baba3976c96980970978018d",
        input={"prompt": "Hello, how are you?"}
    )

    # Package and return the response
    return package(llama_completion)
