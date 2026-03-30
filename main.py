import os
import json


tasks = []

def add_task():
    while True:
        new_task = input("Please enter the task you want to add: ")
        tasks.append({"task": new_task, "done": False})
        print(f"Added task: {new_task}")
        
        progress = input("Would you like to add another? (Y/N): ")
        if progress.lower() == "n":
            print("Finished adding tasks.")
            break
        elif progress.lower() != "y":
            print("Please enter a proper answer! (Y/N)")

def view_tasks():
    if not tasks:
        print("No tasks Yet!")
        return
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "❌"
        print(f"{i}. {task['task']} [{status}]")

def mark_done():
    if not tasks:
        print("No tasks to mark done!")
        return
    
    task_num = int(input("Please select the task you would like to mark done: "))
    
    if 1 <= task_num <= len(tasks):
        tasks[task_num - 1]["done"] = True
        print(f"Task '{tasks[task_num - 1]['task']}' marked as done!")
    else:
        print("Invalid task number.")

def delete_task():
    if not tasks:
        print("No tasks to delete!")
        return
    view_tasks()
    task_num = int(input("Enter which task you would like to remove."))
    if 1 <= task_num <= len(tasks):
        removed = tasks.pop(task_num - 1)
        print(f"Deleted task: {removed['task']}")
    else:
        print("invalid task number!")

def write_file():
    with open ('tasks.json','w', encoding = 'utf-8') as f:
        json.dump(tasks, f, ensure_ascii = False, indent=4 )
    print("Saved to file!")

def load_file():
    global tasks
    try:
        with open('tasks.json', 'r', encoding='utf-8') as f:
            tasks = json.load(f)
        print("Loaded tasks from file!")
    except FileNotFoundError:
        tasks = []
        print("No saved file found. Starting fresh.")

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


# Main Program

# Main Program
load_file()

while True:
    print("\n--- TODO MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Done")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        cls()
        add_task()
        write_file()

    elif choice == "2":
        cls()
        view_tasks()

    elif choice == "3":
        cls()
        view_tasks()
        mark_done()
        write_file()

    elif choice == "4":
        cls()
        delete_task()
        write_file()

    elif choice == "5":
        cls()
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")

