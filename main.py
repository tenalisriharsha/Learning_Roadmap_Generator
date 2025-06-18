import json
from utils.planner import generate_plan


def load_data():
    with open("data/roadmap_data.json", "r") as file:
        return json.load(file)


def main():
    print("🎯 Welcome to the Learning Roadmap Generator\n")

    goal = input("Enter your career goal (e.g., cloud engineer, data scientist, ai developer): ").strip().lower()
    level = input("Enter your current skill level (beginner/intermediate/advanced): ").strip().lower()
    try:
        hours = int(input("How many hours can you study per week?: ").strip())
    except ValueError:
        print("Please enter a valid number for hours.")
        return

    data = load_data()

    if goal not in data:
        print(f"❌ No roadmap found for the career goal: {goal}")
        return

    if level not in data[goal]:
        print(f"❌ No data for skill level: {level}")
        return

    topics = data[goal][level]
    generate_plan(topics, hours)


if __name__ == "__main__":
    main()
