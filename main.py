from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import time


class FoodAnalyser(MDApp):

    def build(self):
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_file('bottom_bar.kv')

    def open_camera(self):
        layout = BoxLayout(orientation='vertical')
        self.camera = Camera(play=True, resolution=(640, 480))
        button = Button(text="take picture", size_hint=(None, None), size=("200dp", "50dp"))
        button.bind(on_release=self.take_picture)
        layout.add_widget(self.camera)
        layout.add_widget(button)
        self.root.add_widget(layout)

    def take_picture(self, *args):
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        self.camera.export_to_png(f"photo_{timestamp}.png")

FoodAnalyser().run()
