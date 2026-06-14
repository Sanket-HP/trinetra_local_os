from modules.battery import get_battery_info

def startup_report():

    return (
        "🤖 Trinetra Ready\n\n"
        + get_battery_info()
    )
