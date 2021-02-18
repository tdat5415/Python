import tkinter as tk
import random as rd

win = tk.Tk()

colors=["red", "purple", "blue", "green", "yellow", "orange"]

W = 600
H = 400

cnv = tk.Canvas(win, width = W, height = H)
cnv.pack()

for i in range(20):
    x = W * rd.random()
    y = H * rd.random()
    r = 100 * rd.random()
    cnv.create_oval(x, y, x+r, y+r, fill = colors[i%6])


win.mainloop()
