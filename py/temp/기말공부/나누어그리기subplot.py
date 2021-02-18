import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 5, 0.01)

plt.subplot(221)
plt.plot(x, x**2, 'r--')

plt.subplot(222)
plt.plot(x, 2**x, 'g-')

plt.subplot(223)
plt.plot(x, x, 'b')

plt.subplot(224)
plt.plot(x, 1/(x+1), 'c')

plt.show()
