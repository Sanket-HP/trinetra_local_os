import json
import os

MEMORY_FILE = "memory.json"

def save_memory(text):

    memories = []

    if os.path.exists(MEMORY_FILE):

        try:
            with open(MEMORY_FILE, "r") as f:
                data = json.load(f)
                memories = data.get("memories", [])
        except:
            memories = []

    memories.append(text)

    with open(MEMORY_FILE, "w") as f:
        json.dump({"memories": memories}, f, indent=4)

def load_memory():

    if not os.path.exists(MEMORY_FILE):
        return "No memory found."

    with open(MEMORY_FILE, "r") as f:
        data = json.load(f)

    memories = data.get("memories", [])

    if not memories:
        return "No memory found."

    result = ""

    for i, memory in enumerate(memories, start=1):
        result += f"{i}. {memory}\n"

    return result.strip()
