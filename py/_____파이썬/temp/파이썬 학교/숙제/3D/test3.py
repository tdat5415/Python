from vpython import *
import random as rd

scene.caption = """Right button drag or Ctrl-drag to rotate "camera" to view scene.
To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
     On a two-button mouse, middle is left + right.
Shift-drag to pan left/right and up/down.
Touch screen: pinch/extend to zoom, swipe or two-finger rotate."""



ballSize = 1.5
side = 4.0
thk = 0.3
s2 = 2*side - thk
s3 = 2*side + thk

wallR = box (pos=vector( side, 0, 0), size=vector(thk, s2, s3),  color = color.red)
wallL = box (pos=vector(-side, 0, 0), size=vector(thk, s2, s3),  color = color.red)
wallB = box (pos=vector(0, -side, 0), size=vector(s3, thk, s3),  color = color.blue)
wallT = box (pos=vector(0,  side, 0), size=vector(s3, thk, s3),  color = color.blue)
wallBK = box(pos=vector(0, 0, -side), size=vector(s2, s2, thk), color = color.gray(0.7))

ball = sphere (color = color.red, radius = ballSize)
ball.mass = 1.0
ball.p = vector (0, 0, 0)#rd.random()-0.5)

ball2 = sphere (color = color.red, radius = ballSize)
ball2.mass = 1.0
ball2.p = vector (0, rd.random()-0.5, 0)#rd.random()-0.5)

side = side - thk*0.5 - ball.radius

ball.pos.y = 2
ball2.pos.y = -2

dt = 0.3

rp = repulsion = 1#0.95 # 반발계수

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
    #return v1+fromV2ToV1, v2+fromV1ToV2


while True:
    rate(30)
    ball.pos = ball.pos + (ball.p/ball.mass)*dt
    ball2.pos = ball2.pos + (ball2.p/ball2.mass)*dt
    
    #ball.p.y -= 0.08
    #ball2.p.y -= 0.08

    if disBall(ball,ball2) <= ballSize*2:
        ball.p, ball2.p = symmetryBalls(ball.p,ball2.p,ball.pos,ball2.pos)
        ball.p *= rp*rp*rp
        ball2.p *= rp*rp*rp
    
    if not (side > ball.pos.x):
        ball.p.x = -abs(ball.p.x) * rp
    if not (side > ball.pos.y):
        ball.p.y = -abs(ball.p.y) * rp
    if not (side > ball.pos.z):
        ball.p.z = -abs(ball.p.z) * rp
    if not (ball.pos.x > -side):
        ball.p.x = abs(ball.p.x) * rp
    if not (ball.pos.y > -side):
        ball.p.y = abs(ball.p.y); #ball.p.y -= 0.08; ball.p.y *= rp
    if not (ball.pos.z > -side):
        ball.p.z = abs(ball.p.z) * rp
        
    if not (side > ball2.pos.x):
        ball2.p.x = -abs(ball2.p.x) * rp
    if not (side > ball2.pos.y):
        ball2.p.y = -abs(ball2.p.y) * rp
    if not (side > ball2.pos.z):
        ball2.p.z = -abs(ball2.p.z) * rp
    if not (ball2.pos.x > -side):
        ball2.p.x = abs(ball2.p.x) * rp
    if not (ball2.pos.y > -side):
        ball2.p.y = abs(ball2.p.y); #ball2.p.y -= 0.08; ball2.p.y *= rp
    if not (ball2.pos.z > -side):
        ball2.p.z = abs(ball2.p.z) * rp
    
        
    







