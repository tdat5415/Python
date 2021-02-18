import turtle as T
import math as M
import numpy as NP


#가로 480 세로 405

xmin = -4; xmax = 4; ymin = -2; ymax = 2;
T.setworldcoordinates(xmin, ymin, xmax, ymax)

T.speed(0)

T.penup(); T.goto(xmin, 0);
T.pendown(); T.goto(xmax, 0);

T.penup(); T.goto(0, ymin);
T.pendown(); T.goto(0, ymax);


dx = 0.2

T.penup()
for x in NP.arange(xmin, xmax + dx, dx):
    T.goto(x, M.sin(x))
    T.pendown()

T.penup()
for x in NP.arange(xmin, xmax + dx, dx):
    T.goto(x, M.cos(x))
    T.pendown()
