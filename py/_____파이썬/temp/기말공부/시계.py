from vpython import *
from random import *

second= cylinder(pos = vec(0,0,0), radius = 0.2, axis =vec(0,10,0), color = color.red)
minute= cylinder(pos = vec(0,0,-0.5), radius = 0.3, axis =vec(0,8,0), color = color.yellow )
hour= cylinder(pos = vec(0,0,-1.0), radius = 0.5, axis =vec(0,6,0), color = color.white )
ang= 2*pi/60
h_ang= 2*pi/12

for k in range(12):
    for j in range(60):
        for i in range(60) :
            rate(10000)
            second.rotate(angle = ang, axis=vec(0,0,-1), origin = vec(0,0,0))
        minute.rotate(angle = ang, axis=vec(0,0,-1), origin =vec(0,0,0))
    hour.rotate(angle = h_ang, axis=vec(0,0,-1), origin =vec(0,0,0))
