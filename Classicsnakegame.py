# snake_game.py

import tkinter as tk
import random

class SnakeGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Snake Game")
        self.window.resizable(False, False)

        self.canvas = tk.Canvas(self.window, width=400, height=400, bg="black")
        self.canvas.pack()

        self.snake = [(200, 200), (220, 200), (240, 200)]
        self.food = self.generate_food()
        self.direction = "Right"

        self.bind_keys()
        self.draw_snake()
        self.draw_food()
        self.update()

        self.window.mainloop()

    def bind_keys(self):
        self.window.bind("<Up>", lambda event: self.change_direction("Up"))
        self.window.bind("<Down>", lambda event: self.change_direction("Down"))
        self.window.bind("<Left>", lambda event: self.change_direction("Left"))
        self.window.bind("<Right>", lambda event: self.change_direction("Right"))
        self.window.bind("<space>", lambda event: self.restart())

    def change_direction(self, direction):
        if direction == "Up" and self.direction != "Down":
            self.direction = "Up"
        elif direction == "Down" and self.direction != "Up":
            self.direction = "Down"
        elif direction == "Left" and self.direction != "Right":
            self.direction = "Left"
        elif direction == "Right" and self.direction != "Left":
            self.direction = "Right"

    def generate_food(self):
        x = random.randint(0, 39) * 10
        y = random.randint(0, 39) * 10
        return (x, y)

    def draw_snake(self):
        self.canvas.delete("snake")
        for i, (x, y) in enumerate(self.snake):
            if i == 0:
                self.canvas.create_oval(x, y, x + 10, y + 10, fill="green", tag="snake")
            else:
                self.canvas.create_oval(x, y, x + 10, y + 10, fill="dark green", tag="snake")

    def draw_food(self):
        self.canvas.delete("food")
        x, y = self.food
        self.canvas.create_oval(x, y, x + 10, y + 10, fill="red", tag="food")

    def update(self):
        head_x, head_y = self.snake[0]
        if self.direction == "Up":
            new_head = (head_x, (head_y - 10) % 400)
        elif self.direction == "Down":
            new_head = (head_x, (head_y + 10) % 400)
        elif self.direction == "Left":
            new_head = ((head_x - 10) % 400, head_y)
        elif self.direction == "Right":
            new_head = ((head_x + 10) % 400, head_y)

        self.snake.insert(0, new_head)

        if self.snake[0] == self.food:
            self.food = self.generate_food()
        else:
            self.snake.pop()

        self.draw_snake()
        self.draw_food()

        if self.snake[0] in self.snake[1:]:
            self.game_over()
        else:
            self.window.after(100, self.update)

    def game_over(self):
        self.canvas.create_text(200, 200, text="Game Over! Press Space to restart.", font=("Arial", 24), fill="red")

    def restart(self):
        self.canvas.delete("all")
        self.snake = [(200, 200), (220, 200), (240, 200)]
        self.food = self.generate_food()
        self.direction = "Right"
        self.draw_snake()
        self.draw_food()
        self.update()

if __name__ == "__main__":
    game = SnakeGame()