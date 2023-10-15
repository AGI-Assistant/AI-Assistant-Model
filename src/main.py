"""
Module Name: main.py

Description:
    This is the main module of the application.
    It contains the main function for running the application.

Functions:
    - main(): This function runs the application.
"""
from dotenv import load_dotenv
from fastapi import FastAPI
from src.package import package
from src.model import api_replicate as model

if __name__ == '__main__':
    # Load the environment variables
    load_dotenv()

    # Initialize the app
    app = FastAPI()


    @app.post("/api/generate")
    async def generate(generate_json: dict) -> dict:
        """
        This function handles the /api/generate endpoint.

        :param generate_json: The application wide generate format.
        :type generate_json: generate.json
        :return: The application wide content format.
        :rtype: content.json
        """
        try:
            generated_content = model.chat_llama2_13b(prompt=generate_json['prompt'])
            return package.content_text(full_text_content=generated_content)
        except Exception as e:
            return package.content_text(error_occurred=str(e))
