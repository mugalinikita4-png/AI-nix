import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("450x350")
        self.root.resizable(False, False)

        self.reset_game()

        title = tk.Label(
            root,
            text="🎯 Number Guessing Game",
            font=("Arial", 18, "bold")
        )
        title.pack(pady=10)

        self.info_label = tk.Label(
            root,
            text="Guess a number between 1 and 100",
            font=("Arial", 12)
        )
        self.info_label.pack()

        self.entry = tk.Entry(root, font=("Arial", 14), justify="center")
        self.entry.pack(pady=10)

        self.guess_btn = tk.Button(
            root,
            text="Submit Guess",
            font=("Arial", 12),
            command=self.check_guess
        )
        self.guess_btn.pack(pady=5)

        self.result_label = tk.Label(
            root,
            text="",
            font=("Arial", 12, "bold")
        )
        self.result_label.pack(pady=10)

        self.attempt_label = tk.Label(
            root,
            text="Attempts: 0",
            font=("Arial", 11)
        )
        self.attempt_label.pack()

        self.score_label = tk.Label(
            root,
            text="Score: 100",
            font=("Arial", 11)
        )
        self.score_label.pack()

        self.restart_btn = tk.Button(
            root,
            text="Restart Game",
            font=("Arial", 12),
            command=self.restart_game
        )
        self.restart_btn.pack(pady=15)

    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.score = 100

    def check_guess(self):
        try:
            guess = int(self.entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
            return

        self.attempts += 1
        self.score = max(0, 100 - (self.attempts - 1) * 10)

        if guess < self.secret_number:
            self.result_label.config(text="📉 Too Low! Try Again.")
        elif guess > self.secret_number:
            self.result_label.config(text="📈 Too High! Try Again.")
        else:
            self.result_label.config(
                text=f"🎉 Correct! Number was {self.secret_number}"
            )
            messagebox.showinfo(
                "Congratulations",
                f"You guessed the number in {self.attempts} attempts!\nScore: {self.score}"
            )

        self.attempt_label.config(text=f"Attempts: {self.attempts}")
        self.score_label.config(text=f"Score: {self.score}")

        self.entry.delete(0, tk.END)

    def restart_game(self):
        self.reset_game()
        self.result_label.config(text="")
        self.attempt_label.config(text="Attempts: 0")
        self.score_label.config(text="Score: 100")
        self.entry.delete(0, tk.END)

        messagebox.showinfo(
            "Game Restarted",
            "A new number has been generated!"
        )

root = tk.Tk()
game = NumberGuessingGame(root)
root.mainloop()
