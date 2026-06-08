from tkinter import *
from tkinter import ttk, messagebox

# Create main window
root = Tk()
root.title("Attendance Management System")
root.geometry("700x400")

# Data storage
students = []

# Function to add student
def add_student():
    name = name_entry.get()

    if name != "":
        students.append([name, "Absent"])

        # Insert into table
        table.insert("", END, values=(name, "Absent"))

        name_entry.delete(0, END)
    else:
        messagebox.showwarning("Warning", "Enter student name!")

# Function to mark attendance
def mark_present():
    selected = table.selection()

    if selected:
        for item in selected:
            table.item(item, values=(table.item(item)["values"][0],
                                     "Present"))
    else:
        messagebox.showwarning("Warning", "Select a student!")

# Function to mark absent
def mark_absent():
    selected = table.selection()

    if selected:
        for item in selected:
            table.item(item, values=(table.item(item)["values"][0],
                                     "Absent"))
    else:
        messagebox.showwarning("Warning", "Select a student!")

# Title
title = Label(root, text="Attendance Management System",
              font=("Arial", 18, "bold"))
title.pack(pady=10)

# Frame for input
frame = Frame(root)
frame.pack(pady=10)

# Entry box
name_entry = Entry(frame, width=30, font=("Arial", 12))
name_entry.grid(row=0, column=0, padx=10)

# Add button
add_btn = Button(frame, text="Add Student",
                 command=add_student)
add_btn.grid(row=0, column=1)

# Table
columns = ("Name", "Attendance")

table = ttk.Treeview(root, columns=columns,
                     show="headings", height=10)

table.heading("Name", text="Student Name")
table.heading("Attendance", text="Attendance")

table.column("Name", width=250)
table.column("Attendance", width=150)

table.pack(pady=20)

# Buttons frame
btn_frame = Frame(root)
btn_frame.pack()

# Present button
present_btn = Button(btn_frame, text="Mark Present",
                     width=15, command=mark_present)
present_btn.grid(row=0, column=0, padx=10)

# Absent button
absent_btn = Button(btn_frame, text="Mark Absent",
                    width=15, command=mark_absent)
absent_btn.grid(row=0, column=1, padx=10)

# Run application
root.mainloop()