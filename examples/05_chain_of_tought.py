import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

prompt = """
I am travelling to Delhi next week. Your are going to be my assistant.
I will ask you to do some tasks for me. You will do the task and then wait for my next instruction.
Task 1: What is the weather forecast for Delhi for next week?
Task 2: What are some popular tourist attractions in Delhi?
Task 3: Can you recommend some good restaurants in Delhi?
Task 4: What are the best hotels to stay in Delhi?
"""

response = get_completion(prompt)
print(response)