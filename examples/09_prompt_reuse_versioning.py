import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

topic = "Fitness plan"
time_available = "1hour 30 minutes a day, 5 days a week"
audiance = "Beginners who want to lose weight and tone their body"

prompt_v1 = """
create a {topic} for {audiance} who have {time_available} to dedicate to working out.
The plan should include exercises, sets, reps, and rest periods.
"""

prompt_v2 = """
Role: You are a begineer friendly fitness coach

Task: Create a {topic} for {audiance} who have {time_available} to dedicate to working out.

context: The beginner has access to a gym with basic equipment and can dedicate 30 minutes a day, 5 days a week to working out. 
They have no prior experience with weightlifting or high-intensity workouts.

Constraints: 
- keep the workout plan simple and easy to follow.
- Include a mix of cardio and strength training exercises.
- Provide clear instructions for each exercise, including proper form and technique.
- Include a warm-up and cool-down routine to prevent injury and promote recovery.
- Suggest modifications or alternatives for exercises that may be too challenging for a beginner.
- Provide tips for staying motivated and consistent with the workout plan.
- Provide a proper diet plan to complement the workout routine for weight loss and toning.
- Ensure that the diet plan is balanced and includes a variety of nutrient-dense foods, while also being mindful of calorie intake for weight loss.
- Ensure that the diet plan is followed strictly no cheating allowed.

output format:
1. Workout Plan:
- Warm-up: [exercise name, duration, intensity]
- Day 1: [exercise name, sets, reps, rest period]
- Day 2: [exercise name, sets, reps, rest period
- Day 3: [exercise name, sets, reps, rest period]
- Day 4: [exercise name, sets, reps, rest period]
- Day 5: [exercise name, sets, reps, rest period]
- Day 6: [exercise name, sets, reps, rest period]
- Day 7: [exercise name, sets, reps, rest period]
- Cool-down: [exercise name, duration, intensity]
2. Diet Plan:
- Breakfast: [meal name, ingredients, portion size]
- Lunch: [meal name, ingredients, portion size]
- Dinner: [meal name, ingredients, portion size]
- Snacks: [meal name, ingredients, portion size]
3. Tips for Motivation and Consistency:
- [tip 1]
- [tip 2]
- [tip 3]
"""


response_v1 = get_completion(prompt_v1.format(topic=topic, audiance=audiance, time_available=time_available))
response_v2 = get_completion(prompt_v2.format(topic=topic, audiance=audiance, time_available=time_available))
print("Prompt Version 1:")
print("-" * 50)
print(prompt_v1.format(topic=topic, audiance=audiance, time_available=time_available))
print("\nResponse Version 1:")
print("-" * 50)
print(response_v1)
print("\nPrompt Version 2:")
print("-" * 50)
print(prompt_v2.format(topic=topic, audiance=audiance, time_available=time_available))
print("\nResponse Version 2:")
print("-" * 50)
print(response_v2)
