import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def query_llm(prompt):
    payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0,
            "top_p": 1
        }
    }

    response = requests.post(OLLAMA_URL, json=payload)

    result = response.json()

    return result["response"]