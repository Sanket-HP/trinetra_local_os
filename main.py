from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from datetime import datetime
from modules.startup import startup_report

from voice import start_voice
from brain import answer
from tts import speak


class TrinetraApp(App):

    def build(self):

        root = BoxLayout(
            orientation="vertical",
            padding=10,
            spacing=10
        )

        self.chat_label = Label(
            text="🤖 Trinetra Assistant Ready\n",
            size_hint_y=None,
            text_size=(400, None),
            markup=True
        )

        self.chat_label.text = startup_report()

        self.chat_label.bind(
            texture_size=self.chat_label.setter("size")
        )

        scroll = ScrollView()
        scroll.add_widget(self.chat_label)

        voice_btn = Button(
            text="🎤 Talk to Trinetra",
            size_hint_y=0.15
        )

        voice_btn.bind(on_press=self.voice_input)

        root.add_widget(scroll)
        root.add_widget(voice_btn)

        return root

    def voice_input(self, instance):

        try:

            text = start_voice()

            if not text:
                return

            response = answer(text)

            current_time = datetime.now().strftime("%H:%M:%S")

            self.chat_label.text += (
                f"\n[{current_time}] You 🎤: {text}"
                f"\n[{current_time}] Trinetra 🤖: {response}\n"
            )

            speak(response)

        except Exception as e:

            current_time = datetime.now().strftime("%H:%M:%S")

            self.chat_label.text += (
                f"\n[{current_time}] Error: {str(e)}\n"
            )

            speak("Sorry, an error occurred")


if __name__ == "__main__":
    TrinetraApp().run()
