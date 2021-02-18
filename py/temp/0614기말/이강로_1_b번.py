import pandas as pd
import random as rd
import matplotlib.pyplot as plt

SIZE = 1000

data = [rd.randint(0,1) for i in range(SIZE)]

s = pd.Series(data)



labels = ['1','0']
sizes = [data.count(1)/SIZE*100, data.count(0)/SIZE*100]
colors = ['red', 'blue']

plt.title("Pie Chart")
plt.pie(sizes, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.show()


