import openai
from .env import open_ai_key

def ask(conversations):
    openai.api_key = open_ai_key
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversations,
        temperature=1
    )
    return res["choices"][0]["message"]["content"]

