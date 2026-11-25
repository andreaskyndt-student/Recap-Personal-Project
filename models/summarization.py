import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

MODEL_NAME = "google/flan-t5-base"

device = "cuda" if torch.cuda.is_available() else "cpu"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
model.to(device)

def summarize_text(text) :
    prompt = f"Summarize the following text clearly (as a lecture): \n\n{text}"

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        max_length=1024,
        truncation=True
    ).to(device)

    with torch.no_grad():
        summary_ids = model.generate(
            **inputs,
            max_new_tokens=150,
            do_sample=False,
        )

    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return summary