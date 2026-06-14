import subprocess
import json

def get_battery_info():
    try:
        result = subprocess.check_output(
            ["termux-battery-status"]
        ).decode()

        data = json.loads(result)

        return (
            f"Battery: {data['percentage']}%\n"
            f"Status: {data['status']}"
        )

    except Exception as e:
        return f"Battery Error: {e}"
