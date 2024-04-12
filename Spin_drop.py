from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.widget import Widget

#Window.size=(400,400)
Builder.load_file("spin_drop.kv")
class Root(Widget):
    def clicked(self,value):
        self.ids.label.text=value
class MainApp(App):
    def build(self):
        return Root()
if __name__=="__main__":
    MainApp().run()