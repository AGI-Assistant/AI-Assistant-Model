import gc
from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForCausalLM

# Create the flask app
app = Flask(__name__)

# Initialize model and tokenizer as None
model = None
tokenizer = None


@app.route('/start_up', methods=['POST'])
def start_up():
    global model, tokenizer
    # Get the model name from the request
    data = request.get_json()
    model_name = data.get('model')

    # Load the model and tokenizer
    model = AutoModelForCausalLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    return jsonify({'message': 'Model loaded successfully'})


@app.route('/generate', methods=['POST'])
def generate():
    global model, tokenizer
    # Check for API key
    if request.headers.get('X-API-Key') != 'Sd%7Rz#cdd2c65Uv@%Z':
        return jsonify({'message': 'Invalid API key'}), 403

    # Get the input data from the request
    data = request.get_json()
    prompt = data.get('prompt')
    settings = data.get('settings')

    # Generate the output using the model and tokenizer
    input_ids = tokenizer.encode(prompt, return_tensors='pt')
    output = model.generate(input_ids, settings.get('max_length'), settings.get('temperature'))
    output_text = tokenizer.decode(output[:, input_ids.shape[-1]:][0], skip_special_tokens=True)

    # Return the result
    return jsonify({'result': output_text})


@app.route('/shut_down', methods=['POST'])
def shut_down():
    global model, tokenizer
    # Delete the model and tokenizer
    del model
    del tokenizer
    # Prompt the garbage collector to free up memory
    gc.collect()
    # Set model and tokenizer back to None
    model = None
    tokenizer = None

    return jsonify({'message': 'Model unloaded successfully'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
