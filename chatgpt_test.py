import os
from openai import OpenAI
from dotenv import load_dotenv

# .env laden
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
def frage_chatgpt(frage):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Du bist ein hilfreicher Assistent."},
            {"role": "user", "content": frage}
        ]
    )
    return response.choices[0].message.content

antwort = frage_chatgpt("Erkläre mir kurz, was Python ist.")
print("Antwort von ChatGPT:")
print(antwort)
