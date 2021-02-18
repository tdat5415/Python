from vpython import *
from random import *
for i in range(100):
    col = vec(random(), random(), random())
    x = randint(0, 10)
    y = randint(0, 10)
    z = randint(0, 10)
    sphere(pos = vector(x, y, z), color=col)
