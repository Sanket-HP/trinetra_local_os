import os

def speak(text):
    print("Trinetra:", text)

    try:
        os.system(f'termux-tts-speak "{text}"')
    except:
        pass
