import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot(2, 1, 1) # 가로 x 세로  첫번째
ax2 = fig.add_subplot(2, 1, 2)

x = range(0, 100)
y = [v*v for v in x]

ax1.plot(x, y)  #선 그래프
ax2.bar(x, y)   #막대 그래프


plt.show()
