from kivy.app import App
from kivy.uix.button import Button
class HelloApp(App):
    def build(self):
        l1=Button(text="Hello World !",
                  font_size="50dp",
                  color=(1,0,.5,.5),
                  markup=False,
                  pos=("100dp","200dp"),
                  size_hint=(.5,.2))
        return l1
#if __name__=="__main__":
HelloApp().run()
