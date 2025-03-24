from datetime import datetime, timedelta

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
        return f"Task ID: {self.task_id}\nName: {self.name}\nDescription: {self.description}\nPriority: {self.priority}\nDeadline: {self.deadline.strftime('%Y-%m-%d %H:%M:%S')}\nCreated At: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}\nCompleted: {self.completed}"

    def mark_as_completed(self):
        self.completed = True
        print(f"Task {self.task_id} marked as completed.")

    def time_left(self):
        return self.deadline - datetime.now()

class TaskManager:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task: Task):
        self.tasks[task.task_id] = task
        print(f"Task '{task.name}' added successfully!")

    def remove_task(self, task_id: int):
        if task_id in self.tasks:
            del self.tasks[task_id]
            print(f"Task ID {task_id} removed successfully!")
        else:
            print(f"Task ID {task_id} not found.")

    def show_all_tasks(self):
        if self.tasks:
            for task in self.tasks.values():
                print(task)
                print("-" * 50)
        else:
            print("No tasks available.")

    def get_task_by_id(self, task_id: int):
        return self.tasks.get(task_id, None)

    def filter_by_priority(self, priority: str):
        filtered_tasks = [task for task in self.tasks.values() if task.priority == priority]
        if filtered_tasks:
            for task in filtered_tasks:
                print(task)
                print("-" * 50)
        else:
            print(f"No tasks found with priority: {priority}")

    def sort_by_deadline(self):
        sorted_tasks = sorted(self.tasks.values(), key=lambda x: x.deadline)
        for task in sorted_tasks:
            print(task)
            print("-" * 50)

    def show_incomplete_tasks(self):
        incomplete_tasks = [task for task in self.tasks.values() if not task.completed]
        if incomplete_tasks:
            for task in incomplete_tasks:
                print(task)
                print("-" * 50)
        else:
            print("No incomplete tasks.")


if __name__ == "__main__":
    task_manager = TaskManager()

    task1 = Task(1, "Complete Python assignment", "Finish coding and submit.", Priority.HIGH, datetime.now() + timedelta(days=2))
    task2 = Task(2, "Read book", "Read 'Python Crash Course'.", Priority.MEDIUM, datetime.now() + timedelta(days=5))
    task3 = Task(3, "Buy groceries", "Get vegetables, fruits, and snacks.", Priority.LOW, datetime.now() + timedelta(days=1))

    task_manager.add_task(task1)
    task_manager.add_task(task2)
    task_manager.add_task(task3)
    
    print("\nAll tasks:")
    task_manager.show_all_tasks()

    print("\nFiltered by Medium priority:")
    task_manager.filter_by_priority(Priority.MEDIUM)

    print("\nTasks sorted by deadline:")
    task_manager.sort_by_deadline()

    print("\nMarking Task 1 as completed:")
    task1.mark_as_completed()

    print("\nIncomplete tasks:")
    task_manager.show_incomplete_tasks()

