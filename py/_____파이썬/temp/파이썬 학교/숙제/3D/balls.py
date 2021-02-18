from vpython import *
import random as rd
import time as t

scene.caption = """Right button drag or Ctrl-drag to rotate "camera" to view scene.
To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
     On a two-button mouse, middle is left + right.
Shift-drag to pan left/right and up/down.
Touch screen: pinch/extend to zoom, swipe or two-finger rotate."""

rp = repulsion = 0.95 # 반발계수
gr = 0.1 #중력가속도
ballSize = 0.15 # 공 크기
numOfBalls = 200 #공 개수



ball = []

side = 4.0
thk = 0.3
s2 = 2*side - thk
s3 = 2*side + thk

#wallR = box (pos=vector( side, 0, 0), size=vector(thk, s2, s3),  color = color.red)
#wallL = box (pos=vector(-side, 0, 0), size=vector(thk, s2, s3),  color = color.red)
wallB = box (pos=vector(0, -side, 0), size=vector(s3, thk, s3),  color = color.blue)
#wallT = box (pos=vector(0,  side, 0), size=vector(s3, thk, s3),  color = color.blue)
#wallBK = box(pos=vector(0, 0, -side), size=vector(s2, s2, thk), color = color.gray(0.7))


for i in range(numOfBalls):
    ball.append(sphere (color = color.red, radius = ballSize))
    ball[i].mass = 1.0
    vx = 0.3*(rd.random()-0.5)
    vy = 0.3*(rd.random()-0.5)
    vz = 0.3*(rd.random()-0.5)
    ball[i].p = vector (vx,vy,vz)
    #ball[i].pos.y = 3*(rd.random()-0.5)
    ball[i].pos.y = 3 - 0.8*(i//25)
    ball[i].pos.x = -2 + 0.8*(i%5)
    ball[i].pos.z = -2 + 0.8*(i//5%5)
    

    


side = side - thk*0.5 - ball[0].radius

#ball.pos.x = 2
#ball2.pos.x = -2

dt = 0.3



def disBall(b1,b2):
    x = b1.pos.x - b2.pos.x
    y = b1.pos.y - b2.pos.y
    z = b1.pos.z - b2.pos.z
    return (x**2 + y**2 + z**2)**0.5

def symmetryBalls(v1,v2,p1,p2):
    fV = flatVec = vector(p1-p2) # p2 -> p1
    flatToV1 = (abs(fV.x*v1.x + fV.y*v1.y + fV.z*v1.z))/((fV.x**2 + fV.y**2 + fV.z**2)**0.5)
    flatToV2 = (abs(fV.x*v2.x + fV.y*v2.y + fV.z*v2.z))/((fV.x**2 + fV.y**2 + fV.z**2)**0.5)
    absfV = (fV.x**2 + fV.y**2 + fV.z**2)**0.5
    fromV1ToV2 = -1 * fV/absfV * flatToV1
    fromV2ToV1 = fV/absfV * flatToV2
    return v1+fromV2ToV1-fromV1ToV2, v2+fromV1ToV2-fromV2ToV1


t.sleep(2)
while True:
    rate(30)
    for i in range(numOfBalls):
        ball[i].pos = ball[i].pos + (ball[i].p/ball[i].mass)*dt
        ball[i].p.y -= gr

    for i in range(numOfBalls-1):
        for j in range(i+1,numOfBalls):
            if disBall(ball[i],ball[j]) <= ballSize*2:
                ball[i].p, ball[j].p = symmetryBalls(ball[i].p,ball[j].p,ball[i].pos,ball[j].pos)
                ball[i].p *= rp**6
                ball[j].p *= rp**6####
        
    for i in range(numOfBalls):
        if not (side > ball[i].pos.x):
            ball[i].p.x = -abs(ball[i].p.x) * rp
        if not (side > ball[i].pos.y):
            ball[i].p.y = -abs(ball[i].p.y) * rp
        if not (side > ball[i].pos.z):
            ball[i].p.z = -abs(ball[i].p.z) * rp
        if not (ball[i].pos.x > -side):
            ball[i].p.x = abs(ball[i].p.x) * rp
        if not (ball[i].pos.y > -side):
            ball[i].p.y = abs(ball[i].p.y)
            if(abs(ball[i].p.y) > gr):  ball[i].p.y -= gr
            ball[i].p.y *= rp
        if not (ball[i].pos.z > -side):
            ball[i].p.z = abs(ball[i].p.z) * rp

    
        
    







