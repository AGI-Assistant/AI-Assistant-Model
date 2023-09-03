import os
from dotenv import load_dotenv, find_dotenv
from flask import Flask, request, jsonify
from src_openai.pipeline.custom_prompter import model_generate

# Create the flask app
app = Flask(__name__)


# Listen for POST requests to /generate
@app.route('/generate', methods=['POST'])
def api_generate():
    # Check the API key
    if request.headers.get('BeKey') != backend_key:
        return jsonify({'message': 'Invalid API key'}), 403
    else:
        # Get the input data from the request
        data = request.get_json()

        print(data)

        # Generate the response
        generated_response = model_generate(
            prompt=data['userPrompt'],
            system_prompt=data['systemPrompt'],
            relationship=data['systemRelationship'],
            model_name=data['modelName'],
            temperature=data['temperature'],
            max_tokens=data['maxTokens'],
            openai_key=openai_key)

        # Return the results
        return jsonify({'answer': generated_response})


if __name__ == '__main__':
    # Load the environment variables
    load_dotenv(find_dotenv())
    backend_key = os.getenv('BACKEND_API_KEY')
    openai_key = os.getenv('OPENAI_API_KEY')

    # Start the app
    app.run(host='localhost', port=5005)
