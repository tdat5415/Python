import tkinter as tk

win = tk.Tk()
lbl = tk.Label(win, text='Hi!')
lbl.pack()

win.title('윈도우 창')
win.geometry("640x400+100+100") 
win.resizable(True, False)

b = [None]*3
b[0]=tk.Button(win, text="btn1")
b[1]=tk.Button(win, text="btn2")
b[2]=tk.Button(win, text="btn3") 
for a in b:
    a.pack(side=tk.RIGHT)

win.mainloop()
win.destroy()
