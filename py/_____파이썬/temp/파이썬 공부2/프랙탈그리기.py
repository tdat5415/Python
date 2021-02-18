from turtle import *

x = -200
y = 000

def practal1(len,dep):
	penup()
	goto(x, y)
	pendown()
	for i in range(3):
		Koch(len, dep)
		right(120)

def practal2(len, dep):
	penup()
	goto(x, y)
	pendown()
	color("black")
	begin_fill()
	for i in range(3):
		fd(len)
		left(120)
	end_fill()
	for i in range(1,dep+1):
		penup()
		goto(x, y)
		pendown()
		Koch2(len, i)
		

def drawSpiral(d):
	if d > 0:
		fd(d)
		left(90)
		drawSpiral(d-5)

def Koch(length, depth):
	if depth==0:
		forward(length)
	else:
		Koch(length/3, depth-1)
		left(60); Koch(length/3, depth-1)
		right(120); Koch(length/3, depth-1)
		left(60); Koch(length/3, depth-1)

def Koch2(length, depth):
	if depth==0:
		forward(length)
	else:
		Koch2(length/2, depth-1)
		color("white")
		begin_fill()
		left(120); fd(length/2)
		right(120); Koch2(length/2, depth-1)
		right(120); fd(length/2)
		end_fill()
		left(120); Koch2(length/2, depth-1)

speed(0)

#drawSpiral(100)
#practal1(200, 5)
practal2(400, 5)
