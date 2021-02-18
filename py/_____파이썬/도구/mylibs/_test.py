import sbox as sb
import numpy as np
import time as t


ENC = 1
DEC = 0

A = [[2,3,1,1],
     [1,2,3,1],
     [1,1,2,3],
     [3,1,1,2]]
A = np.matrix(A)
A = A.I
#print(A)


T = np.array([[0x87, 0xf2, 0x4d, 0x97],
                  [0x6e, 0x4c, 0x90, 0xec],
                  [0x46, 0xe7, 0x4a, 0xc3],
                  [0xa6, 0x8c, 0xd8, 0x95]])
T = T.reshape(16)
T = np.array(list(map(sb.S_box,T,[DEC]*16)))


#raise Exception('tesasdfasdfasdf')


A = [1,2,3,4]

for v in A[1:]:
    print(v)

print(2**128)
