from kivy.app import App
from kivy.uix.camera import Camera

class Photo(Camera):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cam=Camera(play=True)
        self.add_widget(self.cam)

class CameraApp(App):
    def build(self):
        return Photo()
CameraApp().run()
