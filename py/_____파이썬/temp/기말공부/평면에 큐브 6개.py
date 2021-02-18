from vpython import *
from random import *

box(pos = vector(0, 0, -1), length=25, height=25, width=0.1)
for i in range(6):
    col = vec(random(), random(), random())
    x = randint(0, 20) - 10
    y = randint(0, 20) - 10
    box(pos=vector(x, y, 0), length=2, height=2, width=2, color=col)
