import tkinter as tk

win = tk.Tk()

#창 크기와 왼쪽 모서리 위치(WxH+x+y) 
win.geometry("320x200+50+50")
win.resizable(True, False)


lbl = tk.Label(win, text='이름')
txt = tk.Entry(win)
btn = tk.Button(win, text='ok', width=15)

'''
#격자 배치하기
lbl.grid(row=2, column=0)
txt.grid(row=1, column=1)
btn.grid(row=0, column=2)
'''

# 절대위치 배치하기
lbl.place(x=100, y=0)
txt.place(x=150, y=50)
btn.place(x=200, y=100)




win.mainloop()
