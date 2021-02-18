from tkinter import *

def paint(event):
    x1, y1=(event.x-1), (event.y+1)
    x2, y2=(event.x+1), (event.y-1)
    cnv.create_oval(x1, y1, x2, y2, fill=mycolor)
    
def change_color( ):
    global mycolor
    mycolor = "red"

mycolor = "blue"

win = Tk()

cnv = Canvas(win, width=300, height=200)
cnv.pack()
cnv.bind("<B1-Motion>", paint)

btn = Button(win, text="빨강색", command=change_color)
btn.pack()

win.mainloop()
