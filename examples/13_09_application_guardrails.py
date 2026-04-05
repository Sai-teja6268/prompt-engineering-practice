"""
application_guardrails.py
use case: hosipital patient intake assistant that must follow the application guardrails.
"""

import re
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

raw_message="""
Patient Name: John Doe
Age: 45
email:rahul@gmail.com
ward: cardiology - Room 11
symptoms: chest pain, shortness of breath, fatigue
"""

sanitized_message = re.sub(r"Patient Name:.*\n", "Patient Name: [REDACTED]\n", raw_message)
sanitized_message = re.sub(r"email:.*\n", "email: [REDACTED]\n", sanitized_message)
sanitized_message = re.sub(r"Age:.*\n", "Age: [REDACTED]\n", sanitized_message)


prompt=f"""
Role: You are a hospital patient intake assistant.

Task: summarize the following patient-support message into a short internal note.

Rules:
1. Use the sanitized message provided below to create the internal note.
2. Do not include any personally identifiable information (PII) in the internal note.
3. Keep the internal note concise and focused on the patient's symptoms and medical needs.
Patient-Support Message:
{sanitized_message}
"""

response = get_completion(prompt)
print("Prompt:")
print("-" * 50)
print(prompt)
print("\nResponse:")
print("-" * 50)
print(response)
print("\n")
print("-" * 50)
print("End of Response")
print("\n")