from ollama_interface import query_ollama

def get_counterargument(user_argument):
    prompt = f"""You're an intelligent debate partner. The user said: "{user_argument}".
Reply with a strong counterargument in 2-3 sentences."""
    return query_ollama(prompt)

def analyze_argument(user_argument):
    prompt = f"""You're a debate coach. Analyze this argument: "{user_argument}".
Give:
1. Strengths
2. Weaknesses
3. Logical fallacies (if any)
4. Suggestions to improve."""
    return query_ollama(prompt)
