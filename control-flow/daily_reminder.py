# daily_reminder.py

# Prompt user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process task based on priority
match priority:
    case "high":
        reminder = f"🔴 High priority task: {task}."
    case "medium":
        reminder = f"🟡 Medium priority task: {task}."
    case "low":
        reminder = f"🟢 Low priority task: {task}."
    case _:
        reminder = f"⚪ Task: {task} (priority not specified)."

# Modify message if time-bound
if time_bound == "yes":
    reminder += " This task requires immediate attention today!"

# Use a loop to emphasize the reminder (example: repeat 3 times)
for i in range(3):
    print(reminder)
