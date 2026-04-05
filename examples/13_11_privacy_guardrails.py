import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

customer_note = """
Customer Name: John Doe
Customer Email: Doe@gmail.com
Customer Phone: 123-456-7890
Customer Address: 123 Main St, Springfield, USA
Customer Credit Card Number: 4111 1111 1111 1111
Customer Social Security Number: 123-45-6789
"""

prompt = f"""
Role: You are a customer service assistant for an online retail company.

Task: Create a short internal note summary of the customer information provided below.

Privacy Guardrails:
1. Do not repeat the full Customer Credit Card Number.
2. Do not repeat the full Customer Social Security Number.
3. Do not include unnecessary personal information in the summary.
4. Keep the summary concise and focused on relevant information for customer service purposes.

use this exact format:
customer Credit Card number: **** **** **** 1111
customer Social Security Number: ***-**-6789
Customer Information: {customer_note}
"""


response = get_completion(prompt)

print (response)