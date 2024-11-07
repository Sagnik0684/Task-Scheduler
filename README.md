Task Scheduler with Eisenhower Matrix

This is a task scheduling application built with Streamlit and Python, designed to help users organize tasks according to their priority and urgency using the Eisenhower Matrix. Tasks can be added with details like time required, priority, importance, and urgency. The application categorizes tasks into four categories based on the Eisenhower Matrix:
	•	Do Now: Urgent and Important
	•	Plan: Not Urgent but Important
	•	Delegate: Urgent but Not Important
	•	Eliminate: Not Urgent and Not Important

Folder Structure
task_scheduler_app/
├── streamlitapp.py            # Main Streamlit application
├── requirements.txt           # Dependencies for the project
├── README.md                  # Documentation
├── data/                      # Folder for storing data files
│   └── tasks.csv              # CSV file for storing tasks
└── utils/                     # Folder for utility functions
    └── task_utils.py          # Task categorization and sorting functions

Features

	•	Task Input: Enter tasks with details like name, description, time required, priority, importance, and urgency.
	•	Eisenhower Matrix Categorization: Automatically categorizes tasks based on their importance and urgency.
	•	Persistence: Stores tasks in a CSV file (tasks.csv) for persistence across sessions.

Requirements

	•	Python 3.8+
	•	Pandas
	•	Streamlit

Installation and Setup

	1.	Clone the Repository
Clone this repository or download it as a ZIP file.
git clone https://github.com/Sagnik0684/Task_Scheduler.git
cd Task_Scheduler


	2.	Set Up a Virtual Environment (Optional but Recommended)
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows

  3.	Install Dependencies
Install the required Python packages using requirements.txt:

pip install -r requirements.txt

4.	Create tasks.csv File
In the data/ folder, create a tasks.csv file with only the header row to start:

Task Name,Description,Time Required (hrs),Priority,Importance,Urgency,Category


Running the Application

To run the application, use the following command:
streamlit run streamlitapp.py

This will launch the Streamlit server and open the application in your default web browser.

Usage

	1.	Open the App: After running the streamlit command, the app should open in your default browser.
	2.	Add Tasks: Use the sidebar to input task details:
	•	Task Name: Name of the task.
	•	Description: Optional description of the task.
	•	Time Required (hrs): Estimated time needed to complete the task.
	•	Priority: High, Medium, or Low.
	•	Importance: Choose between “Important” and “Not Important”.
	•	Urgency: Choose between “Urgent” and “Not Urgent”.
	3.	Save Task: Click “Add Task” to save the task. It will appear in the main section of the app, categorized based on the Eisenhower Matrix.
	4.	View Tasks: Tasks will be sorted by priority and time required.

Notes

	•	Tasks are saved to data/tasks.csv so they will persist between sessions.
	•	You can modify or delete tasks by directly editing the tasks.csv file if needed.




