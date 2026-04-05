import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

prompt = """ Rewrite the following sentence in a more formal tone:
"hey, what's up? how are you doing? I hope everything is going well.
I just wanted to check in and see if you have any plans for the weekend?"
"""

response = get_completion(prompt)
print(response)
