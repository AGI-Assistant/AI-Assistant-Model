import os
import guidance
from dotenv import load_dotenv, find_dotenv
from flask import Flask, request, jsonify

# Create the flask app
app = Flask(__name__)


# Listen for POST requests to /generate
@app.route('/generate', methods=['POST'])
def generate():
    # Check the API key
    if request.headers.get('X-API-Key') != backend_key:
        return jsonify({'message': 'Invalid API key'}), 403
    else:
        # Get the input data from the request
        data = request.get_json()
        prompt = data.get('prompt')
        settings = data.get('settings')

        # Generate the output using the model and tokenizer
        output_text = run_model(model, tokenizer, prompt, settings)

        # Return the result
        return jsonify({'result': output_text})


# Method to generate text
def openai_generate(prompt, settings):
    # Generate the output using the model and tokenizer
    output_text = run_model(model, tokenizer, prompt, settings)

    # Return the result
    return jsonify({'result': output_text})

if __name__ == '__main__':
    # Load the environment variables
    load_dotenv(find_dotenv())
    backend_key = os.getenv('BACKEND_API_KEY')

    # Set default language model
    guidance.llm = guidance.llms.OpenAI("gpt-3.5-turbo")

    # Start the app
    app.run(host='0.0.0.0', port=5000)
