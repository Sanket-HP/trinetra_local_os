from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class TrinetraHome(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', spacing=10, padding=20, **kwargs)

        self.add_widget(Label(text="Trinetra OS", font_size=32))

        self.add_widget(Button(text="AI Assistant"))
        self.add_widget(Button(text="Voice Assistant"))
        self.add_widget(Button(text="Files"))
        self.add_widget(Button(text="Settings"))

class TrinetraApp(App):
    def build(self):
        return TrinetraHome()

TrinetraApp().run()
