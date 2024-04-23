import tkinter as tk
from tkinter import simpledialog

# Function to add a new task after prompting user input
def add_task():
    task = simpledialog.askstring("Input", "Enter task:")
    if task:  # Ensures only non-empty tasks are added
        tasks.append(task)
        update_tasks()  # Refresh the listbox view with the new task list

# Function to remove a selected task from the list
def remove_task():
    if lstbox_tasks.curselection():  # Checks if there is any item selected
        tasks.pop(lstbox_tasks.curselection()[0])
        update_tasks()  # Refresh the listbox view after removal

# Function to update the listbox display with current tasks
def update_tasks():
    lstbox_tasks.delete(0, tk.END)  # Clears the current listbox contents
    for task in tasks:  # Re-populates the listbox with current tasks
        lstbox_tasks.insert(tk.END, task)

# Set up the main window
root = tk.Tk()
root.title("ToDo List")

# List to store tasks
tasks = []

# Creating the listbox widget to display tasks
lstbox_tasks = tk.Listbox(root, height=10, width=50)
lstbox_tasks.pack(pady=10)  # Add some padding around the listbox

# Creating and setting up the button to add tasks
btn_add_task = tk.Button(root, text="Add Task", command=add_task)
btn_add_task.pack(fill=tk.X)  # Make the button expand to fill the X direction

# Creating and setting up the button to remove tasks
btn_remove_task = tk.Button(root, text="Remove Task", command=remove_task)
btn_remove_task.pack(fill=tk.X)  # Make the button expand to fill the X direction

# Starts the event loop (makes the window responsive)
root.mainloop()
