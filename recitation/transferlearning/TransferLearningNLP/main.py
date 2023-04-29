from transformers import T5ForConditionalGeneration, T5Tokenizer

def summarize_text(model_name_or_path, input_file, output_file, max_length=512):
    # Load the pre-trained model
    model = T5ForConditionalGeneration.from_pretrained(model_name_or_path)
    tokenizer = T5Tokenizer.from_pretrained(model_name_or_path, model_max_length=1024)

    with open(input_file, "r") as f:
        text = f.read()

    input_ids = tokenizer.encode(text, return_tensors="pt", max_length=max_length, truncation=True)

    # Generate the summary
    summary_ids = model.generate(input_ids, max_new_tokens=128)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    with open(output_file, "w") as f:
        f.write(summary)

if __name__ == "__main__":
    model_name_or_path = "t5-small"
    input_file = "input.txt"
    output_file = "output.txt"
    summarize_text(model_name_or_path, input_file, output_file)