import numpy as np
import matplotlib.pyplot as plt

x1 = np.arange(-3, 3, 0.1)
y1 = [128*(x**7) - 1334*(x**5) + 3360*(x**3) - 1680*x for x in x1]

plt.axis([-3,3,-7000,7000])
plt.plot(x1, y1)
plt.show()
