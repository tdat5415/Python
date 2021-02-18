from tkinter import *
import time
from random import *



class Ball:
    def __init__(self, canvas, color, size, x, y, vx, vy):#생성자
        self.canvas = canvas
        self.color = color
        self.size = size #반지름
        self.x = x  #위치
        self.y = y
        self.vx = vx #속도
        self.vy = vy
        self.id = canvas.create_oval(x,y,x+size,y+size,fill=color)
         
    def move(self): #공을 이동시키는 함수
        self.canvas.move(self.id, self.vx, self.vy)
        (x1,y1,x2,y2) = self.canvas.coords(self.id) #공의 현재 위치 얻음
        (self.x, self.y) = (x1, y1)
        if x1 <= 0 or x2 >= Width: #공이 x축 경계를 넘으면
            self.vx = - self.vx #x-축 운동 방향을 바꾼다.
        if y1 <= 0 or y2 >= Height: #공이 y축 경계를 넘으면
            self.vy = - self.vy #y-축 운동 방향을 바꾼다.



        

win = Tk()
Width = 600; Height = 400

cvs = Canvas(win, width = Width, height = Height)
cvs.pack()

colors = ["red", "green", "blue", "cyan", "magenta", "yellow",
            "black", "gray","gold","pink"] 

balls = [ ]
for i in range(10):
    x = random()*Width; y = random()*Height;
    vx = random()*20; vy = random()*20;
    balls.append(Ball(cvs, colors[i%10], 30, x, y, vx, vy))


while True:
    for ball in balls:
        ball.move()
    win.update()
    time.sleep(0.03)

win.mainloop()
