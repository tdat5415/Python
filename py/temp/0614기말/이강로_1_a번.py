import pandas as pd
import random as rd

data = [rd.randint(0,1) for i in range(1000)]

s = pd.Series(data)

print(s)
