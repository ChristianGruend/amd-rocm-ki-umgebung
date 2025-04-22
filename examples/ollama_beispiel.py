#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ein einfaches Beispiel zum Verwenden von Ollama über die API
"""

import requests
import json

def main():
    # Ollama API-Endpoint
    OLLAMA_API = "http://localhost:11435/api"
    
    # Verfügbare Modelle auflisten
    models_response = requests.get(f"{OLLAMA_API}/tags")
    models = models_response.json()
    
    print("Verfügbare Modelle:")
    if "models" in models and models["models"]:
        for model in models["models"]:
            print(f"- {model['name']}")
    else:
        print("Keine Modelle gefunden. Laden Sie ein Modell mit 'ollama pull MODEL_NAME'")
        print("Beispiel: curl -X POST http://localhost:11435/api/pull -d '{\"name\": \"llama3\"}'")
        return
    
    # Beispiel-Modell verwenden (ersetzen Sie 'llama3' mit einem verfügbaren Modell)
    model_name = models["models"][0]["name"] if models["models"] else "llama3"
    
    # Generiere Text mit dem Modell
    prompt = "Erkläre mir, wie AMD ROCm für Machine Learning verwendet wird."
    
    print(f"\nSende Anfrage an {model_name}...\n")
    print(f"Prompt: {prompt}\n")
    
    # API-Anfrage an Ollama senden
    generate_response = requests.post(
        f"{OLLAMA_API}/generate",
        json={
            "model": model_name,
            "prompt": prompt,
            "stream": False
        }
    )
    
    # Antwort anzeigen
    if generate_response.status_code == 200:
        result = generate_response.json()
        print(f"Antwort:\n{result['response']}")
    else:
        print(f"Fehler: {generate_response.status_code}")
        print(generate_response.text)

if __name__ == "__main__":
    main() 