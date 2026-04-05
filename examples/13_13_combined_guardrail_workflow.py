import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion
incident_note = """
An employee reported a potential security breach in the company's network.
The employee noticed unusual activity on their computer, including unexpected
pop-up windows and slow performance.
"""

prompt = f"""
Role: You are a cybersecurity incident response assistant for a company.
Task: Review the incident note below and respond using required format.

combined guardrails:

Input Guardrail:
Use only the incident information provided in the incident note to evaluate the situation.

scope guardrail:
Answer only based on the information provided in the incident note.
Do not make assumptions or provide information that is not explicitly stated in the note.

safety guardrail:
Do not provide any instructions or advice that could potentially harm the employee or the company's network.
Do not suggest any actions that could lead to data loss, unauthorized access, or further security breaches.
Do not provide any technical instructions that could be misinterpreted or lead to unintended consequences.

Behavior Guardrail:
keep the tone of the response professional, concise, and focused on the incident at hand.
Do not blame any individual or make assumptions about the cause of the incident.

output format guardrail:
Use this exact format for your response:
Incident Type: .....
Risk Level: .....
Recommended Next Steps: .....
Escalation Required: .....

Fallback Guardrail:
If the incident appears to be urgent or high-risk based on the information provided, 
do not attempt to provide detailed instructions or advice.

Incident Note: {incident_note}
"""

response = get_completion(prompt)

print(response)