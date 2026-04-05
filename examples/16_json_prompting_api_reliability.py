import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion
return_request = """
orderId: 12345
productId: 67890
reason: The product is defective and does not work as advertised.
customerRequest: I want to return this product and get a refund.
"""

prompt = f"""
Role: You are a customer service assistant for an online retail company.

Task: Review the return request information provided below and evaluate the reliability of the
customer's claim.

API Reliability rules:
1. Return only vlaid JSON format response.
2. Do not include any information that is not explicitly stated in the return request.
3. Do not make assumptions about the customer's claim or the product's condition.
4. Use exactly these keys:
   "status", "category", "priority", "next_action"
5. Use only one of these values for "status":
   "approved", "needs_review", "rejected"
6. Use only one of these values for "category":
   "replacement", "refund", "technical_issue"
7. Use only one of these values for "priority":
   "low", "medium", "high"
8. Keep "next_action" short and operational.

return this exact json format:
{{
  "status": "approved | needs_review | rejected",
  "category": "replacement | refund | technical_issue",
  "priority": "low | medium | high",
  "next_action": "string"
}}

Return Request Information: {return_request}
"""

response = get_completion(prompt)

print(response)