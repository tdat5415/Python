import pandas as pd
import numpy as np

data = {
    'year' : [2016, 2017, 2018],
    'GDP rate' : [2.8, 3.1, 3.0],
    'GDP' : ['1.637M', '1.73M', '1.83M']
    }

df = pd.DataFrame(data)




df =pd.DataFrame(np.arange(12).reshape(3,4), columns=['A', 'B', 'C', 'D'])

print(df)

df.to_csv('testfile/test2.csv')
