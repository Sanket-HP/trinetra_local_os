from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from datetime import datetime

from brain import answer

class TrinetraApp(App):

    def build(self):

        root = BoxLayout(
            orientation="vertical",
            padding=10,
            spacing=10
        )

        self.chat_label = Label(
            text="🤖 Trinetra Assistant Started\n",
            size_hint_y=None,
            markup=True
        )

        self.chat_label.bind(
            texture_size=self.chat_label.setter('size')
        )

        scroll = ScrollView()
        scroll.add_widget(self.chat_label)

        self.input_box = TextInput(
            hint_text="Type your message..."
        )

        send_btn = Button(text="Send")
        clear_btn = Button(text="Clear Chat")

        send_btn.bind(on_press=self.send_message)
        clear_btn.bind(on_press=self.clear_chat)

        buttons = BoxLayout(size_hint_y=0.2)
        buttons.add_widget(send_btn)
        buttons.add_widget(clear_btn)

        root.add_widget(scroll)
        root.add_widget(self.input_box)
        root.add_widget(buttons)

        return root

    def send_message(self, instance):

        user_text = self.input_box.text.strip()

        if not user_text:
            return

        response = answer(user_text)

        current_time = datetime.now().strftime("%H:%M")

        self.chat_label.text += (
            f"\n[{current_time}] You: {user_text}"
            f"\n[{current_time}] Trinetra: {response}\n"
        )

        self.input_box.text = ""

    def clear_chat(self, instance):

        self.chat_label.text = "🤖 Trinetra Assistant Started\n"

TrinetraApp().run()
