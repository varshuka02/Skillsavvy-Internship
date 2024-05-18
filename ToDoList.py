tasks = {}  
completed_tasks = []  

def generate_unique_id():
  """Generates a unique identifier for each task."""
  import uuid
  return str(uuid.uuid4())

def add_task():
  """Prompts user for task details and adds it to the list."""
  description = input("Enter task description: ")
  due_date = input("Enter due date (optional): ")
  task_id = generate_unique_id()
  tasks[task_id] = {"description": description, "due_date": due_date, "completed": False}
  print("Task added successfully!")

def display_tasks(tasks_list):
  """Displays all tasks with details and completion status."""
  for task_id, task in tasks_list.items():
    completion_status = "Completed" if task["completed"] else "Pending"
    print(f"ID: {task_id}, Description: {task['description']}, Due Date: {task['due_date']}, Status: {completion_status}")

def mark_complete():
  """Marks a task as completed and moves it to the completed list."""
  task_id = input("Enter ID of task to mark complete: ")
  if task_id in tasks and not tasks[task_id]["completed"]:
    tasks[task_id]["completed"] = True
    completed_tasks.append(task_id)
    tasks.pop(task_id)  
    print("Task marked complete!")
  else:
    print("Invalid task ID or task already completed!")

def update_task():
  """Updates an existing task's description or due date."""
  task_id = input("Enter ID of task to update: ")
  if task_id in tasks:
    new_description = input("Enter new description (or leave blank): ")
    new_due_date = input("Enter new due date (or leave blank): ")
    if new_description:
      tasks[task_id]["description"] = new_description
    if new_due_date:
      tasks[task_id]["due_date"] = new_due_date
    print("Task updated successfully!")
  else:
    print("Invalid task ID!")

def remove_task():
  """Removes a task from either the to-do or completed list."""
  task_id = input("Enter ID of task to remove: ")
  if task_id in tasks:
    tasks.pop(task_id)
    print("Task removed successfully!")
  elif task_id in completed_tasks:
    completed_tasks.remove(task_id)
    print("Task removed successfully!")
  else:
    print("Invalid task ID!")

def main_menu():
  """Displays the main menu with options for task management."""
  print("\nTo-Do List Application")
  print("1. Add Task")
  print("2. View Tasks")
  print("3. Mark Task Complete")
  print("4. Update Task")
  print("5. Remove Task")
  print("6. Exit")
  choice = input("Enter your choice (1-6): ")
  return choice

while True:
  choice = main_menu()
  if choice == '1':
    add_task()
  elif choice == '2':
    print("\nTo-Do List:")
    display_tasks(tasks)
    print("\nCompleted Tasks:")
    display_tasks({tid: tasks[tid] for tid in completed_tasks}) 
  elif choice == '3':
    mark_complete()
  elif choice == '4':
    update_task()
  elif choice == '5':
    remove_task()
  elif choice == '6':
    print("Exiting application...")
    break
  else:
    print("Invalid choice. Please try again.")
