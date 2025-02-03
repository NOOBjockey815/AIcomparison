def evaluate_response(response, dimension):
    criteria = {
        "accuracy": lambda r: 10 if "correct" in r.lower() else 7,
        "creativity": lambda r: len(set(r.split())) / len(r.split()) * 10,
        "speed": lambda r: 9,  # Simulated constant score
        "contextual": lambda r: 8 if "understood" in r.lower() else 6,
        "bias": lambda r: 5 if "controversial" in r.lower() else 9,
    }
    return criteria.get(dimension, lambda r: 7)(response)
