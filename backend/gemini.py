import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def generate_answer(question, chunks):

    context = "\n\n".join(chunks)

    prompt = f"""
You are an AI Study Companion.

Use ONLY the provided context to answer the user's question.

If the answer is not present in the context, reply exactly:

"I couldn't find the answer in the provided study material."

Do not make up information.
Do not use your own knowledge.

Context:
{context}

Question:
{question}

Answer:
"""

    response = client.chat.completions.create(
    model="nvidia/nemotron-3-ultra-550b-a55b:free",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=500,
    )

    return response.choices[0].message.content