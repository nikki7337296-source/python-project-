from tkinter import *
import random

# Create window
root = Tk()
root.title("Catch the Falling Objects")
root.geometry("500x600")

# Create canvas
canvas = Canvas(root, width=500, height=600, bg="lightblue")
canvas.pack()

# Score
score = 0

# Score label
score_label = Label(root,
                    text="Score: 0",
                    font=("Arial", 14, "bold"))
score_label.pack()

# Basket coordinates
basket = canvas.create_rectangle(200, 550, 300, 580,
                                 fill="brown")

# Falling object
ball = canvas.create_oval(230, 50, 260, 80,
                          fill="red")

# Move basket left
def move_left(event):
    canvas.move(basket, -20, 0)

# Move basket right
def move_right(event):
    canvas.move(basket, 20, 0)

# Falling animation
def fall():

    global score

    # Move ball downward
    canvas.move(ball, 0, 10)

    # Get positions
    ball_pos = canvas.coords(ball)
    basket_pos = canvas.coords(basket)

    # Check collision
    if (ball_pos[2] >= basket_pos[0] and
        ball_pos[0] <= basket_pos[2] and
        ball_pos[3] >= basket_pos[1]):

        score += 1
        score_label.config(text=f"Score: {score}")

        # Reset ball position
        x = random.randint(50, 450)
        canvas.coords(ball, x, 50, x+30, 80)

    # If ball missed
    elif ball_pos[3] > 600:
        x = random.randint(50, 450)
        canvas.coords(ball, x, 50, x+30, 80)

    # Repeat animation
    root.after(50, fall)

# Keyboard controls
root.bind("<Left>", move_left)
root.bind("<Right>", move_right)

# Start game
fall()

# Run application
root.mainloop()