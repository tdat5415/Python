from turtle import *
from random import *


def moveTo(x, y):
	setheading(towards(x, y))
	goto(x, y);

def drawRight():
	setheading(0); fd(5)
def drawLeft():
	setheading(180); fd(5)
def drawUp():
	setheading(90); fd(5)
def drawDown():
	setheading(270); fd(5)

def changeColor():
	color(random(), random(), random())

shape("turtle")

speed(0)

onscreenclick(moveTo, btn=1)
onkey(penup, "u")
onkey(pendown, "d")
onkey(clear, "Delete")
onkey(home, "Home")
onkey(reset, "Escape")

onkey(changeColor, "space")

onkeypress(drawRight, "Right")
onkeypress(drawLeft, "Left")
onkeypress(drawUp, "Up")
onkeypress(drawDown, "Down")

ondrag(goto)

listen()
