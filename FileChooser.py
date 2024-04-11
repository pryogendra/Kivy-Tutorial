from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.widget import Widget

#Window.size=(400,400)
Builder.load_file("file_chooser.kv")
class Root(Widget):
    def selected(self,filename):
        try:
            self.ids.img.source=filename[0]
        except:
            pass
class MainApp(App):
    def build(self):
        return Root()
if __name__=="__main__":
    MainApp().run()