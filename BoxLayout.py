from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class RootWidget(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.B1=Button(text="Button1")
        B2=Button(text="Button2")
        L1=Label(text="Label1")
        L2=Label(text="Label2")
        self.add_widget(self.B1)
        self.add_widget(L1)
        self.add_widget(B2)
        self.add_widget(L2)
class TouchApp(App):
    def build(self):
        return RootWidget()

if __name__=="__main__":
    TouchApp().run()