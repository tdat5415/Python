from vpython import *
from random import *

for i in range(20000):
    col = vec(random(), random(), random())
    x = random() - 0.5
    y = random() - 0.5
    z = random() - 0.5
    d = 10/(((x**2+y**2+z**2)**(1/2)))
    x *= d
    y *= d
    z *= d
    cylinder(pos=vector(0,0,0), axis=vector (x, y, z), color=col, radius=0.5)
