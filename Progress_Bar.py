from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.widget import Widget

#Window.size=(400,400)
Builder.load_file("progress_bar.kv")
class Root(Widget):
    def pressed(self):
        x=self.ids.progress.value
        x+=10
        self.ids.progress.value=x
        self.ids.label.text=f'{x}%'
        self.ids.label.font_size=x
class MainApp(App):
    def build(self):
        return Root()
if __name__=="__main__":
    MainApp().run()