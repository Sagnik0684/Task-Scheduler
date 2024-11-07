import streamlit as st
import pandas as pd
from utils.task_utils import categorize_task, load_tasks, save_task
import os

# Define file path for CSV
TASK_FILE = "data/tasks.csv"

# Main application function
def main():
    st.title("Task Scheduler with Eisenhower Matrix")

    st.sidebar.header("Add Task")
    task_name = st.sidebar.text_input("Task Name")
    task_description = st.sidebar.text_area("Task Description")
    time_required = st.sidebar.number_input("Time Required (hours)", min_value=1)
    priority = st.sidebar.selectbox("Priority", ["High", "Medium", "Low"])
    importance = st.sidebar.selectbox("Importance", ["Important", "Not Important"])
    urgency = st.sidebar.selectbox("Urgency", ["Urgent", "Not Urgent"])

    if st.sidebar.button("Add Task"):
        # Create a new task dictionary
        new_task = {
            "Task Name": task_name,
            "Description": task_description,
            "Time Required (hrs)": time_required,
            "Priority": priority,
            "Importance": importance,
            "Urgency": urgency,
            "Category": categorize_task(importance, urgency)
        }
        # Save task to CSV file
        save_task(TASK_FILE, new_task)
        st.sidebar.success(f"Task '{task_name}' added successfully!")

    display_tasks()

# Function to display tasks from CSV file
def display_tasks():
    tasks_df = load_tasks(TASK_FILE)
    if not tasks_df.empty:
        st.subheader("Scheduled Tasks")
        # Sort by priority and time required
        priority_order = {"High": 1, "Medium": 2, "Low": 3}
        tasks_df["Priority Rank"] = tasks_df["Priority"].map(priority_order)
        tasks_df = tasks_df.sort_values(by=["Priority Rank", "Time Required (hrs)"])
        st.table(tasks_df.drop(columns="Priority Rank"))
    else:
        st.write("No tasks added yet.")

if __name__ == "__main__":
    main()
