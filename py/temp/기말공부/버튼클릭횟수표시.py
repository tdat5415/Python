import tkinter as tk

win = tk.Tk()
win.title("숫자 세기")
win.geometry("300x50+100+100")
num=0

def count():
    global num
    num +=1
    lbl.config(text = num)

lbl = tk.Label(win, text="횟수")
lbl.pack()
btn = tk.Button(win, text="click", command=count,
                overrelief="solid", width=15, repeatdelay=1000, repeatinterval=10)
btn.pack()
win.mainloop()
