from groq import Groq
from config import GROQ_API_KEY

client = Groq(
    api_key=GROQ_API_KEY
)

def ask_llm(prompt):

    try:

        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3,
            max_tokens=4096
        )

        return completion.choices[0].message.content

    except Exception as e:

        return f"Error: {str(e)}"