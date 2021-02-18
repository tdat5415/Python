import tkinter as tk

# Tk 객체 인스턴스 생성
win = tk.Tk()

# Canvas 객체 인스턴스 생성(너비는 500, 높이는 500)
cnv = tk.Canvas(win, width = 500, height = 500)
cnv.pack()    # Canvas 배치

# 선을 그림: 좌표(0, 0)에서 (50, 50), 색은 검정
cnv.create_line(0, 0, 50, 50, fill="blue", width=3)

# 사각형을 그림: 좌표(100, 100)에서 (150, 150), 색은 빨강
cnv.create_rectangle(100, 100, 150, 150, fill = 'red')

# 원을 그림: 좌표(100, 200)에서 (150, 250), 색은 파랑
cnv.create_oval(100, 200, 150, 250, width=3, outline="red", fill="green")

# 다각형을 그림: 8개 좌표를 연결한 팔각형, 색은 녹색
#points = [250, 200, 350, 200, 400, 250, 400, 350, 350, 400, 250, 400, 200, 350, 200, 250]
cnv.create_polygon(250, 200, 350, 200, 400, 250, 400, 350, 350, 400, 250, \
                   400, 200, 350, 200, 250, fill = 'green')

win.mainloop()
