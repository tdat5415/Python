import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 11, 1)

y1 = np.random.rand(11)
plt.plot(x, y1, 'bo-', label = 'rand')      #파랑에 동글이에 -모양 
# 'color marker linestyle'
y2 = np.random.randn(11)
plt.plot(x, y2, 'gs--', label = 'randn')    #초록에 네모에 --모양

plt.axis([0, 10, -2, 2])    #좌표축 범위 설정
plt.xlabel('x')             #x축 제목
plt.ylabel('y')             #y축 제목
plt.title('Two graphs')     #타이틀 설정

plt.grid(True)              #격자 눈금 표시
plt.legend()                #범례 표시
plt.show()
