from transformers import AutoTokenizer, AutoModelWithLMHead


# This function runs the model and returns the results
def run_model(prompt: str, settings: dict) -> str:

    # Load the model and tokenizer
    model_name = settings['model_name']
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelWithLMHead.from_pretrained(model_name)

    # Encode context the generation is conditioned on
    inputs = tokenizer.encode(prompt, return_tensors='pt')

    # Run the model to generate the results
    outputs = model.generate(inputs, max_length=500)

    # Convert results to text and return them
    return tokenizer.decode(outputs[0])
