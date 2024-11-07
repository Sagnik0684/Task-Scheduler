import pandas as pd

# Define categories for the Eisenhower Matrix
EISENHOWER_CATEGORIES = {
    'Urgent and Important': 'Do Now',
    'Not Urgent but Important': 'Plan',
    'Urgent but Not Important': 'Delegate',
    'Not Urgent and Not Important': 'Eliminate'
}

def categorize_task(importance, urgency):
    """Categorize a task based on importance and urgency."""
    if importance == "Important" and urgency == "Urgent":
        return EISENHOWER_CATEGORIES['Urgent and Important']
    elif importance == "Important" and urgency == "Not Urgent":
        return EISENHOWER_CATEGORIES['Not Urgent but Important']
    elif importance == "Not Important" and urgency == "Urgent":
        return EISENHOWER_CATEGORIES['Urgent but Not Important']
    else:
        return EISENHOWER_CATEGORIES['Not Urgent and Not Important']

def load_tasks(file_path):
    """Load tasks from a CSV file."""
    try:
        tasks_df = pd.read_csv(file_path)
    except FileNotFoundError:
        tasks_df = pd.DataFrame(columns=[
            "Task Name", "Description", "Time Required (hrs)",
            "Priority", "Importance", "Urgency", "Category"
        ])
    return tasks_df

def save_task(file_path, task):
    """Save a new task to the CSV file."""
    tasks_df = load_tasks(file_path)
    new_task_df = pd.DataFrame([task])  # Convert the task dictionary to a DataFrame
    tasks_df = pd.concat([tasks_df, new_task_df], ignore_index=True)  # Concatenate to existing tasks
    tasks_df.to_csv(file_path, index=False)