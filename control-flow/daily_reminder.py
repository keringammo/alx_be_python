# daily_reminder.py

# Prompt user for task details
task = input("Enter your task for today: ")
priority = input("Enter the task priority (high, medium, low): ").lower()
time_bound = input("Is this task time-sensitive? (yes or no): ").lower()

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

# Display the customized reminder
print(reminder)