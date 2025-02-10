import matplotlib.pyplot as plt
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
import mplcyberpunk
from kivy.clock import Clock

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
        Clock.schedule_interval(self.plot_graph, 2)
        return Builder.load_string(KV)
    def plot_graph(self, time):
        print(123)
        # Create a plot
        plt.rcParams['font.size'] = 35
        plt.style.use("cyberpunk")

        # set the plt size same as the window
        plt.figure(figsize=(20, 11), constrained_layout=True)

        line_width = 8
        plt.plot([1, 3, 9, 5, 2, 1, 1], marker='o', linewidth=line_width, label="gold price")
        plt.plot([4, 5, 5, 7, 9, 8, 6], marker='o', linewidth=line_width, label="dollar price")
        plt.legend()

        mplcyberpunk.add_glow_effects()
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