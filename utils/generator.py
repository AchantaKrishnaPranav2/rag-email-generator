from utils.vectorstore import retrieve
from utils.llm import generate

def generate_email(persona, cadence, goal):

    context = retrieve(goal)

    context_text = "\n\n".join(context)

    prompt = f"""
You are an expert B2B email writer.

Persona:
{persona}

Cadence:
{cadence}

Context from documents:
{context_text}

Goal:
{goal}

Write a professional email using ONLY the provided context.
Do not hallucinate.
"""

    return generate(prompt)

