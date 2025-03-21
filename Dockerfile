# Basis-Image mit Python 3.11
FROM python:3.11-slim

# Arbeitsverzeichnis im Container
WORKDIR /app

# Projektdateien in den Container kopieren
COPY . .

# Abhängigkeiten installieren
RUN pip install --no-cache-dir openai python-dotenv

# Startbefehl definieren
CMD ["python3", "chatgpt_test.py"]
