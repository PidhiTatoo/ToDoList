tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks added yet.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def remove_task(task_name):
    removed = False
    for task in tasks:
        if task.lower() == task_name.lower():
            tasks.remove(task)
            print(f"Task '{task}' removed successfully!")
            removed = True
            break
    if not removed:
        print("Task not found!")

print("Select operation:")
print("1. Add Task")
print("2. View Tasks")
print("3. Remove Task")

while True:
    choice = input("Enter choice (1/2/3): ")

    if choice == '1':
        task = input("Enter task: ")
        add_task(task)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        task_name = input("Enter task name to remove: ")
        remove_task(task_name)
    else:
        print("Invalid input")
