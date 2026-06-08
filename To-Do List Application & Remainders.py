from tkinter import *
from tkinter import messagebox

# Create main window
root = Tk()
root.title("To-Do List")
root.geometry("400x500")

# List to store tasks
tasks = []

# Function to add task
def add_task():
    task = task_entry.get()

    if task != "":
        tasks.append(task)
        listbox.insert(END, task)
        task_entry.delete(0, END)
    else:
        messagebox.showwarning("Warning", "Enter a task!")

# Function to delete selected task
def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
        tasks.pop(selected)
    except:
        messagebox.showwarning("Warning", "Select a task to delete!")

# Function to clear all tasks
def clear_tasks():
    listbox.delete(0, END)
    tasks.clear()

# Heading
title = Label(root, text="To-Do List App",
              font=("Arial", 18, "bold"))
title.pack(pady=10)

# Entry box
task_entry = Entry(root, width=30, font=("Arial", 14))
task_entry.pack(pady=10)

# Add button
add_btn = Button(root, text="Add Task",
                 width=15, command=add_task)
add_btn.pack(pady=5)

# Listbox to display tasks
listbox = Listbox(root, width=40, height=12,
                  font=("Arial", 12),
                  selectbackground="lightblue")
listbox.pack(pady=10)

# Delete button
delete_btn = Button(root, text="Delete Task",
                    width=15, command=delete_task)
delete_btn.pack(pady=5)

# Clear button
clear_btn = Button(root, text="Clear All",
                   width=15, command=clear_tasks)
clear_btn.pack(pady=5)

# Run window
root.mainloop()