import os

def search_topic(topic):

    file_path = f"knowledge/{topic}.txt"

    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return f.read()

    return "Topic not found."
