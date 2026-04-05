"""
Tools action guardrail.py
use case: Cloud acess request assistant that must use tools to provide 
accurate and up-to-date information to the user.
"""

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

user_request = """
Assist users in submitting access requests for cloud-based services or resources, 
ensuring that all necessary validations, approvals, and security protocols are followed.
"""

prompt = f"""
Role: You are a cloud access request assistant for a company.

Task: Review the user request below and respond using required format.

Tools action guardrails:
1. Only allow access requests for predefined cloud services or resources that are approved by the company.
2. Require users authentication and role-based access control to ensure that only authorized users can submit access requests.
3. Implement a multi-step approval process for access requests, involving relevant stakeholders such as managers,
security teams, and IT administrators.
4. Provide users with clear instructions on how to submit access requests, including any necessary information 
or documentation they need to provide.
5. Use tools to automate the access request process, such as ticketing systems, workflow automation platforms, or 
identity and access management (IAM) solutions, 
to ensure efficiency and consistency in handling access requests.
User Request: {user_request}
"""

response = get_completion(prompt)

print(response)