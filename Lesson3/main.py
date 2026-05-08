import pgzrun
import random

WIDTH = 800
HEIGHT = 800
TITLE = "Alien Game"

message = "Game Start"

player = Actor("alien")
player.pos = 100,100

def draw():
    screen.clear()
    screen.fill("purple")
    player.draw()
    screen.draw.text(message, center=(400,20), fontsize=30, color="black")

def move_alien():
    player.x = random.randint(50,750)
    player.y = random.randint(50,750)
move_alien()

def on_mouse_down(pos):
    print("hi")
    global message
    if player.collidepoint(pos):
        move_alien()
        message = "Good Job!"
    else:
        message = "Error you missed the Alien!"
pgzrun.go()

