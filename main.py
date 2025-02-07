import matplotlib.pyplot as plt
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.core.window import Window
import mplcyberpunk

Window.size = (300, 300)

KV = '''
BoxLayout:
    orientation: 'vertical'
    Image:
        id: img
        source: ''
    Button:
        size_hint_y: 0.2
        text: 'Plot'
        on_press: app.plot_graph()
'''

class MatplotlibApp(App):
    def build(self):
        return Builder.load_string(KV)

    def plot_graph(self):
        # Create a plot
        plt.style.use("cyberpunk")

        plt.plot([1, 3, 9, 5, 2, 1, 1], marker='o')
        plt.plot([4, 5, 5, 7, 9, 8, 6], marker='o')

        mplcyberpunk.add_glow_effects()

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