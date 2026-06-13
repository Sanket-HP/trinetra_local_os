from datetime import datetime
from modules.notes import save_note, read_notes, clear_notes
from modules.calculator import calculate

def answer(query):
    query = query.lower()

    if query.startswith("save note "):
        note = query.replace("save note ", "")
        return save_note(note)

    elif query == "show notes":
        return read_notes()

    elif query == "clear notes":
        return clear_notes()

    elif query.startswith("calc "):
        expression = query.replace("calc ", "")
        return calculate(expression)

    elif "hello" in query:
        return "Hello Sanket, I am Trinetra."

    elif "who are you" in query:
        return "I am Trinetra Assistant."

    elif "developer" in query:
        return "My developer is Sanket."

    elif "time" in query:
        return datetime.now().strftime("%H:%M:%S")

    elif "date" in query:
        return datetime.now().strftime("%d-%m-%Y")

    elif "bye" in query:
        return "Goodbye Sanket."

    else:
        return "I don't understand yet."
