import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

prompt = """ Identify the language of the following sentence:

example: 
Input:"Je suis fatigué"
Output:French
Input:"అవును, నువ్వు నన్ను అడిగావు"
Output:
"""
response = get_completion(prompt)
print(response)