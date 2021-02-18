from mylibs import sbox as sb
import numpy as np





m = [[2,3,1,1],
         [1,2,3,1],
         [1,1,2,3],
         [3,1,1,2]]

m[0], m[1], m[2], m[3] = m[1], m[2], m[3], m[0]
print(m)

A = [1,2,3,4]

S = list(map(int,A))
print(S)
print(S[0])
