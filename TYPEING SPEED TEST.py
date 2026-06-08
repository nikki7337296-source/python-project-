from tkinter import *
import time

# Sample text
text_to_type = "Python programming is fun and easy."

# Variables
start_time = 0

# Function to start timer
def start_typing(event):
    global start_time

    if start_time == 0:
        start_time = time.time()

# Function to calculate speed and accuracy
def check_result():

    end_time = time.time()

    typed_text = entry.get()

    # Time taken
    time_taken = end_time - start_time

    # Words per minute
    words = len(typed_text.split())
    wpm = (words / time_taken) * 60

    # Accuracy calculation
    correct_chars = 0

    for i in range(min(len(typed_text), len(text_to_type))):
        if typed_text[i] == text_to_type[i]:
            correct_chars += 1

    accuracy = (correct_chars / len(text_to_type)) * 100

    # Display result
    result_label.config(
        text=f"Speed: {wpm:.2f} WPM\nAccuracy: {accuracy:.2f}%"
    )

# Create window
root = Tk()
root.title("Typing Speed Test")
root.geometry("600x350")

# Heading
title = Label(root,
              text="Typing Speed Test",
              font=("Arial", 18, "bold"))
title.pack(pady=10)

# Text to type
text_label = Label(root,
                   text=text_to_type,
                   font=("Arial", 14),
                   wraplength=500)
text_label.pack(pady=20)

# Typing entry
entry = Entry(root, width=50, font=("Arial", 14))
entry.pack(pady=10)

# Start timer when typing begins
entry.bind("<KeyPress>", start_typing)

# Submit button
submit_btn = Button(root,
                    text="Check Result",
                    command=check_result)
submit_btn.pack(pady=15)

# Result label
result_label = Label(root,
                     text="",
                     font=("Arial", 14))
result_label.pack(pady=20)

# Run application
root.mainloop()