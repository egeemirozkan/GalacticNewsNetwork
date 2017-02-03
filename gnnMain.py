from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


def callback(instance):
    print("BUTTON PRESSED!")


class StartScreen(GridLayout):

    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)
        self.cols = 1
        self.titleLabel = Label(text="Galactic News Network",
                                font_size="20sp")
        self.explainitoryText = Label(text="Alpha Centauri is roughly 4 Ligh"
                                      "tyears away from us Earthlings. This me"
                                      "ans any news we make will reach them fo"
                                      "ur years due, so, how would it looked l"
                                      "ike then?")
        self.lookButton = Button(text="Let's Learn!")
        self.lookButton.bind(on_press=callback)
        self.add_widget(self.titleLabel)
        self.add_widget(self.explainitoryText)
        self.add_widget(self.lookButton)


class gnnModernApp(App):
    def build(self):
        return StartScreen()


if __name__ == "__main__":
    acdnModernApp().run()
