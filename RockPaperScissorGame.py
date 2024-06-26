import tkinter as tk
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.geometry("400x300")
        self.root.configure(background="#f0f0f0")

        self.rules_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.rules_frame.pack()

        self.instruction_label = tk.Label(self.rules_frame, text="Winning rules of the game ROCK PAPER SCISSORS are :\n"
                                                      "Rock vs Paper -> Paper wins \n"
                                                      "Rock vs Scissors -> Rock wins \n"
                                                      "Paper vs Scissors -> Scissor wins \n",
                                          font=("Arial", 12), wraplength=350, bg="#f0f0f0")
        self.instruction_label.pack(pady=10)

        self.choice_label = tk.Label(self.rules_frame, text="Enter your choice:", font=("Arial", 14), bg="#f0f0f0")
        self.choice_label.pack()

        self.choice_frame = tk.Frame(self.rules_frame, bg="#f0f0f0")
        self.choice_frame.pack()

        self.rock_button = tk.Button(self.choice_frame, text="Rock", command=lambda: self.play(1), width=10, bg="green", fg="white")
        self.rock_button.pack(side=tk.LEFT, padx=5)

        self.paper_button = tk.Button(self.choice_frame, text="Paper", command=lambda: self.play(2), width=10, bg="blue", fg="white")
        self.paper_button.pack(side=tk.LEFT, padx=5)

        self.scissors_button = tk.Button(self.choice_frame, text="Scissors", command=lambda: self.play(3), width=10, bg="red", fg="white")
        self.scissors_button.pack(side=tk.LEFT, padx=5)

        self.result_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.result_frame.pack(pady=20)

        self.result_label = tk.Label(self.result_frame, text="", font=("Arial", 14), bg="#f0f0f0")
        self.result_label.pack(pady=10)

        self.play_again_label = tk.Label(self.result_frame, text="Do you want to play again? (Y/N)", font=("Arial", 12), bg="#f0f0f0")
        self.play_again_label.pack(pady=10)

        self.play_again_entry = tk.Entry(self.result_frame, width=20)
        self.play_again_entry.pack()

        self.play_again_button = tk.Button(self.result_frame, text="Play Again", command=self.play_again, width=10, bg="green", fg="white")
        self.play_again_button.pack(pady=10)

    def play(self, choice):
        comp_choice = random.randint(1, 3)
        while comp_choice == choice:
            comp_choice = random.randint(1, 3)

        choice_name = ""
        comp_choice_name = ""

        if choice == 1:
            choice_name = "Rock"
        elif choice == 2:
            choice_name = "Paper"
        else:
            choice_name = "Scissors"

        if comp_choice == 1:
            comp_choice_name = "Rock"
        elif comp_choice == 2:
            comp_choice_name = "Paper"
        else:
            comp_choice_name = "Scissors"

        result = ""

        if choice == comp_choice:
            result = "DRAW"
        elif (choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 3) or (choice == 3 and comp_choice == 1):
            result = "Computer"
        else:
            result = "User"

        self.result_label.config(text=f"User choice: {choice_name}\nComputer choice: {comp_choice_name}\nResult: {result} wins!")

    def play_again(self):
        self.result_label.config(text="")
        self.play_again_entry.delete(0, tk.END)

root = tk.Tk()
game = RockPaperScissors(root)
root.mainloop()