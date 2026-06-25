from groq import Groq

client = Groq(
    api_key="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"
)

def generate_content(prompt):

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content
