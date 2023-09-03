import os
import guidance
from datetime import datetime
from dotenv import load_dotenv, find_dotenv
from flask import Flask, request
from flask_socketio import SocketIO

# Create the flask app
app = Flask(__name__)

# Initialize SocketIO with the Flask application
socketio = SocketIO(app, async_mode='eventlet')


# Use the guidance program to generate a response
def model_generate(
        prompt: str,
        user_data: str,
        system_prompt: str,
        relationship: str,
        context: str,
        model_name: str) -> dict:
    # Set the model used for generating the response
    llm_model = guidance.llms.OpenAI(model=model_name)

    # Define a guidance template for generation
    generated_template = guidance.Program("""                
    {{#system~}}
    {{system_prompt}}
    Following is some additional information to provide you with the context of the conversation.
    The User:
    {{user_data}}
    Their relationship:
    {{relationship}}
    Additional context:
    {{context}}
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
        # Generate the response
        generated_text = generated_template(
            system_prompt=system_prompt, user_data=user_data, relationship=relationship,
            context=context, prompt=prompt).get('answer')
        return {'answer': generated_text, 'status': 200}
    # If an error occurs, return the error message instead
    except Exception as e:
        return {'exception': str(e), 'status': 500}


# Listen for POST requests to /generate
@app.route('/generate', methods=['POST'])
def api_generate():
    # Check the API key
    if request.headers.get('BeKey') != backend_key:
        return {'message': 'Invalid API key'}, 403
    else:
        # Get the input data from the request
        data = request.get_json()
        data['context'] = "Date and Time: {}".format(
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        # Generate the response
        generated_response = model_generate(
            prompt=data['userPrompt'],
            user_data=data['userData'],
            context=data['context'],
            system_prompt=data['systemPrompt'],
            relationship=data['systemRelationship'],
            model_name="gpt-3.5-turbo")

        # Return the results
        return generated_response, generated_response['status']


if __name__ == '__main__':
    # Load the environment variables
    load_dotenv(find_dotenv())
    backend_key = os.getenv('BACKEND_API_KEY')

    # Start the app with SocketIO
    socketio.run(app, host='localhost', port=5005)
