import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv()

API_KEY=os.getenv("API_GEMINI_KEY")
genai.configure(api_key=API_KEY)

print("Modelos disponíveis para você:")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)