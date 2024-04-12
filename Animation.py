from kivy.animation import Animation
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.widget import Widget

#Window.size=(400,400)
Builder.load_file("animation.kv")
class Root(Widget):
    def animate(self,widget,*args):
        ani=Animation(background_color=(0,0,1,1),duration=1)
        ani += Animation(size_hint=(1, 1))
        ani += Animation(size_hint=(0.5,0.5))
        ani += Animation(pos_hint={'center_x':0.1})
        ani += Animation(pos_hint={'center_x': 0.5})
        ani.start(widget)
        ani.bind(on_complete=self.complete)
    def complete(self,*args):
        self.ids.label.text="Animation is completed now...!!"
class MainApp(App):
    def build(self):
        return Root()
if __name__=="__main__":
    MainApp().run()