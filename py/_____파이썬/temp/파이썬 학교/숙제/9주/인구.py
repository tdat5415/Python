import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file_path='2018.12.31.기준 대구광역시 주민등록인구 현황(구군별 연령별 성별).csv'
df = pd.read_csv(file_path, encoding='cp949')

df2 = pd.DataFrame({'c1':list(df[' 총계 ']), 'c2':list(df[' 총계 남 ']), 'c3':list(df[' 총계 여 '])})
df2.columns = ['total', 'men', 'women']

                    
df2.plot()
plt.show()
