from datetime import datetime

def answer(query):

    query = query.lower()

    if "hello" in query:
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
