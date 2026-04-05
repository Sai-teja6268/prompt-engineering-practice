import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# prompt=""" Translate the following English sentences into French.

# English: "Hello, how are you?"
# French: "Bonjour, comment ça va?"

# English: "I am learning prompt engineering."
# French: "J'apprends l'ingénierie des invites."

# English: "This book is very interesting."
# French: "Ce livre est très intéressant."

# English: "What time is it?"
# French:

# """
prompt = """ Classify the following sentences into positive, negative, or neutral sentiment.
Sentence: I love this movie!
Sentiment: Positive
Sentence: This restaurant is terrible.
Sentiment:Negative
Sentence: The weather is okay today.
Sentiment: Neutral
Sentence: I am so excited for the concert tonight!
Sentiment:
"""
response = get_completion(prompt)
print(response)