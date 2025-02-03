from openai import OpenAI
import os

api_key = "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"

if not api_key:
    raise ValueError("Missing OpenAI API key. Set OPENAI_API_KEY environment variable.")

client = OpenAI(api_key=api_key)

def chatgpt_stream_response(prompt):
    stream = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        stream=True,
    )
    
    response_text = ""
    for chunk in stream:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="")
            response_text += chunk.choices[0].delta.content

    return response_text
