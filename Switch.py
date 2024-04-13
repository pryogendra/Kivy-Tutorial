from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.widget import Widget

#Window.size=(400,400)
Builder.load_file("switch.kv")
class Root(Widget):
    def clicked(self,obj,state):
        if state:
            self.ids.label.text=f'Switch is on.'
        else:
            self.ids.label.text="Switch is off."
class MainApp(App):
    def build(self):
        return Root()
if __name__=="__main__":
    MainApp().run()