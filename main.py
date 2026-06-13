from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

from brain import answer


class TrinetraApp(App):

    def build(self):

        root = BoxLayout(
            orientation="vertical",
            padding=10,
            spacing=10
        )

        self.chat = Label(
            text="Welcome to Trinetra Assistant\n",
            size_hint_y=None,
            halign="left",
            valign="top"
        )

        self.chat.bind(
            texture_size=self.chat.setter("size")
        )

        scroll = ScrollView()
        scroll.add_widget(self.chat)

        self.input_box = TextInput(
            hint_text="Type a message...",
            size_hint_y=None,
            height=100
        )

        send_btn = Button(
            text="Send",
            size_hint_y=None,
            height=80
        )

        send_btn.bind(on_press=self.send_message)

        root.add_widget(scroll)
        root.add_widget(self.input_box)
        root.add_widget(send_btn)

        return root

    def send_message(self, instance):

        user_text = self.input_box.text

        if not user_text.strip():
            return

        response = answer(user_text)

        self.chat.text += f"\nYou: {user_text}"
        self.chat.text += f"\nTrinetra: {response}\n"

        self.input_box.text = ""


TrinetraApp().run()
