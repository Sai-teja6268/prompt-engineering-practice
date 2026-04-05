"""
Input Gaurdrails
use case: emergency hot line intake assistant 
"""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

callerId = "12321"
emergency_type = "fire"
location = "123 Main St, Springfield"
severity = "urgent"

if not callerId.strip():
    print("Error: Caller ID is missing.")
if not emergency_type.strip():
    print("Error: Emergency type is missing.")
if not location.strip():
    print("Error: Location is missing.")
elif severity.lower() not in ["low", "medium", "high"]:
    print("Error: Severity level is invalid. Please provide one of the following: low, medium, high, urgent.")    
        
prompt=f"""
Role: You are an emergency hotline intake assistant for a city.

Task: Evaluate the following emergency call information and determine if it is complete and valid.
If any information is missing or invalid, provide a clear explanation of what is missing or invalid 
and suggest how the caller can provide the necessary information.

Rules:
1. use always the input details to evaluate the call information.
2. keep the conversation simple and concise.
3. provide clear instructions to the caller on how to provide any missing or invalid information.
Emergency Call Information:
Caller ID: {callerId}
Emergency Type: {emergency_type}
Location: {location}
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