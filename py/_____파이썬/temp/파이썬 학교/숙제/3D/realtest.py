from vpython import *
import random as rd

ball = []
for i in range(3):
    ball.append(sphere (color = color.red, radius = 1))
    ball[i].mass = 1.0
    ball[i].p = vector (rd.random()-0.5, rd.random()-0.5, rd.random()-0.5)
    print(ball[i].p)
    
