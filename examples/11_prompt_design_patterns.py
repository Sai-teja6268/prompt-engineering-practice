import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

review_text = """
I recently purchase a waterPurifier from pureit and I am extremely disappointed with the product. 
The water purifier stopped working within a week of purchase and I had to get it repaired.
The customer service was also very poor and they took a long time to respond to my queries. 
I would not recommend this product to anyone.
"""

classification_prompt = """
Classify the sentiment of the following review text as Positive, Negative, or Neutral:
Review Text: {review_text}
"""

extraction_prompt = """
Extract the main issues mentioned in the following review text:
Review Text: {review_text}
"""

rewrite_prompt = """Rewrite the following review text in a more polite and constructive manner:
Review Text: {review_text}
"""

generation_prompt = """
Generate a response to the following review text from the perspective of the company, addressing the customer's concerns and offering a solution:
Review Text: {review_text}
"""

classification_response = get_completion(classification_prompt.format(review_text=review_text))
extraction_response = get_completion(extraction_prompt.format(review_text=review_text))
rewrite_response = get_completion(rewrite_prompt.format(review_text=review_text))
generation_response = get_completion(generation_prompt.format(review_text=review_text))

print("Classification Response:")
print("-" * 50)
print(classification_response)

print("\nExtraction Response:")
print("-" * 50)
print(extraction_response)

print("\nRewrite Response:")
print("-" * 50)
print(rewrite_response)

print("\nGeneration Response:")
print("-" * 50)
print(generation_response)

print("\nReview Text:")
print("-" * 50)
print(review_text)
print("\n")