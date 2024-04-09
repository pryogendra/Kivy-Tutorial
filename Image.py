from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget

Builder.load_file("image.kv")
class ImageW(Widget):
    pass
class ImageApp(App):
    def build(self):
        return ImageW()
if __name__=="__main__":
    ImageApp().run()