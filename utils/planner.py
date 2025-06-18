def save_plan_to_file(plan_text, filename="learning_plan.txt"):
    with open(filename, "w") as file:
        file.write(plan_text)
    print(f"\n✅ Your learning plan has been saved to {filename}.")


def generate_plan(topics, hours_per_week):
    print(f"\n📚 Generating a weekly plan based on {hours_per_week} hrs/week...\n")
    plan_text = ""
    days_in_week = 5  # You can change this if you want weekends included
    daily_study_time = hours_per_week / days_in_week

    for week, item in enumerate(topics, 1):
        topic = item.get("topic", "Unknown Topic")
        resources = item.get("resources", [])
        tools = item.get("tools", [])

        plan_text += f"📅 Week {week}: {topic}\n"
        plan_text += f"🕒 Suggested Study Time for the Week: {hours_per_week} hours\n"
        plan_text += f"🗓 Daily Study Time: {daily_study_time:.2f} hours per day\n"

        for day in range(1, days_in_week + 1):
            plan_text += f"   Day {day}: Study {topic} for {daily_study_time:.2f} hours\n"

        plan_text += "🔗 Recommended Resources:\n"
        for res in resources:
            plan_text += f"   - {res}\n"

        plan_text += "🧰 Suggested Tools/Platforms:\n"
        for tool in tools:
            plan_text += f"   - {tool}\n"

        plan_text += "-" * 50 + "\n"

    return plan_text  # Ensure it returns the plan_text