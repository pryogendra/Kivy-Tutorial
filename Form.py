from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget


class MainWidget(Widget):
    pass
class FormApp(App):
    def build(self):
        return MainWidget()

if __name__=="__main__":
    FormApp().run()