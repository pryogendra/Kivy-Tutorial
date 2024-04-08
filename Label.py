from kivy.app import App
from kivy.uix.label import Label


class LabelApp(App):
    def build(self):
        return Label(text="Hello World",font_size=42)

if __name__=="__main__":
    LabelApp().run()
