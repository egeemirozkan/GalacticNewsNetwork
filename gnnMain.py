from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

Window.clearcolor = (1, 0.97, 0.90, 0.5)

class StartScreen(FloatLayout):
    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)

class gnnModernApp(App):
    def build(self):
        return StartScreen()


if __name__ == "__main__":
    gnnModernApp().run()
