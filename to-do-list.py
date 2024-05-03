import tkinter as tk
from tkinter import simpledialog #tkinter and Simpledialog allows us to have this ui we are using right now. It looks a bit old but I-
#-couldn't get the themes to work.


# This function lets you add a new task to your list. When you run it,
# it asks you what task you want to add. If you tell it something, it will remember that task and show it on the screen.
def add_task():
    task = simpledialog.askstring("Input", "Enter task:")
    if task:  # Make sure the task isn't empty
        tasks.append(task)
        update_tasks()  # Now, let's update the screen to show your new task, without this it wont even appear.

# This function helps you remove a task you don't want anymore. It checks if you
# have chosen a task to remove, and if you have, it takes it off your list and updates the screen to show the change.
def remove_task():
    if lstbox_tasks.curselection():  # Checks if you've selected a task
        tasks.pop(lstbox_tasks.curselection()[0])
        update_tasks()  # Updates the screen to show the remaining tasks

# Here we update the list on the screen with all the tasks you've told it. First,
# it clears the old list and then adds all the tasks back in so you can see everything you need to do!
def update_tasks():
    lstbox_tasks.delete(0, tk.END)  # Clear the list on the screen
    for task in tasks:  # Add each task back to the list on the screen
        lstbox_tasks.insert(tk.END, task)

# Setting up the main window of our app where everything happens. It's like the stage
# for our little task-show where we get to add and remove tasks!
root = tk.Tk()
root.title("ToDo List")


tasks = []

# This is a special box where we show all the tasks you need to do. It's like
# a display board that lets you see everything clearly.
lstbox_tasks = tk.Listbox(root, height=10, width=50)
lstbox_tasks.pack(pady=10)  # We add some space around the box so it looks nice.

# This is a button that adds a new task. When you click it, it starts the process
# of adding a task to your list.
btn_add_task = tk.Button(root, text="Add Task", command=add_task)
btn_add_task.pack(fill=tk.X)  # The button grows to fill the space it's in, so it's easy to click.

# This button lets you remove a task from your list. It's super helpful for
# keeping your list neat and tidy.
btn_remove_task = tk.Button(root, text="Remove Task", command=remove_task)
btn_remove_task.pack(fill=tk.X)  # This button also grows to fill its space.

root.mainloop()



#I never got the themes to work as well as the ability to save things as I couldn't really understand them.
#Also I tried to make the comments seem better and more fun in a way so it won't be boring to read.
