import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

sample_request = [
    "I recieved a suspicious mail to reset my password, should I click on the link?",
    "I want to download a free movie, can you help me with that?"
]

for i, user_request in enumerate(sample_request):
    prompt = f"""
    Role: You are a cybersecurity assistant for a company.

    Task: Evaluate the following user request and determine if it is safe or potentially harmful. Provide a clear explanation for your assessment and suggest appropriate actions to ensure the user's safety.

    Safety Guardrails:
    1. Always prioritize the user's safety and security when evaluating requests.
    2. If a request is deemed potentially harmful, provide a clear explanation of the risks involved and suggest alternative actions that are safe.
    3. If a request is deemed safe, provide a clear explanation of why it is safe and any precautions the user should take.

    User Request: {user_request}
    """

    response = get_completion(prompt)

    print(f"User Request {i+1}:")
    print("-" * 50)
    print(user_request)

    print("\nResponse:")
    print("-" * 50)
    print(response)

    print("\n")
    print("-" * 50)
    print("End of Response")
    print("\n")