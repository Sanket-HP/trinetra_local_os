from voice import start_voice

def listen_for_wake_word():

    text = start_voice().lower()

    if "trinetra" in text:
        return True

    return False
