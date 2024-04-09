from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget

Builder.load_file("font.kv")
class MainW(Widget):
    pass
class FontApp(App):
    title ="Font Color"
    def build(self):
        return MainW()

if __name__=="__main__":
    FontApp().run()