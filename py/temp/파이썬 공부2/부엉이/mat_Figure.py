import matplotlib.pyplot as plt

#fig = plt.figure()

#ax = fig.add_subplot(111)

fig, ax_list = plt.subplots(2, 2)


ax_list[0][0].plot([1,2,3,4])

plt.show()
