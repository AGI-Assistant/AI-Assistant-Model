import guidance


# Use the guidance program to generate a response
def model_generate(
        prompt: str,
        system_prompt: str,
        relationship: str,
        model_name: str,
        temperature: float,
        max_tokens: int,
        openai_key: str, ) -> str:
    # Set the model used for generating the response
    llm_model = guidance.llms.OpenAI(model=model_name, api_key=openai_key)

    # Define a guidance template for generation
    generated_template = llm_model('''                
    {{#system~}}
    {{system_prompt}}
    {{~/system}}

    {{#user~}}
    Here are some information about the user:
    {{prompt}}
    {{~/user}}

    {{#assistant~}}
    Here are some information about the users assistant and their relationship:
    {{relationship}}
    {{~/assistant}}

    {{#assistant~}}
    {{gen 'response' {{temperature}} {{max_tokens}}}}
    {{~/assistant}}
    ''')

    # Try to generate the response using the guidance template with the openai model
    try:
        # Generate the response
        generated_text = generated_template(
            system_prompt, prompt, relationship, temperature, max_tokens)
    # If an error occurs, return the error package instead
    except Exception as e:
        generated_text = str(e)

    # Return the result of the generation attempt
    return generated_text
