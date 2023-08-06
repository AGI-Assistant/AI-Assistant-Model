def run(model, tokenizer, prompt: str, settings: dict) -> str:
    # Encode context the generation is conditioned on
    inputs = tokenizer.encode(prompt, return_tensors='pt')

    # Run the model to generate the results
    outputs = model.generate(inputs, max_length=settings.get('max_length'),
                             temperature=settings.get('temperature'))

    # Convert results to text and return them
    return tokenizer.decode(outputs[:, inputs.shape[-1]:][0], skip_special_tokens=True)
