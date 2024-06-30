import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.geometry("300x300")

        self.player1_name = tk.StringVar()
        self.player2_name = tk.StringVar()

        self.name_page()

    def name_page(self):
        tk.Label(self.window, text="Player 1 Name:").pack()
        tk.Entry(self.window, textvariable=self.player1_name).pack()
        tk.Label(self.window, text="Player 2 Name:").pack()
        tk.Entry(self.window, textvariable=self.player2_name).pack()
        tk.Button(self.window, text="Start Game", command=self.start_game).pack()

    def start_game(self):
        for widget in self.window.winfo_children():
            widget.destroy()

        self.player_turn = "X"
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.window, command=lambda row=i, column=j: self.click(row, column), height=3, width=6)
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

        self.restart_button = tk.Button(self.window, text="Restart", command=self.restart)
        self.restart_button.grid(row=3, column=0, columnspan=3)

    def click(self, row, column):
        if self.buttons[row][column]['text'] == "":
            self.buttons[row][column]['text'] = self.player_turn
            if self.check_win():
                messagebox.showinfo("Game Over", f"{self.player1_name.get() if self.player_turn == 'X' else self.player2_name.get()} wins!")
                self.window.quit()
            self.player_turn = "O" if self.player_turn == "X" else "X"

    def check_win(self):
        for row in self.buttons:
            if row[0]['text'] == row[1]['text'] == row[2]['text'] != "":
                return True
        for column in range(3):
            if self.buttons[0][column]['text'] == self.buttons[1][column]['text'] == self.buttons[2][column]['text'] != "":
                return True
        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != "":
            return True
        if self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != "":
            return True
        return False

    def restart(self):
        for widget in self.window.winfo_children():
            widget.destroy()
        self.name_page()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()