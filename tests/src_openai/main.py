"""
This file contains the code for accessing the OpenAI API.
"""

import os
import guidance
from datetime import datetime
from dotenv import load_dotenv, find_dotenv
from flask import Flask, request
from flask_socketio import SocketIO

# Create the flask application
app = Flask(__name__)

# Initialize SocketIO with the Flask application
socketio = SocketIO(app, async_mode='eventlet')


# Generate response
def model_generate(
        prompt: str,
        user_data: str,
        system_prompt: str,
        relationship: str,
        context: str,
        model_name: str) -> dict:
    """
    This function takes all the data and generates a response using the OpenAI API.
    It does so by using the guidance library to generate a template, which
    is then filled with the data and used to generate the response.

    Args:
        prompt (str): The user's prompt.
        user_data (str): Data about the user.
        system_prompt (str): The system prompt or what the model should pretend to be.
        relationship (str): The relationship between the user and his assistant.
        context (str): Additional context to provide the model with.
        model_name (str): The name of the model used for generation.

    Returns:
        dict (answer or exception (str), status (int)): A dictionary holding
        the generated answer as a string or the exception package if an error has occurred.
        The dictionary also contains a status code.
    """
    # Set the model used for generating the response
    llm_model = guidance.llms.OpenAI(model=model_name)

    # Define a guidance template for generation
    generated_template = guidance.Program("""                
    {{#system~}}
    You are: {{system_prompt}}
    The user: {{user_data}}
    Their relationship: {{relationship}}
    Additional context: {{context}}
    {{~/system}}

    {{#user~}}
    {{prompt}}
    {{~/user}}

    {{#assistant~}}
    {{gen 'answer' temperature=0.5 max_tokens=256}}
    {{~/assistant}}
    """, llm=llm_model, silent=True, stream=False)

    # Try to generate the response using the guidance template with the openai model
    try:
        # API call to generate the response
        generated_text = generated_template(
            system_prompt=system_prompt, user_data=user_data, relationship=relationship,
            context=context, prompt=prompt).get('answer')
        # Return the generated response
        return {'answer': generated_text, 'status': 200}
    except Exception as e:
        # If an error has occurred, return the error package instead
        return {'exception': str(e), 'status': 500}


# Generate endpoint
@app.route('/generate', methods=['POST'])
def api_generate():
    """
    This function listens to a POST requests to the /generate endpoint.
    It then calls the model_generate function to generate a response
    and sends back the result.

    Headers:
        backendKey (str): The API key used to access the endpoint.
    
    Body:
        data (application/json): A JSON object containing all the
        required data, including the prompt and all contexts.

    Returns:
        json-body (application/json): A JSON object holding the generated
        answer as a string or the exception package if an error has occurred.
        The dictionary also contains a status code.
    """
    # Check the API key
    if request.headers.get('backendKey') != backend_key:
        # Return an error if the API key is invalid
        return {'package': 'Invalid API key'}, 403
    else:
        # Get the input data from the request
        data = request.get_json()
        # Add some simple context to the data (in this case, date and time)
        data['context'] = "Date and Time: {}".format(
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        # Call the generation method with the data from the request
        generated_response = model_generate(
            prompt=data['userPrompt'],
            user_data=data['userData'],
            context=data['context'],
            system_prompt=data['systemPrompt'],
            relationship=data['systemRelationship'],
            model_name="gpt-3.5-turbo")

        # Return the results as a JSON object
        return generated_response, generated_response['status']


# Main function to run the app
if __name__ == '__main__':
    # Load the environment variables
    load_dotenv(find_dotenv())
    backend_key = os.getenv('BACKEND_API_KEY')

    # Start the app with SocketIO
    # This is done to handle the asynchronous requests to the openai API
    socketio.run(app, host='localhost', port=5005)
