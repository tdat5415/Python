import tkinter as tk

# Tk 객체 인스턴스 생성 
root = tk.Tk()

# 슬라이드 바의 값을 저장할 Variable 객체 생성(정수형) 
val = tk.IntVar()
val.set(0)

# 손잡이를 움직였을 때 처리 
def func(scl):
    label.config(text='Value = %d' % int(scl))

# 슬라이드 바의 값을 표시하는 라벨 생성
label = tk.Label(root, text = 'Value = %d' % val.get())
label.pack()    # 라벨 배치

# 슬라이드 바 생성: Scale 라벨 표시. 수평으로 숫자 범위는 0에서 100까지
s = tk.Scale(root, label = 'Scale', orient = 'h', from_ = 0, to = 100, 
             showvalue = True, variable = val, command = func)
s.pack()    # 슬라이드 바 배치

# root 표시
root.mainloop()
