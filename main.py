from tkinter import *
import random

# constants
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "green"
FOOD_COLOR = "yellow"
BACKGROUND_COLOR = "#000000"


class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []
        # list of coordinates
        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        # create some boxes
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x +
                                             SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
            self.squares.append(square)


class Food:
    def __init__(self):
        x_coordinate = random.randint(0, 700)
        y_coordinate = random.randint(0, 700)

        self.coordinates = [x_coordinate, y_coordinate]
        # draw food canvas
        canvas.create_oval(x_coordinate, y_coordinate, x_coordinate + SPACE_SIZE,
                           y_coordinate + SPACE_SIZE, fill=FOOD_COLOR, tags="food")


def next_turn():
    pass


def change_direction(new_direction):
    pass


def check_collisions():
    pass


def game_over():
    pass


window = Tk()
window.title("Snake game")
window.resizable(False, False)
# score
score = 0
direction = "down"

label = Label(window, text="score:{}".format(score), font=('consolas', 50))
label.pack()

# create a canvas
canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_height = window.winfo_height()
window_width = window.winfo_width()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# adjust the position of window
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
# set the geometry of the window

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

snake = Snake()
food = Food()

window.mainloop()
