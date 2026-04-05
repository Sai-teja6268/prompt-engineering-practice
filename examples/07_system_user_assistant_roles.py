import sys
import os
from google import genai
from pathlib import Path
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

sys.path.append(str(Path(__file__).resolve().parent.parent))

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

system_instruction = """ 
You are going to act as a helpful teacher who is trying to help a 
student understand the concept of system, user and assistant roles 
in the context of AI language models.
"""

user_message = """
Can you explain the concept of system, user and assistant roles in the context of AI language models
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=user_message,
    config=types.GenerateContentConfig(
        system_instruction=system_instruction,
        temperature=0.7,
        top_p=0.5,
        max_output_tokens=20000,
    ),
)

print("SYSTEM ROLE:")
print("-" * 50)
print(system_instruction)

print("\nUSER ROLE:")
print("-" * 50)
print(user_message)

print("\nASSISTANT / MODEL RESPONSE:")
print("-" * 50)
print(response.text)

