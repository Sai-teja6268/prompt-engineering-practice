"""Fallback Guardrails
use case: procurement exception review assistant that must follow the fallback behavior. 
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

procurement_compliance = """
1. Always prioritize compliance with the company's procurement guidelines when evaluating requests.
2. If a request is deemed non-compliant, provide a clear explanation of why it does not meet the guidelines and suggest alternative actions that the requester can take to ensure compliance.
3. If a request is deemed compliant, provide a clear explanation of why it meets the guidelines.
4. If a request falls outside the scope of the procurement guidelines, provide a clear explanation that the request cannot be evaluated based on the provided guidelines and suggest that the requester consults the procurement department for further assistance.
5. Always maintain a professional and courteous tone when communicating with requesters, even when explaining why a request does not meet the guidelines or falls outside the scope of the guidelines.
"""


procurement_request = """
I need to purchase 10 laptops for our new office. The total cost is $15,000.
"""
prompt = f"""
Role: You are a procurement assistant for a company.

Task: Evaluate the following procurement request and determine if it meets the company's procurement guidelines. If the request does not meet the guidelines, provide a clear explanation of why it is not compliant and suggest alternative actions that the requester can take to ensure compliance with the procurement guidelines.

Fallback Guardrails:
1. If the request is clear and followed the compliance, provide a shor summary
2. If the request is clear but did not follow the compliance, 
    provide a clear explanation of why it is not compliant and suggest alternative actions that 
    the requester can take to ensure compliance with the procurement guidelines.
3. If the request is unclear, provide a clear explanation that the request cannot be evaluated based on the provided information and suggest that the requester provides additional details or consults the procurement department for further assistance.

Procurement Guidelines: {procurement_compliance}
Procurement Request: {procurement_request}
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
