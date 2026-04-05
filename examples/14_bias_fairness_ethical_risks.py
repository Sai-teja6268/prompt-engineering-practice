"""
escalation guardrail.py
use case: Loan approval assistant that must evaluate loan applications
while adhering to ethical guidelines to prevent bias and ensure fairness in the decision-making process.
"""



import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

Candidate_profile = """
Income: $85,000 annually, verified through payslips and bank statements
Credit Score: 720
Debt-to-Income Ratio: 28%
Repayment History: No defaults; minor delays (≤10 days) on two occasions in past 3 years
"""


prompt = f"""
Role: You are a hiring manager for a tech company.

Task: Generate a structured summary of a loan applicant’s 
financial profile to support decision-making by human loan officers.

Fairness and Ethical Guidelines:
1. Evaluate the candidate's financial profile based solely on objective criteria such as income,
credit score, debt-to-income ratio, and repayment history.
2. Avoid any consideration of protected characteristics such as race, gender, age,or ethnicity.
3. Ensure that the summary is concise, clear, and focused on relevant financial
information that is pertinent to the loan approval process.
Candidate Profile: {Candidate_profile}
"""

response = get_completion(prompt)

print(response)