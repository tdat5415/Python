import numpy as np

s = [[1,2,3],
     [4,5,6],
     [0,9,0]]

s = np.array(s)

print(s)

base = 2
s = np.log(s+1) / np.log(base)

print(s)


s.round(5)

print(s)
