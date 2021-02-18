import numpy as np
import matplotlib.pyplot as plt
from math import *


def f(x):
    return 128*(x**7) - 1334*(x**5) + 3360*(x**3) - 1680*x

def df(x):
    return 128*7*(x**6) - 1334*5*(x**4) + 3360*3*(x**2) - 1680


eps = 0.001#한계
x = np.arange(-3, 3, eps)
y = [f(i) for i in x]
'''
plt.plot(x, f(x),'g-')
plt.plot(x, df(x),'r--')

#뉴턴-랩슨법
x0 = 0.#초기값
eps = 1.0e-5 #계산한계

while True:
    x1 = x0 - f(x0)/df(x0)
    print (x1, abs(x1-x0)/2)
    if abs(x1-x0) < eps:
        break
    x0 = x1
    plt.plot(x0, 0, 'o')
plt.show()
'''

tmp = 0
if y[0] > 0:
    tmp = 1
else:
    tmp = 0
    
for i in range(0, len(y)):
    if y[i] > 0:
        if tmp != 1:
            plt.plot(x[i], 0, 'o')
            print(x[i])
            tmp = 1
    else:
        if tmp != 0:
            plt.plot(x[i], 0, 'o')
            print(x[i])
            tmp = 0

plt.axis([-3,3,-7000,7000])
plt.plot(x, f(x),'g-')
plt.show()
