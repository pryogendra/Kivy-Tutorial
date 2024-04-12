from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.widget import Widget

#Window.size=(400,400)
Builder.load_file("tab.kv")
class Root(TabbedPanel):
    pass
class MainApp(App):
    def build(self):
        return Root()
if __name__=="__main__":
    MainApp().run()