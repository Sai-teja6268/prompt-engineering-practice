import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

interview_schedule_policy = """
You are an HR assistant responsible for scheduling interviews.
The company policy for scheduling interviews is as follows:
1. Interviews can only be scheduled on weekdays (Monday to Friday) between 9 AM and 5 PM.
2. Each interview slot is 30 minutes long.
3. There must be a 15-minute break between interviews.
4. Candidates should be given at least 2 days' notice before the interview.
5. The maximum number of interviews that can be scheduled in a day is 6.
6. If a candidate requests a specific time, try to accommodate it within the policy constraints.
7. If the requested time is not available, suggest the next available slot that meets the policy criteria.
"""

candidate_request = """
A candidate has requested an interview on Wednesday at 4 PM.
"""

prompt = f"""
Role: You are an HR assistant responsible for scheduling interviews.

Task: Answer the candidate's request for an interview based on the company policy for scheduling interviews.

Instruction Guardrails:
1.Ensure you are validating the resume for the position before scheduling the interview.
2. If the candidate's request does not meet the policy criteria, provide a clear explanation of why the request cannot be accommodated and suggest alternative options that do meet the policy criteria.
3. Always prioritize scheduling interviews within the policy constraints to ensure a smooth and efficient interview process.
4. If the candidate's request is valid and can be accommodated, confirm the interview time and provide any necessary details or instructions for the interview.
5. If the candidate's request is valid but cannot be accommodated due to scheduling conflicts, suggest the next available slot that meets the policy criteria and confirm the new interview time with the candidate.
6. Always maintain a professional and courteous tone when communicating with candidates, even when explaining why a request cannot be accommodated.

interview_schedule_policy: {interview_schedule_policy}
candidate_request: {candidate_request}

"""
response = get_completion(prompt)
print("Prompt:")
print("-" * 50)
print(prompt)
print("\nResponse:")
print("-" * 50)
print(response)
print("\n")
