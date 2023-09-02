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
        systempromt = data.get('systemPropmt')
        prompt = data.get('prompt')
        userdata = data.get('userData')
        settings = data.get('settings')

        # Generate the response
        response = generate(prompt=prompt, user_data, assistant_data, temprature=settings)

        # Return the result
        return jsonify({'response': response})


# Use the guidance program to generate a response
def generate(prompt str,
             systempromt str='You are a helpful digital assistant.',
             character_relationship str='This is the first time the user meets with his new assistant.',
             model str='gpt-3.5-turbo',
             temprature float=0.5,
             max_tokens int=256) -> str:
    
    # Define a guidance template for generating the response
    generated_template = guidance("""                 
    {{#system~}}
    {{systempromt}}
    {{~/system}}

    {{#user~}}
    Here are some information about the user:
    {{prompt}}
    {{~/user}}

    {{#assistant~}}
    Here are some information about the users assistant and their relationship:
    {{character_relationship}}
    {{~/assistant}}
                                  
    {{#assistant~}}
    {{gen 'response' {{temperature}} {{max_tokens}}}}
    {{~/assistant}}
    """, prompt=prompt, systempromt=systempromt, character_relationship=character_relationship, temperature=temprature, max_tokens=max_tokens, model=model)
    
    # Generate the response
    try:
        generated_text = generated_template()
    except Exception as e:
        generated_text = str(e)

    # Return the result
    return generated_text

if __name__ == '__main__':
    # Load the environment variables
    load_dotenv(find_dotenv())
    backend_key = os.getenv('BACKEND_API_KEY')

    # Set default language model
    generate()

    # Start the app
    app.run(host='0.0.0.0', port=5000)
