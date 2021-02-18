from turtle import *
from random import choice, random
class MyTurtle(Turtle):
    # 파생클래스 ← Turtle 클래스
    def glow(self, x, y):
        clr = ["red","green","blue",]
        self.fillcolor(choice(clr)) #random(),random(),random())
        self.goto(x,y)
        
#Turtle 객체
ttl = Turtle()
ttl.shape("turtle")
ttl.shapesize(3,3)

#MyTurtle 객체
ttA = MyTurtle()
ttA.shape("turtle")
ttA.shapesize(3,3)
# ttA.glow(100,100)
ttA.onclick(ttA.glow)
