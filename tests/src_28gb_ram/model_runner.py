# This function runs the model and returns the results
def run_model(model, tokenizer, prompt: str, settings: dict) -> str:
    # Encode context the generation is conditioned on
    inputs = tokenizer.encode(prompt, return_tensors='pt')

    # Move the inputs to the same device as the model
    inputs = inputs.to(model.device)

    # Run the model to generate the results
    outputs = model.generate(inputs, max_length=500)

    # Convert results to text and return them
    return tokenizer.decode(outputs[0])
