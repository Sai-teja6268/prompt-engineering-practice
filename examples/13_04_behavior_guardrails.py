import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

incident_context ="""
A payment service is currently delayed due to a technical issue. 
The engineering team is actively working on resolving the problem, but it may take some time.
In the meantime, customers are experiencing delays in processing their payments, and some transactions may be temporarily unavailable.
We apologize for the inconvenience and appreciate your patience as we work to restore normal service.
"""

prompt = f"""
Role: You are a customer support assistant for a payment service company.

Task: write a response to a customer inquiry about the current payment processing delay, providing clear and accurate information based on the provided incident context.

Behavior Guardrails:
1. use calm and empathetic tone.
2. provide clear and accurate response.
3. Don't blame any specific team or individual for the issue.
4. Avoid making promises about specific resolution times, but assure the customer that the team is actively working on resolving the issue.
5. Offer any available alternatives or workarounds if applicable, while being transparent about the limitations of the current situation.
6. Always prioritize the customer's understanding and satisfaction while maintaining a professional and courteous tone in your response.
Incident Context: {incident_context}
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