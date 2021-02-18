import matplotlib.pyplot as plt
import pandas_datareader.data as web

sk_hynix = web.DataReader("000660.KS", "yahoo")

#그래프가 들어갈 상자 두개 넣음
fig = plt.figure(figsize=(12, 8))
top_axes = plt.subplot2grid((4,4), (0,0), rowspan=3, colspan=4)
bottom_axes = plt.subplot2grid((4,4), (3,0), rowspan=1, colspan=4)

#지수형태로 표시되지않게 
bottom_axes.get_yaxis().get_major_formatter().set_scientific(False)


top_axes.plot(sk_hynix.index, sk_hynix['Adj Close'], label='Adjusted Close')
bottom_axes.plot(sk_hynix.index, sk_hynix['Volume'])

#자동으로 최대 크기로
plt.tight_layout()
plt.show()
