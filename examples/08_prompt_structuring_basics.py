import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

prompt = """
Role: You are a begineer friendly fitness

Task: Create a workout plan for a beginner who wants to lose weight and tone their body.
The workout plan should include exercises, sets, reps, and rest periods. 

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

response = get_completion(prompt)

print("Prompt:")
print("-" * 50)
print(prompt)

print("\nResponse:")
print("-" * 50)
print(response)