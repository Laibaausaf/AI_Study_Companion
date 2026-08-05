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

You are given a syllabus extracted from a PDF.

Your task is to create a study plan.

Use ONLY the syllabus topics from the context.

Do NOT say that the answer is not found.

If the user asks for a study plan:

• Divide the syllabus evenly.
• Create a day-wise schedule.
• Mention the topics to study each day.
• Keep the output neat and readable.

Context:
{context}

User Request:
{question}
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
def generate_study_plan(days, chunks):

    context = "\n\n".join(chunks)

    prompt = f"""
You are an expert study planner.

Using ONLY the syllabus below, create a detailed {days}-day study plan.

Instructions:
- Divide topics across {days} days.
- Keep the workload balanced.
- Include revision days if appropriate.
- Output in clean Markdown.
- Use headings and bullet points.
- Do NOT invent topics that are not in the syllabus.

Syllabus:

{context}
"""

    response = client.chat.completions.create(
         model="nvidia/nemotron-3-ultra-550b-a55b:free",   # keep using the model that worked
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=1200,
    )

    return response.choices[0].message.content