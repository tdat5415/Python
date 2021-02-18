import tkinter as tk

win = tk.Tk()

lbl1 = tk.Label(win, text = '입력1 : ')
lbl2 = tk.Label(win, text = '입력2 : ')
lbl3 = tk.Label(win, text = '출력 : ')

lbl1.grid(row=0, column=0)
lbl2.grid(row=1, column=0)
lbl3.grid(row=2, column=0)

ent1 = tk.Entry(win, bg = 'yellow', fg = 'blue')
ent2 = tk.Entry(win, bg = 'yellow', fg = 'blue')
ent3 = tk.Entry(win, bg = 'yellow', fg = 'blue')

ent1.grid(row=0, column=1)
ent2.grid(row=1, column=1)
ent3.grid(row=2, column=1)

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

btn1 = tk.Button(win, text = '+', command=_add)
btn2 = tk.Button(win, text = '-', command=_sub)
btn3 = tk.Button(win, text = '*', command=_mul)
btn4 = tk.Button(win, text = '/', command=_div)

btn1.grid(row=3, column=0)
btn2.grid(row=4, column=0)
btn3.grid(row=5, column=0)
btn4.grid(row=6, column=0)

win.mainloop()
