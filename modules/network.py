import subprocess

def get_network_info():
    try:
        result = subprocess.check_output(
            ["termux-wifi-connectioninfo"]
        ).decode()

        return result

    except Exception as e:
        return f"Network Error: {e}"
