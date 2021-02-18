import time
from vpython import *

ball1 = sphere(pos=vec(-1, 0, 0), radius=2, color=color.blue)
ball2 = sphere(pos=vec(1, 0, 0), radius=2, color=color.red)

time.sleep(2)
for i in range(21):
    ball2.rotate(angle=pi/10, origin=vec(0,0,0), axis=vec(0,1,0))
    time.sleep(0.1)
