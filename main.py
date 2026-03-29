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

# Main Program
add_task()
view_tasks()
mark_done()
view_tasks()