# Dieses Skript nutzt die OpenAI API und unterstützt einen Testmodus.
# Im Testmodus entstehen keine Kosten. Bei aktivem API-Key wird die API genutzt.

import os
from openai import OpenAI
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key or api_key.strip() == "":
    print("⚠️ Testmodus aktiv – es entstehen keine API-Kosten.")
    api_key = None
else:
    print("ℹ️ OpenAI API aktiv – jede Anfrage zählt als API-Aufruf.")

def frage_chatgpt(frage):
    if not api_key:
        return "✅ Testmodus aktiv – dies ist eine simulierte Antwort."
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Du bist ein hilfreicher Assistent."},
            {"role": "user", "content": frage}
        ]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print("Willkommen im Chat! Schreibe 'exit' zum Beenden.")
    while True:
        frage = input("Du: ")
        if frage.lower() in ["exit", "quit", "stop"]:
            print("Chat beendet.")
            break

        antwort = frage_chatgpt(frage)
        print(f"ChatGPT: {antwort}\n")

        with open("chat_log.txt", "a", encoding="utf-8") as log_file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_file.write(f"[{timestamp}] Du: {frage}\n")
            log_file.write(f"[{timestamp}] ChatGPT: {antwort}\n\n")
