from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.widget import Widget

class FirstWindow(Screen):
    pass
class SecondWindow(Screen):
    pass
class WindowManager(ScreenManager):
    pass

#Window.size=(400,400)
kv=Builder.load_file("window.kv")
class Root(Widget):
    pass
class MainApp(App):
    def build(self):
        return kv
if __name__=="__main__":
    MainApp().run()