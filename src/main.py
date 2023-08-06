from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForCausalLM
import model_runner

# Create the flask app
app = Flask(__name__)

# Initialize model and tokenizer
model_name = 'gpt2'  # Replace with your model name
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)


@app.route('/generate', methods=['POST'])
def generate():
    # Check for API key
    if request.headers.get('X-API-Key') != 'Sd%7Rz#cdd2c65Uv@%Z':
        return jsonify({'message': 'Invalid API key'}), 403

    # Get the input data from the request
    data = request.get_json()
    prompt = data.get('prompt')
    settings = data.get('settings')

    # Generate the output using the model and tokenizer
    output_text = model_runner.run(model, tokenizer, prompt, settings)

    # Return the result
    return jsonify({'result': output_text})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
