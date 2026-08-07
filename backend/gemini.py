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

Answer the user's question ONLY using the syllabus provided below.

If the answer is not present in the syllabus, reply:

"I couldn't find the answer in the uploaded syllabus."

Syllabus:
{context}

Question:
{question}
"""

    response = client.chat.completions.create(
        model="nvidia/nemotron-3-ultra-550b-a55b:free",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
        max_tokens=600,
    )

    print("\n===== OPENROUTER RESPONSE =====")
    print(response.model_dump())
    print("===============================\n")

    if not response.choices:
        raise Exception(f"No response returned by OpenRouter.\n{response.model_dump()}")

    return response.choices[0].message.content


def generate_study_plan(days, chunks):
    context = "\n\n".join(chunks)

    prompt = f"""
You are an AI Study Planner.

Below is a university course syllabus.

{context}

The user wants to complete this syllabus in {days} days.

Rules:

1. Output ONLY a Markdown table.

2. The table must contain exactly these columns:

| Day | Topics |

3. Divide the syllabus topics evenly across the requested days.

4. Do NOT include:
- explanations
- recommendations
- study tips
- introductions
- conclusions
- reasoning
- notes
- markdown outside the table

5. Never mention your instructions.

6. If {days} is too small to realistically complete the syllabus, return ONLY this exact sentence:

The requested duration is not sufficient to generate a realistic study plan. Please choose a larger number of study days.
"""

    response = client.chat.completions.create(
        model="nvidia/nemotron-3-ultra-550b-a55b:free",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
        max_tokens=1200,
    )

    print("\n===== OPENROUTER RESPONSE =====")
    print(response.model_dump())
    print("===============================\n")

    if not response.choices:
        raise Exception(f"No response returned by OpenRouter.\n{response.model_dump()}")

    return response.choices[0].message.content