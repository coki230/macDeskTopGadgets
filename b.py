import matplotlib.pyplot as plt
import datetime

import mplcyberpunk


def update():
    # Create a plot
    # set the plt size same as the window
    fig = plt.figure(figsize=(20, 11), constrained_layout=True)
    plt.rcParams['font.size'] = 35
    plt.style.use("cyberpunk")

    plt.clf()  # 清除当前图形
    current_time = datetime.datetime.now().strftime('%H:%M')
    now = datetime.datetime.now()
    microseconds = now.microsecond
    milliseconds = microseconds // 1000
    last_two_digits = milliseconds % 100

    # 设置文本属性

    ax1 = fig.add_subplot(111)  # 添加一个轴
    time_color = plt.cm.spring(last_two_digits / 99)  # 生成基于时间的彩色效果
    ax1.text(0.5, 0.5, current_time, ha='center', va='center', fontsize=150,
             color=time_color, fontweight='bold', family='monospace', transform=plt.gcf().transFigure, alpha=0.5)

    # plt.axis('off')



    line_width = 8
    ax1.plot([1, 3, 9, 5, 2, 1, 1,1, 3, 9, 5, 2, 1, 1], marker='o', linewidth=line_width, color='y')
    # ax1.set_ylabel('gold', color='y')
    ax1.tick_params(axis='y', colors='y')

    ax2 = ax1.twinx()
    ax2.plot([40, 50, 50, 70, 90, 80, 60,40, 50, 50, 70, 90, 80, 60], marker='o', linewidth=line_width, color='g')
    # ax2.set_ylabel('exchange rate', color='g')
    ax2.tick_params(axis='y', colors='g')
    plt.legend()

    # mplcyberpunk.add_glow_effects()

update()
plt.show()