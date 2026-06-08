from tkinter import *
import random

# Create main window
root = Tk()
root.title("Memory Card Matching Game")
root.geometry("400x450")

# Card symbols
symbols = ['🍎', '🍎', '🍌', '🍌',
           '🍇', '🍇', '🍒', '🍒']

# Shuffle cards
random.shuffle(symbols)

# Variables
buttons = []
first_card = None
second_card = None
first_index = None

# Function to handle card click
def flip_card(index):

    global first_card, second_card, first_index

    # Show symbol
    buttons[index]["text"] = symbols[index]
   
