# ChatGPT Python API Projekt

## 📜 Beschreibung
Dieses Projekt zeigt, wie man mit Python und der OpenAI-API kommuniziert.  
Das Skript lädt den API-Key sicher aus einer `.env`-Datei und führt einen Chat mit ChatGPT im Terminal.

## 🔧 Technologien
- Python 3
- OpenAI API
- python-dotenv (zum Laden der Umgebungsvariablen)
- Git und GitHub

## ▶️ Ausführung
1. Installiere die Abhängigkeiten:


## ✅ Features
- API-Anbindung
- Umgebungsvariablen aus `.env`
- Chat-Schleife direkt im Terminal

## 📎 Autor
Eduard Mayer  
GitHub: [https://github.com/EduardMayer-IT](https://github.com/EduardMayer-IT)

## 🔄 Testmodus (API-kostenfrei testen)
Das Skript erkennt automatisch, ob ein OpenAI API-Key vorhanden ist. 
Fehlt der Schlüssel oder ist die `.env` leer, läuft das Skript im **Testmodus**:
- Keine Verbindung zur OpenAI API
- Keine Kosten
- Simulierte Antworten im Chat

## 📋 Funktionen

- Kommunikation mit der OpenAI API
- Vollständiger Testmodus ohne API-Kosten
- Speicherung des gesamten Chat-Verlaufs in `chat_log.txt`
- Erweiterbar um Zeiterfassung und weitere Features

## 🛠 Testmodus (kostenfrei)
Falls kein API-Key in der `.env` hinterlegt ist, arbeitet das Skript im **Testmodus**:
- Keine Verbindung zur OpenAI API
- Keine Kosten
- Simulierte Antworten im Terminal und in der Log-Datei

## 🗒 Chat-Logging
Jede Unterhaltung wird automatisch in der Datei `chat_log.txt` gespeichert:
- Frage und Antwort werden protokolliert
- Optional mit Zeitstempel erweiterbar
