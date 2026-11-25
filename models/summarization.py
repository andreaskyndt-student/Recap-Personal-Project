import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

MODEL_NAME = "google/flan-t5-base"

device = "cuda" if torch.cuda.is_available() else "cpu"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
model.to(device)

def summarize_text(text) :
    prompt = f"""
        You are an expert lecture summarization assistant.

        Create a clear and informative summary of the following lecture.
        - Include the most important information.
        - Remove repetitive information.
        - Organize related topics together.
        - Do not invent information.
        - Write in the same language as the original text.

        Lecture:
        {text}

        Summary:
        """

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        max_length=1024,
        truncation=True
    ).to(device)

    with torch.no_grad():
        summary_ids = model.generate(
            **inputs,
            max_new_tokens=200,
            num_beams=4,
            repetition_penalty=1.5,
            no_repeat_ngram_size=3,
            early_stopping=True,
        )

    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return summary