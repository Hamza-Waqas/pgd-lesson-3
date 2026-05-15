import pgzrun
import random

WIDTH = 800
HEIGHT = 800

message = "Click the Cookie!"
score = 0

cookie = Actor("cookie")
cookie.pos = (100, 100)

def draw():
    screen.clear()
    screen.fill("green")
    cookie.draw()

    screen.draw.text(
        message,
        center=(400, 40),
        fontsize=40,
        color="black"
    )

    screen.draw.text(
        "Score: " + str(score),
        center=(400, 90),
        fontsize=35,
        color="red"
    )

def on_mouse_down(pos):
    global score, message

    if cookie.collidepoint(pos):
        score += 1
        message = "You clicked the cookie!"
        cookie.x = random.randint(50, 700)
        cookie.y = random.randint(50, 700)
    else:
        message = "Missed!"

pgzrun.go()