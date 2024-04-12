# todo_list.py

#This code creates a list that we can use to create a to do list like mine.
tasks = []

#Here I use def to define the functions shown below. I also use if and else so I can have 3 functions at the same time.
#Also a new thing, to me atleast is the enumerate. It's a way to give a number to objects, it starts with 0 and goes upwards from there.
#If you want to you can change it so it starts with 1 instead but I find it uneccessary as this code MAY be scrapped anyway..
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

def remove_task(task_index):
    try:
        del tasks[task_index - 1]
        print("Task removed successfully!")
    except IndexError:
        print("Invalid task index!")

#As you can see this is just to print the thing you wanna do, nothing special.
print("Select operation:")
print("1. Add Task")
print("2. View Tasks")
print("3. Remove Task")

#This part of the code allows you to choose if you want to add daily tasks, see them and delete them.
#Choice 1 is to add, choice 2 is to see the status and choice 3 is to delete, however to delete you have to press a number instead of its name
#depending on when you added the task. so if you have 3 tasks (Cheese, dolphin, horse) cheese would be 0, dolphin 1 and horse 2.
#It has to do with the enumerate explained earlier. 
while True:
    choice = input("Enter choice (1/2/3): ")

    if choice == '1':
        task = input("Enter task: ")
        add_task(task)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        task_index = int(input("Enter task index to remove: "))
        remove_task(task_index)
    else:
        print("Invalid input")
