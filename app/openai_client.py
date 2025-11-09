import os
from openai import OpenAI
from app.configs.app_configs import open_api_key

client = OpenAI(api_key=open_api_key)

def summerize_text(text: str) -> str:
    prompt = f"Summarize the following text:\n\n{text}\n\nSummary:"
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    summary = response.choices[0].message.content.strip()
    return summary