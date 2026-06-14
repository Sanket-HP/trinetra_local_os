REMINDER_FILE = "reminders.txt"

def add_reminder(text):
    with open(REMINDER_FILE, "a") as f:
        f.write(text + "\n")
    return "Reminder added."

def show_reminders():
    try:
        with open(REMINDER_FILE, "r") as f:
            data = f.read()
            return data if data else "No reminders."
    except:
        return "No reminders."
