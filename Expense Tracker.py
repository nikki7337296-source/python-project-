from tkinter import *
from tkinter import messagebox

# Create main window
root = Tk()
root.title("Expense Tracker")
root.geometry("450x500")

# Lists for storing expenses
expenses = []

# Function to add expense
def add_expense():
    item = item_entry.get()
    amount = amount_entry.get()

    if item != "" and amount != "":
        try:
            amount = float(amount)

            # Store expense
            expenses.append((item, amount))

            # Display in listbox
            listbox.insert(END, f"{item} - ₹{amount}")

            # Update total
            update_total()

            # Clear entry boxes
            item_entry.delete(0, END)
            amount_entry.delete(0, END)

        except:
            messagebox.showerror("Error", "Enter valid amount!")

    else:
        messagebox.showwarning("Warning", "Fill all fields!")

# Function to calculate total spending
def update_total():
    total = 0

    for item, amount in expenses:
        total += amount

    total_label.config(text=f"Total Spending: ₹{total}")

# Title
title = Label(root, text="Expense Tracker",
              font=("Arial", 18, "bold"))
title.pack(pady=10)

# Item label and entry
Label(root, text="Expense Name:",
      font=("Arial", 12)).pack()

item_entry = Entry(root, width=30, font=("Arial", 12))
item_entry.pack(pady=5)

# Amount label and entry
Label(root, text="Amount:",
      font=("Arial", 12)).pack()

amount_entry = Entry(root, width=30, font=("Arial", 12))
amount_entry.pack(pady=5)

# Add button
add_btn = Button(root, text="Add Expense",
                 width=15, command=add_expense)
add_btn.pack(pady=10)

# Listbox to display expenses
listbox = Listbox(root, width=40, height=12,
                  font=("Arial", 11))
listbox.pack(pady=10)

# Total label
total_label = Label(root,
                    text="Total Spending: ₹0",
                    font=("Arial", 14, "bold"))
total_label.pack(pady=10)

# Run application
root.mainloop()