import requests

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "llama3:8b"

CHAT_HISTORY = []
MAX_HISTORY = 4

def ask_ai(prompt):
    global CHAT_HISTORY

    CHAT_HISTORY.append({"role": "user", "content": prompt})
    CHAT_HISTORY = CHAT_HISTORY[-MAX_HISTORY:]

    try:
        r = requests.post(OLLAMA_URL, json={
            "model": MODEL,
            "messages": CHAT_HISTORY,
            "stream": False
        })

        reply = r.json()["message"]["content"]
        CHAT_HISTORY.append({"role": "assistant", "content": reply})
        return reply

    except:
        return "AI offline or not responding"
