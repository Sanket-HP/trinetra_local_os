import os

def execute(command):
    command = command.lower()

    if "battery" in command:
        os.system("termux-battery-status")

    elif "storage" in command:
        os.system("df -h /storage/emulated")

    elif "time" in command:
        os.system("date")

    else:
        print("Unknown command")
