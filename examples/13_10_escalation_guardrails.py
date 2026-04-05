"""
escalation guardrail.py
use case: An emergency customer distress triage assistant that
must escalate urgent cases instead of providing instructions to the caller.
"""

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

incident_message = """
I am a customer service representative and I need to escalate this urgent case immediately.
my father is having a heart attack and I need help right now.
"""

prompt = f"""
Role: You are an emergency customer distress triage assistant for a city.

Task: Review the message below and respond using required format.

Escalation guardrails:
1. If the message suggests immediate danger, do not handle it like a normal customer service inquiry.
2. In Urgent or Life-threatening situations, do not provide instructions to the caller. 
    Instead, immediately escalate the case to the appropriate emergency response team.
3. Do not provide false reassurance or attempt to diagnose the situation.
4. Do not try to act like a medical professional.
5. keep the answer, short and concise.

Incident Message: {incident_message}
"""

print("Prompt:")
print("-" * 50)
print(prompt)

response = get_completion(prompt)

print("\nResponse:")
print("-" * 50)
print(response)

print("\n")
print("-" * 50)
print("End of Response")
print("\n")
