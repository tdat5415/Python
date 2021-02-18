import tkinter as tk

win = tk.Tk()
win.geometry("320x240+100+100")
win.resizable(False, False)

def flash():
    chb1.flash()


CheckVar1=tk.IntVar()
CheckVar2=tk.IntVar()

chb1=tk.Checkbutton(win, text="O", variable=CheckVar1, activebackground="blue")
chb2=tk.Checkbutton(win, text="△", variable=CheckVar2)
chb3=tk.Checkbutton(win, text="X", variable=CheckVar2, command=flash)

chb1.pack()
chb2.pack()
chb3.pack()
win.mainloop()
