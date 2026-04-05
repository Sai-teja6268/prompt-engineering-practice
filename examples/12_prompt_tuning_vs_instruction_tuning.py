import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

simple_prompt = """
Explain the difference between prompt engineering, prompt tuning, and instruction tuning in the context of AI language models.

use this format:
1. Prompt Engineering:
2. Prompt Tuning:
3. Instruction Tuning:
4. fine-tuning:
"""

response = get_completion(simple_prompt)

print("Prompt:")
print("-" * 50)
print(simple_prompt)

print("\nResponse:")
print("-" * 50)
print(response)

print("\n")
