import streamlit as st
import json
from utils.planner import generate_plan, save_plan_to_file


def load_data():
    with open("data/roadmap_data.json", "r") as file:
        return json.load(file)


def main():
    st.title("Learning Roadmap Generator")

    # User input
    goal = st.selectbox("Choose your career goal", ["cloud engineer", "data scientist", "ai developer"])
    level = st.selectbox("Choose your skill level", ["beginner", "intermediate", "advanced"])
    hours = st.number_input("How many hours can you study per week?", min_value=1, max_value=40)

    if st.button("Generate Learning Plan"):
        data = load_data()
        if goal not in data or level not in data[goal]:
            st.error("Invalid input! Please check your goal and skill level.")
        else:
            topics = data[goal][level]
            # Generate the learning plan and save to file
            plan_text = generate_plan(topics, hours)
            save_plan_to_file(plan_text)

            # Show plan in the app
            st.text(plan_text)

            # Provide file download
            st.download_button(
                label="Download Learning Plan",
                data=plan_text,
                file_name="learning_plan.txt",
                mime="text/plain"
            )


if __name__ == "__main__":
    main()