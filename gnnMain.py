from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


def callback(instance):
    print("BUTTON PRESSED!")


class StartScreen(PageLayout):

    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)


class gnnModernApp(App):
    def build(self):
        return StartScreen()


if __name__ == "__main__":
    gnnModernApp().run()
