import subprocess

def start_voice():

    try:

        result = subprocess.check_output(
            [
                "termux-speech-to-text"
            ],
            text=True
        ).strip()

        if not result:
            return ""

        if "ERROR" in result:
            return ""

        return result

    except Exception as e:

        return ""
