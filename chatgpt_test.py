# Dieses Skript nutzt die OpenAI API und unterstützt einen Testmodus
# Dieses Skript nutzt die OpenAI API und unterstützt einen Testmodus

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

def frage_chatgpt(frage):
    if not api_key:
        return "✅ Testmodus aktiv – keine echte API-Antwort."
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Du bist ein hilfreicher Assistent."},
            {"role": "user", "content": frage}
        ]
    )
    return response.choices[0].message.content

# Test
antwort = frage_chatgpt("Erklär mir Python!")
print("Antwort:", antwort)

