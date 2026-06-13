from kivy.app import App
from kivy.uix.label import Label

class TrinetraApp(App):
    def build(self):
        return Label(text="Welcome to Trinetra OS")

TrinetraApp().run()
