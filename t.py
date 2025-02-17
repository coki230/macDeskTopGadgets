import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7]
y1 = ['5', '6', '7', '8', '2', '3', '4']
y2 = ['2', '3', '4', '5', '6', '7', '8']

y1 = [int(i) for i in y1]
y2 = [int(i) for i in y2]

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y1, label='Line 1')
ax2 = ax.twinx()
ax2.plot(x, y2, label='Line 2')
ax.legend()
ax2.legend()
plt.show()