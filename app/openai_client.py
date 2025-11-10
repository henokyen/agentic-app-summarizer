import os
from openai import OpenAI
from app.configs.app_configs import open_api_key

client = OpenAI(api_key=open_api_key)

def summerize_text(text: str) -> str:
    prompt = f"Summarize the following text:\n\n{text}\n\nSummary:"
    with client.chat.completions.stream(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    ) as stream:
        for chunk in stream:
            if chunk.choices[0].delta.get("content"):
                yield chunk.choices[0].delta.content
                