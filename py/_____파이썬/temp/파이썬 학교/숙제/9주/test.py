import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame([1000, 2000, 3000, 4000])
#df = pd.DataFrame([1000, 2000, 3000, 4000], index=["i1", "i2", "i3", "i4"])
#df = pd.DataFrame({"c1":[1000, 2000, 3000, 4000]}, index=["i1", "i2", "i3", "i4"])



df.columns = ["c1"]

df.plot()
plt.show()

