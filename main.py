from turtle import Turtle
from turtle import Screen
from turtle import textinput
import random
screen = Screen()
screen.title("Turtle Race")
writing_turtle = Turtle()
writing_turtle.hideturtle()
writing_turtle.penup()
writing_turtle.color("black")
writing_turtle.goto(-200, 100)
COLORS = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
turtles = []
cur = -90
for color in COLORS:
    tim = Turtle()
    tim.color(color)
    tim.shape("turtle")
    tim.penup()
    tim.shapesize(1.5, 1.5)
    tim.goto(-320, cur)
    cur += 40
    turtles.append(tim)

choice = str(textinput("enter your choice", "who's gonna win ?"))
winning = None
flag = 1
while True:
    for turtle in turtles:
        turtle.forward(random.randint(10, 40))
        if turtle.xcor() >= 300:
            flag = 0
            winning = turtle.color()[0]
            break
    if not flag:
        break

if choice.lower() == winning:
    writing_turtle.write("YOU HAVE WON THE BET", False, font=("Arial", 20, "bold"))
else:
    writing_turtle.write("YOU HAVE LOST THE BET", False, font=("Arial", 20, "bold"))
screen.mainloop()
