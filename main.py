import matplotlib.pyplot as plt
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
import mplcyberpunk
from kivy.clock import Clock
import datetime
from info_util import InfoUtil


Window.size = (500, 500)

KV = '''
BoxLayout:
    orientation: 'vertical'
    Image:
        id: img
        source: ''
    # Button:
    #     size_hint_y: 0.2
    #     text: 'Plot'
    #     on_press: app.plot_graph()
'''

class MatplotlibApp(App):
    def build(self):
        info_util = InfoUtil()
        Clock.schedule_interval(lambda dt: self.plot_graph(dt, info_util=info_util), 2)
        return Builder.load_string(KV)

    def update(self, info_util):
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
        ax1.text(0.5, 0.5, current_time, ha='center', va='center', fontsize=350,
                 color=time_color, fontweight='bold', family='monospace', transform=plt.gcf().transFigure, alpha=0.5)

        gold_info = "" if info_util.gold_queue.get_all() == [] else info_util.gold_queue.get_all()[-1]
        ax1.text(0.1, 0.9, gold_info, fontsize=60,
                 color='y', fontweight='bold', family='monospace', transform=plt.gcf().transFigure, alpha=0.5)

        rate_info = "" if info_util.rate_queue.get_all() == [] else info_util.rate_queue.get_all()[-1]
        ax1.text(0.5, 0.9, rate_info, fontsize=60,
                 color='g', fontweight='bold', family='monospace', transform=plt.gcf().transFigure, alpha=0.5)

        # plt.axis('off')



        line_width = 8
        ax1.plot(info_util.time_queue.get_all(),info_util.gold_queue.get_all(), marker='o', linewidth=line_width, color='y')
        # ax1.set_ylabel('gold', color='y')
        ax1.tick_params(axis='y', colors='y')

        ax2 = ax1.twinx()
        ax2.plot(info_util.time_queue.get_all(),info_util.rate_queue.get_all(), marker='o', linewidth=line_width, color='g')
        # ax2.set_ylabel('exchange rate', color='g')
        ax2.tick_params(axis='y', colors='g')
        plt.legend()

        mplcyberpunk.add_glow_effects()


    def plot_graph(self, time, info_util):
        info_util.update_if_need()
        # Create a plot
        self.update(info_util)
        # plt.subplots_adjust(left=0.1, right=0.1, top=0.1, bottom=0.1)

        # Save the plot as a png file
        try:
            plt.savefig('plot.png')
        except Exception as e:
            print(f"Error saving file: {e}")

        # Update the source of the Image widget
        self.root.ids.img.source = 'plot.png'
        self.root.ids.img.reload()  # Ensure the image is reloaded and displayed

if __name__ == '__main__':
    MatplotlibApp().run()