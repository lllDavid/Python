from datetime import datetime

class Priority:
    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'

class Task:
    def __init__(self, task_id, name, description, priority, deadline):
        self.task_id = task_id
        self.name = name
        self.description = description
        self.priority = priority
        self.deadline = deadline
        self.created_at = datetime.now()
        self.completed = False

    def __str__(self):
        return (f"Task ID: {self.task_id}\n"
                f"Name: {self.name}\n"
                f"Description: {self.description}\n"
                f"Priority: {self.priority}\n"
                f"Deadline: {self.deadline.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"Created At: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"Completed: {self.completed}")

    def mark_as_completed(self):
        self.completed = True
        print(f"Task {self.task_id} marked as completed.")

    def time_left(self):
        return self.deadline - datetime.now()
