from tkinter import *

# Create window
root = Tk()
root.title("Drawing Pad")
root.geometry("800x600")

# Create canvas
canvas = Canvas(root, bg="white", width=800, height=600)
canvas.pack()

# Variables to store previous mouse position
last_x, last_y = None, None

# Function to draw
def draw(event):
    global last_x, last_y

    x, y = event.x, event.y

    # Draw line from previous point to current point
    if last_x is not None and last_y is not None:
        canvas.create_line(last_x, last_y, x, y,
                           fill="black", width=3)

    last_x, last_y = x, y

# Reset coordinates when mouse button released
def reset(event):
    global last_x, last_y
    last_x, last_y = None, None

# Mouse events
canvas.bind("<B1-Motion>", draw)   # Mouse drag
canvas.bind("<ButtonRelease-1>", reset)

# Run window
root.mainloop()