from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class Root(Widget):
    def on_touch_down(self, touch):
        print(touch)


class TouchApp(App):
    def build(self):
        return Root()

if __name__=="__main__":
    TouchApp().run()
