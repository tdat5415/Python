import tkinter as tk

win = tk.Tk()
win.title("Text Widget")
win.geometry("320x100+100+100")
win.resizable(True, True)

text = tk.Text(win)

text.insert('1.0', "텍스트 실습을 합니다.\n")
text.insert('2.0', "두번째 줄입니다.\n")
text.insert('3.0', "세번째 줄입니다.\n")
text.pack()

win.mainloop()
