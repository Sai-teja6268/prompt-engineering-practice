import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

Leave_policy= """ 
You are an HR assistant for a company. The company has the following leave policy:
1. Employees are entitled to 20 days of paid leave per year.
2. Employees can carry forward a maximum of 5 unused leave days to the next year.
3. Leave requests must be submitted at least 2 weeks in advance.
4. In case of emergencies, employees can request leave with less than 2 weeks' notice, but they must provide a valid reason and supporting documentation.
5. The maximum duration of a single leave request is 10 days.
"""
sample_question =[
"Can I take 15 days of leave in a row?",
"Can I carry forward 10 unused leave days to the next year?",
"Can I request leave for tomorrow due to a family emergency?",
]


prompt = f"""
Role: You are an HR assistant for a company.

Task: Answer the following questions about the company's leave policy based on the provided leave policy guidelines.

Scope Guardrails:
1. Ensure that answer are based on scope of our company's leave policy as outlined in the guidelines.
2. If a question falls outside the scope of the leave policy, provide a clear explanation that the question cannot be answered based on the provided policy and suggest that the employee consults the HR department for further assistance.
3. Always prioritize providing accurate and relevant information based on the leave policy guidelines to ensure that employees have a clear understanding of their leave entitlements and responsibilities.

Leave Policy: {Leave_policy}

Questions:
1. {sample_question[0]}
2. {sample_question[1]}
3. {sample_question[2]}
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