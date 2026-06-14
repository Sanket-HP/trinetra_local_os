def execute(command):
    command = command.lower()

    if "battery" in command:
        print("Battery information unavailable")

    elif "storage" in command:
        print("Storage command not supported in APK mode")

    elif "time" in command:
        import datetime
        print(datetime.datetime.now())

    else:
        print("Unknown command")
