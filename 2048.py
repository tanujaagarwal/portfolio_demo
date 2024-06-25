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
        self.create_menu()

    def create_menu(self):
        self.menu_frame = tk.Frame(self.window, bg="azure3")
        self.menu_frame.pack(fill="both", expand=True)

        self.play_button = tk.Button(self.menu_frame, text="Play", font=("Arial", 20), command=self.start_game, bg="green", fg="white")
        self.play_button.pack(fill="x")

        self.settings_button = tk.Button(self.menu_frame, text="Settings", font=("Arial", 20), command=self.settings, bg="blue", fg="white")
        self.settings_button.pack(fill="x")

        self.exit_button = tk.Button(self.menu_frame, text="Exit", font=("Arial", 20), command=self.window.destroy, bg="red", fg="white")
        self.exit_button.pack(fill="x")

    def start_game(self):
        self.menu_frame.destroy()
        self.create_widgets()
        self.new_game()

    def settings(self):
        print("Settings button clicked")

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

        self.restart_button = tk.Button(self.frame, text="Restart", font=("Arial", 20), command=self.new_game, bg="orange", fg="white")
        self.restart_button.grid(row=5, column=0, columnspan=4)

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
                    self.buttons[i][j]['bg'] = "azure2"
                else:
                    self.buttons[i][j]['text'] = str(self.grid[i][j])
                    if self.grid[i][j] < 8:
                        self.buttons[i][j]['bg'] = "azure2"
                    elif self.grid[i][j] < 128:
                        self.buttons[i][j]['bg'] = "lightgreen"
                    elif self.grid[i][j] < 512:
                        self.buttons[i][j]['bg'] = "green"
                    elif self.grid[i][j] < 2048:
                        self.buttons[i][j]['bg'] = "darkgreen"
                    else:
                        self.buttons[i][j]['bg'] = "black"

        if self.is_game_over():
            self.score_label['text'] = "Game Over! Score: " + str(self.score)

    def click(self, i, j):
     if self.grid[i][j] != 0:
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
        if not self.is_game_over():
             self.add_tile()
        self.update_grid()

    def is_game_over(self):
        for i in range(4):
            for j in range(4):
                if self.grid[i][j] == 0:
                    return False
                if i > 0 and self.grid[i-1][j] == self.grid[i][j]:
                    return False
                if j > 0 and self.grid[i][j-1] == self.grid[i][j]:
                    return False
                if i <3 and self.grid[i+1][j] == self.grid[i][j]:
                    return False
                if j < 3 and self.grid[i][j+1] == self.grid[i][j]:
                    return False
        return True

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = Game2048()
    game.run()