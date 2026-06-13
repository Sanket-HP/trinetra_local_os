from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class TrinetraApp(App):

    def build(self):

        self.layout = BoxLayout(
            orientation='vertical',
            padding=20,
            spacing=10
        )

        self.output = Label(
            text="Welcome to Trinetra Assistant"
        )

        self.input_box = TextInput(
            hint_text="Type your message"
        )

        send_btn = Button(
            text="Send"
        )

        send_btn.bind(on_press=self.process_message)

        self.layout.add_widget(self.output)
        self.layout.add_widget(self.input_box)
        self.layout.add_widget(send_btn)

        return self.layout

    def process_message(self, instance):

        user_text = self.input_box.text

        response = self.trinetra_brain(user_text)

        self.output.text = response

    def trinetra_brain(self, text):

        text = text.lower()

        if "hello" in text:
            return "Hello, I am Trinetra."

        elif "name" in text:
            return "My name is Trinetra."

        elif "time" in text:
            from datetime import datetime
            return datetime.now().strftime("%H:%M:%S")

        else:
            return f"You said: {text}"

TrinetraApp().run()
