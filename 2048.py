import tkinter as tk
from random import randint

class Game2048:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("2048 Game")
        self.window.geometry("400x400")
        self.frame = tk.Frame(self.window, bg="azure3")
        self.frame.pack(fill="both", expand=True)
        self.grid = [[0]*4 for _ in range(4)]
        self.score = 0
        self.create_widgets()
        self.new_game()

    def create_widgets(self):
        self.buttons = []
        for i in range(4):
            row = []
            for j in range(4):
                button = tk.Button(self.frame, text="", width=5, height=2, font=("Arial", 20), bg="azure2", command=lambda i=i, j=j: self.click(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

        self.score_label = tk.Label(self.frame, text="Score: 0", font=("Arial", 20), bg="azure3")
        self.score_label.grid(row=4, column=0, columnspan=4)

    def new_game(self):
        self.score = 0
        self.score_label['text'] = "Score: 0"
        self.grid = [[0]*4 for _ in range(4)]
        self.add_tile()
        self.add_tile()
        self.update_grid()

    def add_tile(self):
        while True:
            x, y = randint(0, 3), randint(0, 3)
            if self.grid[x][y] == 0:
                self.grid[x][y] = 2
                break

    def update_grid(self):
        for i in range(4):
            for j in range(4):
                if self.grid[i][j] == 0:
                    self.buttons[i][j]['text'] = ""
                else:
                    self.buttons[i][j]['text'] = str(self.grid[i][j])

    def click(self, i, j):
        if self.grid[i][j]!= 0:
            if i > 0 and self.grid[i-1][j] == self.grid[i][j]:
                self.grid[i-1][j] *= 2
                self.grid[i][j] = 0
                self.score += self.grid[i-1][j]
            elif j > 0 and self.grid[i][j-1] == self.grid[i][j]:
                self.grid[i][j-1] *= 2
                self.grid[i][j] = 0
                self.score += self.grid[i][j-1]
            elif i < 3 and self.grid[i+1][j] == self.grid[i][j]:
                self.grid[i+1][j] *= 2
                self.grid[i][j] = 0
                self.score += self.grid[i+1][j]
            elif j < 3 and self.grid[i][j+1] == self.grid[i][j]:
                self.grid[i][j+1] *= 2
                self.grid[i][j] = 0
                self.score += self.grid[i][j+1]
        self.score_label['text'] = "Score: " + str(self.score)
        self.update_grid()
        self.add_tile()
        self.update_grid()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = Game2048()
    game.run()