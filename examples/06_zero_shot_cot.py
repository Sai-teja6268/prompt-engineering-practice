import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion
prompt = """ 
A Developer who earns 8 Lakhs per annum has fixed monthly expenses of 25,000. 
He wants to save enough money to buy a laptop costing 1.5 Lakhs.
Solve this step by step and tell:
1. Monthly savings
2. How many months it will take
3. One practical suggestion to reach the goal faster
4. Suggest some alternatives to earn apart from job to reach the goal faster
"""
response = get_completion(prompt)
print(response)