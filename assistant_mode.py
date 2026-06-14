from wake_word import listen_for_wake_word
from voice import start_voice
from brain import answer
from tts import speak

print("Trinetra Assistant Running...")

while True:

    if listen_for_wake_word():

        speak("Yes Sanket, I am listening")

        command = start_voice()

        response = answer(command)

        print(response)

        speak(response)
