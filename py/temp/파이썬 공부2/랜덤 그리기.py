import turtle as t
import random as r


def drawSquare(n):
    t.begin_fill()
    for i in range(4):
        t.fd(n)
        t.left(90)
    t.end_fill()

def drawCircle(n):
    t.begin_fill()
    t.circle(n)
    t.end_fill()

def drawTriangle(n):
    t.begin_fill()
    for i in range(3):
        t.fd(n)
        t.left(120)
    t.end_fill()


t.speed(0)
t.fillcolor("red")
for i in range(1000):
    x = r.randint(-400, 400)
    y = r.randint(-400, 400)
    
    t.penup()
    t.goto(x, y)
    t.pendown()

    R = r.randint(0, 100)
    G = r.randint(0, 100)
    B = r.randint(0, 100)
    t.fillcolor(R/100, G/100, B/100)

    s = r.randint(10, 80)
    #drawCircle(s)
    #drawSquare(s)
    drawTriangle(s)



    
