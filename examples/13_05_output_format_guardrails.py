"""
Title: Output Format Guardrails
useCase: compliance checklist assistant 
the fixed format of the output is a compliance checklist with specific 
items that need to be addressed based on the provided compliance guidelines. 
The checklist should be structured in a clear and organized manner, 
with each item clearly labeled and explained.
The assistant should ensure that the output adheres to the specified format and 
includes all necessary information to effectively communicate the compliance requirements to the user.
"""



import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion


compliance_guidelines = """
Compliance Checklist:
1. Data Privacy: Ensure that all personal data is collected, processed, and stored in accordance with applicable data protection laws and regulations. This includes obtaining proper consent from individuals before collecting their data and implementing appropriate security measures to protect the data from unauthorized access or breaches.
2. Accessibility: Ensure that all digital content and services are accessible to individuals with disabilities, in compliance with relevant accessibility standards and guidelines. This includes providing alternative text for images, ensuring proper color contrast, and making sure that all interactive elements are navigable using assistive technologies.
3. Compliance with Regulatory Requirements: Ensure that all business practices and operations comply with relevant regulatory requirements, such as industry-specific regulations, financial reporting standards, and environmental regulations. This includes conducting regular audits and assessments to identify and address any potential compliance issues.
4. Employee Training and Awareness: Ensure that all employees are trained on compliance requirements and understand their
responsibilities in maintaining compliance. This includes providing regular training sessions, creating awareness campaigns, and establishing clear policies and procedures for reporting and addressing compliance concerns.
5. Incident Response and Reporting: Ensure that there are established procedures for responding to and reporting compliance incidents. This includes having a clear process for investigating and addressing any potential compliance violations, as well as reporting any incidents to the appropriate authorities or stakeholders as required by law.
"""

prompt = f"""
Role:You are a compliance checklist assistant

Task: Create a compliance checklist based on the provided compliance guidelines.
The checklist should be structured in a clear and organized manner, 
with each item clearly labeled and explained.

Output Format Guardrails:
1. Use exactly these five items in the checklist: 
    Data Privacy, 
    Accessibility, 
    Compliance with Regulatory Requirements, 
    Employee Training and Awareness, 
    and Incident Response and Reporting.
    
2. Each item in the checklist should be clearly labeled and explained in a concise manner.
3. under strength of each time, provide them in a bullet points.
4. keep each bullet poin short and to the point, ideally no more than 10 words.
5. Don't add any extra items or information that is not specified in the compliance guidelines.
Compliance Guidelines: {compliance_guidelines}
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