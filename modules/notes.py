import os

NOTES_FILE = "notes.txt"

def save_note(note):
    with open(NOTES_FILE, "a") as f:
        f.write(note + "\n")

    return "Note saved successfully."

def read_notes():

    if not os.path.exists(NOTES_FILE):
        return "No notes found."

    with open(NOTES_FILE, "r") as f:
        notes = f.read()

    return notes if notes else "No notes found."

def clear_notes():

    open(NOTES_FILE, "w").close()

    return "All notes cleared."
