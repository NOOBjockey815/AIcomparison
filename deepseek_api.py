import random

# Simulating DeepSeek response since API is unavailable
def deepseek_response(prompt):
    responses = [
        "DeepSeek is currently unavailable.",
        "Simulated response based on available documentation.",
        "DeepSeek response: " + prompt[::-1]  # Just a fun simulation
    ]
    return random.choice(responses)
