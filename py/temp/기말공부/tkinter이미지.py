import tkinter as tk

win = tk.Tk()
win.geometry("640x400+100+100")
win.resizable(True, True)
W = 600
H = 400

cnv = tk.Canvas(win, width = W, height = H)
cnv.pack()


img = tk.PhotoImage(file="치킨.jpg")

cnv.create_image(0, 0, anchor=tk.NW, image=img)
#lbl = tk.Label(win, image=img)
#lbl.pack()



win.mainloop()
