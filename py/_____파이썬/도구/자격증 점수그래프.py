import numpy as np
import matplotlib.pyplot as plt
from math import *


# 점수를 뒤에 추가
score = [[None, None, None],
         [53, None, None],
         [57, None, None],
         [57, None, None],
         [58, None, None],
         [51, 52, 50],
         [None, None, 44],
         [None, None, 69],
         [None, None, 66],
         [None, None, 71],
         [None, 66, 62],
         [None, 62, 87],
         [None, None, 62],
         [None, None, 68],
         [None, None, 68],
         [None, None, 71],
         [None, None, 71],
         [None, None, 75],
         [None, None, 75],  # 0906
         [None, None, 59],  # 0912
         [None, None, 71],  # 0913
         [None, 54, 75],    # 0914
         [None, 58, 59],    # 0920
         [None, 81, 78],    # 0920
         [None, None, 78],  # 0920
         [75, 72, 78],      # 0921
         [None, None, None]
         ]

score = np.array(score)
score = score.T



plt.axis([1,len(score[0]),0,100])
plt.plot(range(1,len(score[0])+1), score[0],'go-')
plt.plot(range(1,len(score[0])+1), score[1], 'yo:')
plt.plot(range(1,len(score[0])+1), score[2], 'bo:')

plt.show()

