import pandas as pd
import random as rd
import matplotlib.pyplot as plt

SIZE = 1000

data = [rd.randint(0,1) for i in range(SIZE)]

counts = [0] * (SIZE+1)
N = 0

for n in data:
    if n == 1:
        N += 1
        continue
    else:
        counts[N] += 1
        N = 0
counts[N] += 1

#print(data)
for i in range(1, 11):#range(1, SIZE+1):
    print('%d회 : ' % i, counts[i])
