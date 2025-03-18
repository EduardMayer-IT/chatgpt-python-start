# Dieses Skript nutzt die OpenAI API und unterstützt einen Testmodus.
# Im Testmodus entstehen keine Kosten. Bei aktivem API-Key wird die API genutzt.

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

# Sicherer Check: auch leere Einträge abfangen
if not api_key or api_key.strip() == "":
    print("⚠️ Testmodus aktiv – es entstehen keine API-Kosten.")
    api_key = None  # API-Key sicher auf None setzen
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

# Einmaliger Testaufruf
antwort = frage_chatgpt("Erklär mir Python!")
print("Antwort:", antwort)

with open("chat_log.txt", "a") as log:
    log.write(f"Du: {frage}\n")
    log.write(f"ChatGPT: {antwort}\n\n")


# Chat-Schleife
if __name__ == "__main__":
    print("Willkommen im Chat! Schreibe 'exit' zum Beenden.")
    while True:
        frage = input("Du: ")
        if frage.lower() in ["exit", "quit", "stop"]:
            print("Chat beendet.")
            break
        antwort = frage_chatgpt(frage)
        print(f"ChatGPT: {antwort}\n")
