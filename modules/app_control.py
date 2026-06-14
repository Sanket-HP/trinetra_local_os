import os

def execute_system_command(command):

    command = command.lower()

    if command == "open youtube":
        os.system("am start -a android.intent.action.VIEW -d https://www.youtube.com")
        return "Opening YouTube"

    elif command == "open whatsapp":
        os.system("am start -n com.whatsapp/.Main")
        return "Opening WhatsApp"

    elif command == "open chrome":
        os.system("am start -n com.android.chrome/com.google.android.apps.chrome.Main")
        return "Opening Chrome"

    elif command == "open camera":
        os.system("am start -a android.media.action.IMAGE_CAPTURE")
        return "Opening Camera"

    elif command == "open settings":
        os.system("am start -a android.settings.SETTINGS")
        return "Opening Settings"

    elif command == "open gmail":
        os.system("am start -n com.google.android.gm/.ConversationListActivityGmail")
        return "Opening Gmail"

    elif command == "open play store":
        os.system("am start -n com.android.vending/com.google.android.finsky.activities.MainActivity")
        return "Opening Play Store"

    else:
        return "Unknown system command"
