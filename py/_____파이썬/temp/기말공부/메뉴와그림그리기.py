import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import random as rd


win = tk.Tk()

W=600; H=400
colors = ["red", "green", "blue", "cyan", "magenta", "yellow"]

cnv = tk.Canvas(win, width=W, height=H)
cnv.pack()


def paint(event):
    x1, y1=(event.x-1), (event.y+1)
    x2, y2=(event.x+1), (event.y-1)
    cnv.create_oval(x1, y1, x2, y2, fill='black')

cnv.bind("<B1-Motion>", paint)

def hello():
    print ("hello!")

def _open():
    file = fd.askopenfile(parent=win, mode='r')
    if(file != None):
        lines = file.read()
        text.insert('1.0', lines)
        file.close()

def _save():
    file = fd.asksaveasfile(parent=win, mode='w')
    if file != None:
        lines = text.get('1.0', tk.END + '-1c')
        file.write(lines)
        file.close()

def _exit():
    if mb.showinfo('Exit', '종료할까요?'):
        win.destroy()

def _about():
    lbl = mb.showinfo('About', '메모장 프로그램')

def _clear():
    cnv.delete('all')

def _circle():
    for i in range(30):
        x = W * rd.random()
        y = H * rd.random()
        r = 100 * rd.random()
        cnv.create_oval(x-r, y-r, x+r, y+r, fill=colors[i%6])

def _rect():
    for i in range(30):
        x = W * rd.random()
        y = H * rd.random()
        dx = 100 * rd.random()
        dy = 100 * rd.random()
        cnv.create_rectangle(x-dx, y-dy, x+dx, y+dy, fill=colors[i%6])

    
#menubar = tk.Menu(win)
#menubar.add_command(label="Hello", command=hello)
#menubar.add_command(label="Exit", command=win.destroy)

mainmenu = tk.Menu(win)
win.config(menu=mainmenu)

# ‘File’ 메뉴와 서브 메뉴 만들기
filemenu = tk.Menu(mainmenu, tearoff=0)
mainmenu.add_cascade(label="File", menu=filemenu)

filemenu.add_command(label="Open", command=_open)
filemenu.add_command(label="Save", command=_save)
filemenu.add_separator() #구분자 삽입
filemenu.add_command(label="Exit", command=_exit)

#Draw
drawmenu = tk.Menu(mainmenu, tearoff=0)
mainmenu.add_cascade(label="File", menu=drawmenu)
drawmenu.add_command(label='Circle', command=_circle)
drawmenu.add_command(label='Rect', command=_rect)
drawmenu.add_command(label='Clear', command=_clear)


# ‘Help’ 메뉴와 서브 메뉴 만들기
helpmenu = tk.Menu(mainmenu)
mainmenu.add_cascade(label="Help", menu=helpmenu)

helpmenu.add_command(label="Program Info", command=_about)

win.mainloop()
