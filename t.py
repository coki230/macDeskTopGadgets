import matplotlib.pyplot as plt
import numpy as np

# 创建图形和一个子图
fig, ax1 = plt.subplots()

# 数据集1（使用ax1）
x = np.linspace(0, 10, 100)
y1 = x**2
ax1.plot(x, y1, 'b-', label='x^2')  # 蓝色线表示x平方
ax1.set_xlabel('X')
ax1.set_ylabel('x^2', color='b')
ax1.tick_params(axis='y', colors='b')

# 创建一个共享X轴的新轴
ax2 = ax1.twinx()

# 数据集2（使用ax2）
y2 = np.exp(x)
ax2.plot(x, y2, 'r-', label='exp(x)')  # 红色线表示e的x次方
ax2.set_ylabel('exp(x)', color='r')
ax2.tick_params(axis='y', colors='r')

# 设置图例
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# 设置标题
plt.title('Double Y Axis Example')

# 显示图形
plt.show()