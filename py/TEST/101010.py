import pandas as pd
import random as rd
import matplotlib.pyplot as plt
import threading as thr

SIZE = 99
dep = 3
total = [0]*(dep+1)
total1 = 0
total2 = 0
total3 = 0
total4 = 0

#print(SIZE//2+1)
def cel():
    t = 0
    for i in range(SIZE):
        t += rd.randint(0,1)
    return t

def rcsv(depth):
    if depth == 0:
        return cel()
    else:
        tot = 0
        for i in range(SIZE):
            tot += rcsv(depth-1)//(SIZE//2 +1)
        return tot

total[dep] = rcsv(dep)
        
'''
def th():
    global total
    total[4] = 0
    for l in range(SIZE):
        total[3] = 0
        for g in range(SIZE):
            total[2] = 0
            for h in range(SIZE):
                total[1] = 0
                for j in range(SIZE):
                    total[0] = 0
                    for i in range(SIZE):
                        total[0] += rd.randint(0,1)
                    total[1] += total[0]//(SIZE//2 +1)
                total[2] += total[1]//(SIZE//2 +1)
            total[3] += total[2]//(SIZE//2 +1)
        total[4] += total[3]//(SIZE//2 +1)
    total[5] += total[4]//(SIZE//2 +1)
    
    


obj = None
for k in range(SIZE):
    obj = thr.Thread(target=th)
    obj.start()
obj.join()

'''
'''
for l in range(SIZE):
    total[4] = 0
    for k in range(SIZE):
        total[3] = 0
        for g in range(SIZE):
            total[2] = 0
            for h in range(SIZE):
                total[1] = 0
                for j in range(SIZE):
                    total[0] = 0
                    for i in range(SIZE):
                        total[0] += rd.randint(0,1)
                    total[1] += total[0]//(SIZE//2 +1)
                total[2] += total[1]//(SIZE//2 +1)
            total[3] += total[2]//(SIZE//2 +1)
        total[4] += total[3]//(SIZE//2 +1)
    total[5] += total[4]//(SIZE//2 +1)
   '''

labels = ['1','0']
sizes = [total[dep]/SIZE*100, (SIZE-total[dep])/SIZE*100]
colors = ['red', 'blue']

plt.title("Pie Chart")
plt.pie(sizes, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.show()

plt.show()
