import numpy as np

A = np.matrix([[15,2,3,4,5],
               [1,10,1,3,0],
               [3,2,10,0,4],
               [0,3,5,15,1],
               [1,1,1,1,5]])

B = np.matrix([20,15,12,10,14])

X = A.I * B.T
print(X)
