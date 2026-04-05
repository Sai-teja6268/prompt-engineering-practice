"""
Output Validation Guardrails
use case: military field status report assistant that must follow the output validation guardrails.
"""
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

field_report = """
1. Location: Grid 45X, Sector 7
2. Status: All clear, no enemy activity detected.
3. Resources: 3 tanks, 5 infantry units, and 2 helicopters available.
4. Communication: Radio communication is stable, no issues reported.
5. Weather: Clear skies, visibility is good.
6. Morale: Troops are in high spirits, no signs of fatigue or distress.
7. Intelligence: No new intelligence reports, but ongoing surveillance is active.
"""

prompt = f"""
Role: You are a military field status report assistant.

Task: Create a concise and accurate field status report based on the following information. 
Ensure that the report is clear, well-structured, and follows the output validation guardrails. 

Required Format:
Field Status Report:
- Location: 
- Status: 
- Resources: 
- Communication: 
- Weather:
- Morale:
- Intelligence:

Rules:
1. Use the exact headings above provided.
2. keep each section short and concise, ideally one sentence per section.
3. Do not add extra headings.
4. Ensure that the information provided in each section is accurate and relevant to the field status.
Field Report Information: {field_report}
"""
response = get_completion(prompt)

print("Prompt:")
print("-" * 50)
print(prompt)
print("\nResponse:")
print("-" * 50)
print(response)
print("\n")
print("-" * 50)
print("End of Response")
print("\n")

