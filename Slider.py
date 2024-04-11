from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.widget import Widget

#Window.size=(400,400)
Builder.load_file("slider.kv")
class Root(Widget):
    def slided(self,*args):
        print(args[1])
        self.ids.label.text=str(args[1])
        self.ids.label.font_size=20+int(args[1]*2)
class MainApp(App):
    def build(self):
        return Root()
if __name__=="__main__":
    MainApp().run()