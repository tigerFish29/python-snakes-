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
    pass

class Food:
    pass

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

window.mainloop()

