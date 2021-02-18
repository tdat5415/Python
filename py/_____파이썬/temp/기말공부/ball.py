from tkinter import *

class Ball:
     def __init__(self, canvas, color, size, x, y, vx, vy):#생성자
         self.canvas = canvas
         self.color = color
         self.size = size #반지름
         self.x = x  #위치
         self.y = y
         self.vx = vx #속도
         self.vy = vy
         canvas.create_oval(x,y,x+size,y+size,fill=color)
         
def move(self): #공을 이동시키는 함수
    pass #보류

win = Tk()
W = 600; H = 400

cvs = Canvas(win, width = W, height = H)#.pack()
cvs.pack()

ball1 = Ball(cvs, "red", 30, 100, 100, 0, 0)
ball2 = Ball(cvs, "blue", 30, 500, 300, 0, 0)
win.mainloop()
