from datetime import datetime

from modules.notes import save_note, read_notes, clear_notes
from modules.calculator import calculate
from modules.reminders import add_reminder, show_reminders
from modules.system import device_info
from modules.knowledge import search_topic
from modules.local_ai import ask_ai
from modules.app_control import execute_system_command

from memory_manager import save_memory, load_memory
from intent_engine import detect_intent


def answer(query):
    query = query.lower().strip()

    intent = detect_intent(query)

    # Memory
    if query.startswith("remember "):
        text = query.replace("remember ", "")
        save_memory(text)
        return "Memory saved."

    elif query.startswith("open "):
        return execute_system_command(query)

    elif query == "recall" or "my project" in query or "memory" in query:
        memory = load_memory()
        return memory if memory else "No memory found."

    # Notes
    elif query.startswith("save note "):
        return save_note(query.replace("save note ", ""))

    elif query == "show notes":
        return read_notes()

    elif query == "clear notes":
        return clear_notes()

    # Reminders
    elif query.startswith("remind "):
        return add_reminder(query.replace("remind ", ""))

    elif query == "show reminders":
        return show_reminders()

    # Calculator
    elif query.startswith("calc "):
        return calculate(query.replace("calc ", ""))

    # App Control
    elif query.startswith("open "):
        return execute_system_command(query)

    # Intent Based System Commands
    elif intent == "battery":
        return execute_system_command("battery")

    elif intent == "storage":
        return execute_system_command("storage")

    elif intent == "camera":
        return execute_system_command("open camera")

    elif intent == "time":
        return datetime.now().strftime("%H:%M:%S")

    # Device Information
    elif query == "device info":
        return device_info()

    # Built-in Knowledge
    elif query.startswith("search "):
        return search_topic(query.replace("search ", ""))

    # Greetings
    elif "hello" in query:
        return "Hello Sanket, I am Trinetra."

    elif "who are you" in query:
        return "I am Trinetra Assistant."

    elif "developer" in query:
        return "My developer is Sanket."

    elif "date" in query:
        return datetime.now().strftime("%d-%m-%Y")

    elif "bye" in query:
        return "Goodbye Sanket."

    # Everything Else → AI
    else:
        return ask_ai(query)
