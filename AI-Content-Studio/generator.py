from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="distilgpt2"
)

#distilgpt2
#google/flan-t5-base

def generate_content(prompt):
    result = generator(
        prompt,
        max_new_tokens=200
    )
    return result[0]["generated_text"]