import tkinter as tk

win = tk.Tk()
win.geometry("320x200+50+50")

lbl1 = tk.Label(win, text = 'a = ')
lbl2 = tk.Label(win, text = 'b = ')
lbl3 = tk.Label(win, text = '결과 = ')
lbl1.place(x=40, y=0)
lbl2.place(x=40, y=20)
lbl3.place(x=25, y=80)

ent1 = tk.Entry(win, bg = 'yellow', fg = 'blue')
ent2 = tk.Entry(win, bg = 'yellow', fg = 'blue')
ent3 = tk.Entry(win, bg = 'yellow', fg = 'blue')
ent1.place(x=70, y=0)
ent2.place(x=70, y=20)
ent3.place(x=70, y=80)

def _add():
    inp1 = float(ent1.get())
    inp2 = float(ent2.get())
    ent3.delete(0, tk.END)
    ent3.insert(0, inp1+inp2)

def _sub():
    inp1 = float(ent1.get())
    inp2 = float(ent2.get())
    ent3.delete(0, tk.END)
    ent3.insert(0, inp1-inp2)

def _mul():
    inp1 = float(ent1.get())
    inp2 = float(ent2.get())
    ent3.delete(0, tk.END)
    ent3.insert(0, inp1*inp2)

def _div():
    inp1 = float(ent1.get())
    inp2 = float(ent2.get())
    ent3.delete(0, tk.END)
    ent3.insert(0, inp1/inp2)

def _can():
    ent1.delete(0, tk.END)
    ent2.delete(0, tk.END)
    ent3.delete(0, tk.END)

btn1 = tk.Button(win, text = '+', command=_add)
btn2 = tk.Button(win, text = '-', command=_sub)
btn3 = tk.Button(win, text = 'x', command=_mul)
btn4 = tk.Button(win, text = '/', command=_div)
btn5 = tk.Button(win, text = 'c', command=_can)
btn1.place(x=70, y=40)
btn2.place(x=100, y=40)
btn3.place(x=130, y=40)
btn4.place(x=160, y=40)
btn5.place(x=220, y=80)

win.mainloop()
