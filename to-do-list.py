import tkinter as tk
from tkinter import simpledialog

def add_task():
    task = simpledialog.askstring("Input", "Enter task:")
    if task:
        tasks.append(task)
        update_tasks()

def remove_task():
    if lstbox_tasks.curselection():
        tasks.pop(lstbox_tasks.curselection()[0])
        update_tasks()

def update_tasks():
    lstbox_tasks.delete(0, tk.END)
    for task in tasks:
        lstbox_tasks.insert(tk.END, task)

root = tk.Tk()
root.title("ToDo List")

tasks = []

# Creating the listbox to display tasks
lstbox_tasks = tk.Listbox(root, height=10, width=50)
lstbox_tasks.pack(pady=10)

# Creating buttons and binding them to their respective functions
btn_add_task = tk.Button(root, text="Add Task", command=add_task)
btn_add_task.pack(fill=tk.X)

btn_remove_task = tk.Button(root, text="Remove Task", command=remove_task)
btn_remove_task.pack(fill=tk.X)

root.mainloop()
