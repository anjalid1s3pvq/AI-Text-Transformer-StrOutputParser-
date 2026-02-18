#!/usr/bin/env python3
"""
Find available Groq models for your API key
"""

from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("❌ No GROQ_API_KEY found in .env file")
    exit(1)

print("Testing different Groq models...\n")

# Common model names to try
models = [
    "mixtral-8x7b-32768",
    "llama2-70b-4096",
    "llama-3-8b-instant",
    "llama-3-70b",
    "llama3-8b",
    "llama3-70b",
    "llama-3.1-8b-instant",
    "llama-3.1-70b-versatile",
    "llama-3.2-70b-text",
    "llama-3.2-90b-text",
    "gemma-7b-it",
    "gemma2-9b-it",
]

working_models = []

for model in models:
    try:
        llm = ChatGroq(model=model, api_key=api_key)
        # Try a simple test
        response = llm.invoke("Say 'OK'")
        working_models.append(model)
        print(f"✅ {model} - WORKING")
    except Exception as e:
        error_msg = str(e)
        if "decommissioned" in error_msg.lower():
            print(f"❌ {model} - DECOMMISSIONED")
        elif "not found" in error_msg.lower() or "does not exist" in error_msg.lower():
            print(f"⚠️  {model} - NOT AVAILABLE")
        else:
            print(f"⚠️  {model} - ERROR: {error_msg[:50]}")

if working_models:
    print(f"\n✅ AVAILABLE MODELS: {', '.join(working_models)}")
    print(f"\nUpdate ai_text_transformer.py to use one of these models:")
    print(f"  model=\"{working_models[0]}\"")
else:
    print("\n❌ No working models found. Check your API key.")
