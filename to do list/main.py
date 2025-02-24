#Avery bowman, To do list

import os

# Define the file name where tasks will be stored
todo_file = "todo_list.txt"

def load_tasks():
    #Load tasks from the file. If the file doesn't exist, return an empty list.
    if not os.path.exists(todo_file):
        return []
    with open(todo_file, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    #Save the list of tasks to the file.
    with open(todo_file, "w") as file:
        file.writelines([task + "\n" for task in tasks])

def view_tasks():
    #Display all tasks in the to-do list.
    tasks = load_tasks()
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("Your To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def add_task():
    #Prompt the user to enter a task and add it to the to-do list.
    task = input("Enter a new task: ").strip()
    if task:  # Ensure the task is not empty
        tasks = load_tasks()
        tasks.append(f"[ ] {task}")  # Add task with incomplete status
        save_tasks(tasks)
        print("Task added successfully.")
    else:
        print("Task cannot be empty.")

def mark_task_complete():
    #Mark a task as completed by replacing '[ ]' with '[X]'.
    tasks = load_tasks()
    if not tasks:
        print("No tasks to mark as complete.")
        return
    
    view_tasks()
    try:
        task_num = int(input("Enter the number of the task to mark as complete: ")) - 1
        if 0 <= task_num < len(tasks) and tasks[task_num].startswith("[ ]"):
            tasks[task_num] = tasks[task_num].replace("[ ]", "[X]", 1)  # Mark as complete
            save_tasks(tasks)
            print("Task marked as complete.")
        else:
            print("Invalid task number or task already completed.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    #Delete a task from the to-do list.
    tasks = load_tasks()
    if not tasks:
        print("No tasks to delete.")
        return
    
    view_tasks()
    try:
        task_num = int(input("Enter the number of the task to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            del tasks[task_num]  # Remove the selected task
            save_tasks(tasks)
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    #Main loop to interact with the to-do list manager.
    while True:
        print("\nTo-Do List Manager")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose an option: ").strip()
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_task_complete()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

    main()