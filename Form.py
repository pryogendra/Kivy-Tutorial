from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class MainWidget(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols=2
        self.add_widget(Label(text="Name : "))
        self.name=TextInput(multiline=False)
        self.add_widget(self.name)
        self.add_widget(Label(text="Age : "))
        self.age = TextInput(multiline=False)
        self.add_widget(self.age)
        self.add_widget(Label(text="Standard : "))
        self.std = TextInput(multiline=False)
        self.add_widget(self.std)
        self.b1=Button(text="Submit",font_size=32)
        self.add_widget(self.b1)
        self.b1.bind(on_press=self.press)
    def press(self,instance):
        name=self.name.text
        age=self.age.text
        std=self.std.text
        self.add_widget(Label(text=f"Hi {name}. You are {age} years old. You are studying in {std}."))

        self.name.text=""
        self.age.text=""
        self.std.text=""

class FormApp(App):
    def build(self):
        return MainWidget()

if __name__=="__main__":
    FormApp().run()
