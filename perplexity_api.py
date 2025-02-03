import requests
import os

PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")
PERPLEXITY_URL = "https://api.perplexity.ai"

def perplexity_response(prompt):
    headers = {"Authorization": f"Bearer {PERPLEXITY_API_KEY}"}
    data = {"query": prompt}
    response = requests.post(PERPLEXITY_URL, headers=headers, json=data)
    return response.json().get("output", "No response")
