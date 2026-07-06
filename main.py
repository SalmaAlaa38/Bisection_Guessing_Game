import tkinter as tk
from tkinter import messagebox

# Game State
# TO BE CHANGED INTO A CLASS!!!!!

minimum = 1
maximum = 100

low = minimum
high = maximum

guess = 0
attempts = 0

# Functions

def calculate_guess():
    """Calculate the middle value and update the UI"""
    global guess, attempts

    if low > high:
        messagebox.showerror(
            "Error",
            "your answers are inconsistent!\nNo valid number exists."
        )
        disable_game()
        return
    
    guess = (low + high) // 2
    attempts += 1

    guess_label.config(text=f"My Guess: {guess}")
    attempts_label.config(text=f"Attempts: {attempts}")
    interval_label.config(text=f"Possible range: {low} - {high}")

def start_game():
    """Start or restart the game"""
    global low, high, attempts

    low = minimum
    high = maximum
    attempts = 0

    enable_game()
    calculate_guess()

def higher():
    """When the player says the number is higher"""
    global low
    low = guess + 1
    calculate_guess()

def lower():
    """When the player says the number is lower"""
    global high
    high = guess - 1
    calculate_guess()

def correct():
    """When the user confirms the guess"""
    messagebox.showinfo(
        "Success",
        f"I guessed your number!\n\nNumber: {guess}\nAttempts: {attempts}"
    )
    disable_game()

def disable_game():
    """Disabling the buttons"""
    higher_button.config(state=tk.DISABLED)
    lower_button.config(state=tk.DISABLED)
    correct_button.config(state=tk.DISABLED)


def enable_game():
    """Enabling the buttons"""
    higher_button.config(state=tk.NORMAL)
    lower_button.config(state=tk.NORMAL)
    correct_button.config(state=tk.NORMAL)


root = tk.Tk()
root.title("Bisection Guessing Game")
root.geometry("450x350")
root.resizable(False, False)

title = tk.Label(
    root,
    text="Bisection Guessing Game",
    font=("Arial", 18, "bold")
)
title.pack(pady=15)

instruction = tk.Label(
    root,
    text="Think of a number between 1 and 100\nThen press Start Game.",
    font=("Arial", 11)
)
instruction.pack()

# information labels

guess_label = tk.Label(
    root,
    text="My Guess: -",
    font=("Arial", 16)
)
guess_label.pack(pady=15)

attempts_label = tk.Label(
    root,
    text="Attempts: 0",
    font=("Arial", 12)
)
attempts_label.pack()

interval_label = tk.Label(
    root,
    text="Possible Range: 1 - 100",
    font=("Arial", 12)
)
interval_label.pack(pady=10)


# Buttons

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

higher_button = tk.Button(
    button_frame,
    text="Higher",
    width=10,
    command=higher
)
higher_button.grid(row=0, column=0, padx=5)

lower_button =tk.Button(
    button_frame,
    text="Lower",
    width=10,
    command=lower
)
lower_button.grid(row=0, column=1, padx=5)

correct_button = tk.Button(
    button_frame,
    text="Correct",
    width=10,
    command=correct
)
correct_button.grid(row=0, column=2, padx=5)

disable_game()


start_button = tk.Button(
    root,
    text="Start Game",
    width=20,
    font=("Arial", 12, "bold"),
    command=start_game
)
start_button.pack()

# Run the application

root.mainloop()