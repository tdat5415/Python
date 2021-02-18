import tkinter as tk

win = tk.Tk()

lbl1 = tk.Label(win, text = "화씨")
lbl2 = tk.Label(win, text = "섭씨")
lbl1.grid(row=0, column=0)
lbl2.grid(row=1, column=0)

ent1 = tk.Entry(win, bg = "yellow", fg = "blue")
ent2 = tk.Entry(win, bg = "yellow", fg = "blue")
ent1.grid(row=0, column=1)
ent2.grid(row=1, column=1)

def convFC():
    tempF = float(ent1.get())
    tempC = (tempF-32)*5/9
    ent2.delete(0, tk.END)
    ent2.insert(0, tempC)
    
def convCF():
    tempC = float(ent2.get())
    tempF = tempC*9/5+32
    ent1.delete(0, tk.END)
    ent1.insert(0, tempF)
    
btn1 = tk.Button(win, text = "화씨->섭씨", command=convFC)
btn2 = tk.Button(win, text = "섭씨->화씨", command=convCF)
btn1.grid(row=2, column=0)
btn2.grid(row=2, column=1)

win.mainloop()
