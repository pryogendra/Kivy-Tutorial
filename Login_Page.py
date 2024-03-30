from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
class LoginPage(GridLayout):
    def __init__(self, **kwargs):
        super(LoginPage,self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="Username  : ",size_hint=(.5,.5)))
        self.t1 = TextInput(multiline=False,size_hint=(.5,.5))
        self.add_widget(self.t1)
        self.add_widget(Label(text="Password : ",size_hint=(.5,.5)))
        self.t2 = TextInput(multiline=False,password=True,size_hint=(.5,.5))
        self.add_widget(self.t2)

class LoginApp(App):
    def build(self):
        return LoginPage()
LoginApp().run()
