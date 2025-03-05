#Avery bowman, To do list

TODO_FILE = "to do list/todo_list.txt"
def load_tasks():

    #Load tasks from the to-do file.
    try:
        with open(TODO_FILE, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    #Save tasks to the to-do file.
    with open(TODO_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def display_tasks(tasks):

    #Display the to-do list.
    if not tasks:
        print("No tasks in the to-do list.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(task):
    #Add a new task to the list.
    tasks = load_tasks()
    tasks.append("[ ] " + task)  #Mark new tasks as incomplete
    save_tasks(tasks)
    print("Task added!")

    #Mark as completed (not done yet)
def completed_task()
    tasks = load_tasks()


def delete_task(index):
    #Delete a task from the list.
    tasks = load_tasks()
    if 1 <= index <= len(tasks):
        tasks.pop(index - 1)
        save_tasks(tasks)
        print("Task deleted!")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\nTo-Do List Manager")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark as done")
        print("4. Delete task")
        print("5. Exit")
       
        choice = input("Enter your choice: ")
       
        if choice == "1":
            display_tasks(load_tasks())
        elif choice == "2":
            task = input("Enter the task: ")
            #needs to be completed
        elif choice == "3":
            display_tasks(load_tasks())
            index = int(input("Select the task to mark as completed: "))

        elif choice == "4":
            display_tasks(load_tasks())
            index = int(input("Enter task number to delete: "))
            delete_task(index)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()