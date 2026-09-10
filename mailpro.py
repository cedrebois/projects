import json
from typing import List, Dict
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

SYSTEM_PROMPT = (
    "You are MailPro, an AI assistant specialized in professional business emails.\n"
    "You write, reply to, rewrite, and summarize emails.\n"
    "Always produce clear, well-structured emails.\n"
    "Match the requested tone.\n"
    "If the user asks to save an email, confirm and save it.\n"
    "Make reasonable assumptions if details are missing."
)

# ---------- Tools ----------

def write_json(filepath: str, content: str) -> str:
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump({"content": content}, f, indent=2, ensure_ascii=False)
        return f"Email saved to {filepath}"
    except Exception as e:
        return f"Error saving email: {e}"

def read_json(filepath: str) -> str:
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f).get("content", "")
    except Exception as e:
        return f"Error reading file: {e}"

# ---------- Agent Logic ----------

def ask_mailpro(user_input: str, history: List[Dict[str, str]]) -> str:
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    messages.extend(history)
    messages.append({"role": "user", "content": user_input})

    response = client.responses.create(
        model="gpt-4o-mini",
        input=messages
    )

    content = response.output_text

    # 🔎 Very simple tool trigger (you can improve later)
    if "save" in user_input.lower() and ".json" in user_input.lower():
        filepath = user_input.split()[-1]
        write_json(filepath, content)

    return content
