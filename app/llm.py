# ✅ app/llm.py (Switch to flan-t5-large for better answers)

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

model_name = "google/flan-t5-large"  # Upgraded from flan-t5-base

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def ask_llm(context, query):
    prompt = f"""
You are a legal assistant. Based on the context below, provide a clear and detailed legal answer to the question. Use only the given context and answer in 3–5 complete sentences.

Context:
{context}

Question:
{query}

Answer:
"""

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=300,
            do_sample=True,
            temperature=0.7,
            top_k=50,
            top_p=0.95,
            early_stopping=True
        )

    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Fallback if answer is too short or generic
    short_response = decoded.strip().lower()
    if short_response in ["yes", "no"]:
        return "The context suggests a legal nuance. Please review the case details further or consult legal counsel."

    # Extract clean answer
    if "Answer:" in decoded:
        return decoded.split("Answer:")[-1].strip()
    else:
        return decoded.strip()
