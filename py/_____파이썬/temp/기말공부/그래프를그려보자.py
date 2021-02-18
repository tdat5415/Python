import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 11, 1)

y1 = np.random.rand(11)#0~1사이
y2 = np.random.randn(11)#표준정규분포
y3 = np.random.randn(11)

plt.plot(x, y1, color='red', linestyle='--', marker='+')
plt.plot(x, y2, c='g', ls='-.')
plt.plot(x, y3, c=(0.5, 0.1, 0.3, 0.1)) #c=(빨,초,파,투명도)
plt.show()

