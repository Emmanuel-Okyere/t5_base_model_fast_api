def translate_text(model, tokenizer, source, destination, texts):
    """Translates the text depending on the entry"""
    input_ids = tokenizer(
        f"translate {source} to {destination}: " + texts, return_tensors="pt"
    ).input_ids
    outputs = model.generate(input_ids)
    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return decoded
