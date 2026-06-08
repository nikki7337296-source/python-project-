from tkinter import *
import random

# Create window
root = Tk()
root.title("Puzzle Rearrangement Game")
root.geometry("320x380")

# Correct order
correct_order = [1, 2, 3,
                 4, 5, 6,
                 7, 8, ""]

# Shuffle puzzle
tiles = correct_order.copy()

while True:
    random.shuffle(tiles)
    if tiles != correct_order:
        break

buttons = []
selected = None

# Function to update buttons
def update_buttons():

    for i in range(9):
        buttons[i].config(text=tiles[i])

# Function when tile clicked
def tile_click(index):

    global selected

    # First selection
    if selected is None:
        selected = index
        buttons[index].config(bg="lightblue")

    else:
        # Swap tiles
        tiles[selected], tiles[index] = \
            tiles[index], tiles[selected]

        # Reset button colors
        for btn in buttons:
            btn.config(bg="SystemButtonFace")

        # Update board
        update_buttons()

        # Check win
        if tiles == correct_order:
            result_label.config(
                text="🎉 Puzzle Solved!"
            )

        selected = None

# Title
title = Label(root,
              text="Puzzle Rearrangement Game",
              font=("Arial", 16, "bold"))
title.pack(pady=10)

# Puzzle frame
frame = Frame(root)
frame.pack()

# Create grid buttons
for i in range(9):

    btn = Button(frame,
                 text=tiles[i],
                 font=("Arial", 18),
                 width=6,
                 height=3,
                 command=lambda i=i: tile_click(i))

    btn.grid(row=i//3, column=i%3)

    buttons.append(btn)

# Result label
result_label = Label(root,
                     text="",
                     font=("Arial", 14, "bold"))
result_label.pack(pady=20)

# Initial display
update_buttons()

# Run application
root.mainloop()